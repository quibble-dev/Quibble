<script lang="ts">
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import BaseModal from '../_components/base-modal.svelte';
  import { create_form_history } from '../_utils/history.svelte';
  import type { FormsState, FormSubmitData, Forms } from '../types';
  import forms from './forms';

  type AuthForms = Forms<typeof forms>;
  type AuthFormsState = FormsState<typeof forms>;

  const modalsStore = createModalsStore();

  const form_history = create_form_history<typeof forms>('join');
  let form = $derived(forms[form_history.history.at(-1) ?? 'join']);

  const initial_forms_state = Object.fromEntries(
    Object.keys(forms).map((key) => [key, {}])
  ) as AuthFormsState;

  let forms_state = $state<AuthFormsState>(initial_forms_state);

  function update_forms_state(form: AuthForms, data: FormSubmitData) {
    forms_state[form] = { ...forms_state[form], ...data };
  }

  function goto_form(form: AuthForms) {
    form_history.go_to_form(form);
  }

  function handle_go_back() {
    form_history.go_back();
  }

  function handle_modal_close() {
    modalsStore.close('auth');
  }
</script>

<BaseModal
  open={modalsStore.state.get('auth') === true}
  onclose={handle_modal_close}
  class="max-w-[25rem] md:max-w-[25rem]"
>
  {#await form then Form}
    <Form.default {forms_state} {update_forms_state} {goto_form} />
  {/await}
  {#if form_history.history.length > 1}
    <div
      class="tooltip tooltip-right absolute left-2.5 top-2.5 flex before:capitalize"
      data-tip={form_history.history.at(-2)?.replace('_', ' ')}
    >
      <button
        class="btn btn-square btn-circle btn-ghost btn-sm"
        aria-label="Close modal"
        onclick={handle_go_back}
      >
        <coreicons-shape-arrow class="size-5" variant="left"></coreicons-shape-arrow>
      </button>
    </div>
  {/if}
  <button
    class="btn btn-square btn-circle btn-ghost btn-sm absolute right-2.5 top-2.5"
    aria-label="Close modal"
    onclick={handle_modal_close}
  >
    <coreicons-shape-x class="size-5" variant="no-border"></coreicons-shape-x>
  </button>
</BaseModal>
