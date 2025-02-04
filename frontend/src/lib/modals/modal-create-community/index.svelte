<script lang="ts">
  import { goto } from '$app/navigation';
  import { toast } from '$lib/components/ui/toast';
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import BaseModal from '../_components/base-modal.svelte';
  import { create_form_history } from '../_utils/history.svelte';
  import type { FormsState, FormSubmitData, Forms } from '../types';
  import forms from './forms';

  type CCForms = Forms<typeof forms>;
  type CCFormsState = FormsState<typeof forms>;

  const modalsStore = createModalsStore();

  const form_history = create_form_history<typeof forms>('introduction');
  let form = $derived(forms[form_history.history.at(-1) ?? 'introduction']);

  const form_keys = Object.keys(forms);
  const form_step = $derived.by<'start' | 'middle' | 'end'>(() => {
    const current_form_index = form_keys.indexOf(form_history.history.at(-1) as string);
    if (current_form_index === 0) {
      return 'start';
    } else if (current_form_index === form_keys.length - 1) {
      return 'end';
    } else {
      return 'middle';
    }
  });

  const initial_forms_state = Object.fromEntries(
    Object.keys(forms).map((key) => [key, { valid: false, data: {} }])
  ) as CCFormsState;

  let forms_state = $state<CCFormsState>(initial_forms_state);

  let is_valid = $derived(
    (forms_state[form_history.history.at(-1) as CCForms] as { valid: boolean }).valid
  );

  function update_forms_state(form: CCForms, data: FormSubmitData) {
    forms_state[form] = { ...forms_state[form], ...data };
  }

  function goto_form(form: CCForms) {
    form_history.go_to_form(form);
  }

  function handle_modal_close() {
    modalsStore.close('create_community');
  }

  async function handle_create_click() {
    const { name, description } = (
      forms_state.introduction as { data: { name: string; description: string } }
    ).data;
    // send request to kit server
    const res = await fetch('/api/communities/', {
      method: 'POST',
      body: JSON.stringify({
        name,
        description
      })
    });

    const { data, success, error } = await res.json();

    if (!success && error) {
      if (error.includes('name')) goto_form('introduction');
      toast.push({ message: error, inside_modal: true });
    } else {
      modalsStore.close('create_community');
      goto(`/q/${data.name}`);
    }
  }
</script>

<BaseModal
  open={modalsStore.state.get('create_community') === true}
  onclose={handle_modal_close}
  class="flex max-w-[25rem] flex-col gap-4 md:max-w-[45rem]"
>
  <!-- async form rendering -->
  {#await form then Form}
    <Form.default {forms_state} {update_forms_state} {goto_form} />
  {/await}

  <!-- close button for the modal -->
  <button
    class="btn btn-square btn-circle btn-ghost btn-sm absolute right-2.5 top-2.5"
    aria-label="Close modal"
    onclick={handle_modal_close}
  >
    <coreicons-shape-x class="size-5" variant="no-border"></coreicons-shape-x>
  </button>

  <!-- form navigation and actions -->
  <div class="flex items-center justify-between">
    <!-- form step indicators -->
    <div class="flex items-center gap-2">
      {#each Object.keys(forms) as _form}
        {@const is_active = _form === form_history.history.at(-1)}
        <button
          class="size-2 rounded-full bg-base-content"
          class:opacity-50={!is_active}
          aria-label="Go to {_form}"
          onclick={() => goto_form(_form as CCForms)}
          disabled={_form === form_history.history.at(-1) ||
            (!is_valid && !(forms_state[_form as CCForms] as { valid: boolean }).valid)}
        ></button>
      {/each}
    </div>

    <!-- back and next/cancel buttons -->
    <div class="flex items-center gap-2">
      <button
        class="btn btn-ghost"
        onclick={() => {
          if (form_step === 'start') {
            handle_modal_close();
          } else {
            form_history.go_back();
          }
        }}
      >
        {form_step === 'start' ? 'Cancel' : 'Back'}
      </button>
      <button
        class="btn btn-primary"
        disabled={!is_valid}
        onclick={() => {
          if (form_step === 'end') {
            // community creation logic goes here
            handle_create_click();
          } else {
            form_history.go_next(forms);
          }
        }}
      >
        {form_step === 'end' ? 'Create' : 'Next'}
        <coreicons-shape-arrow variant="right" class="size-4"></coreicons-shape-arrow>
      </button>
    </div>
  </div>
</BaseModal>
