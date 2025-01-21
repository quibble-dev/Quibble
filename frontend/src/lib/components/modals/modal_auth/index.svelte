<script lang="ts">
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import type { Nullable } from '$lib/types/shared';
  import type { FormsState, FormSubmitData, Forms } from '../types';
  import { create_form_history } from '../utils/history.svelte';
  import forms from './forms';

  type AuthForms = Forms<typeof forms>;
  type AuthFormsState = FormsState<typeof forms>;

  const form_history = create_form_history<typeof forms>('join');
  let current_form = $derived(forms[form_history.history.at(-1) ?? 'join']);

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

  let dialog_element = $state<Nullable<HTMLDialogElement>>(null);

  const modalsStore = createModalsStore();

  $effect(() => {
    if (modalsStore.state.get('auth')) {
      dialog_element?.showModal();
    } else {
      dialog_element?.close();
    }
  });
</script>

<dialog
  class="modal modal-bottom sm:modal-middle"
  bind:this={dialog_element}
  onclose={() => modalsStore.close('auth')}
>
  <div class="modal-box !w-[25rem]">
    {#await current_form then Form}
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
      onclick={() => dialog_element?.close()}
    >
      <coreicons-shape-x class="size-5" variant="no-border"></coreicons-shape-x>
    </button>
  </div>
  <form method="dialog" class="modal-backdrop">
    <button>close</button>
  </form>
</dialog>
