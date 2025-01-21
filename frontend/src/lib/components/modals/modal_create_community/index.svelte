<script lang="ts">
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import type { Nullable } from '$lib/types/shared';
  import type { FormsState, FormSubmitData, Forms } from '../types';
  import forms from './forms';

  type CForms = Forms<typeof forms>;
  type CFormsState = FormsState<typeof forms>;

  let _form = $state<CForms>('introduction');
  let prev_form_history = $state<CForms[]>(['introduction']);

  let current_form = $derived(forms[_form]);

  const initial_forms_state = Object.fromEntries(
    Object.keys(forms).map((key) => [key, {}])
  ) as CFormsState;

  let forms_state = $state<CFormsState>(initial_forms_state);

  function update_forms_state(form: CForms, data: FormSubmitData) {
    forms_state[form] = { ...forms_state[form], ...data };
  }

  function goto_form(form: CForms) {
    // if navigating to a form thats already in the history stack,
    // truncate the stack upto the most recent occurance of that form
    // (avoiding duplicate entiries)
    const form_index = prev_form_history.findIndex((entry) => entry === form);
    if (form_index > -1) {
      // if exists
      prev_form_history = prev_form_history.slice(0, form_index + 1);
    } else {
      // otherwise, push current form to prev_form_history
      prev_form_history.push(form);
    }
    // update form
    _form = form;
  }

  function handle_go_back() {
    // remove current form from history stack
    prev_form_history.pop();
    // set current_form to previous form in history stack (the one before removed form)
    const prev_form = prev_form_history.at(-1);
    if (prev_form) {
      _form = prev_form;
    }
  }

  let dialog_element = $state<Nullable<HTMLDialogElement>>(null);

  const modalsStore = createModalsStore();

  $effect(() => {
    if (modalsStore.state.get('create_community')) {
      dialog_element?.showModal();
    } else {
      dialog_element?.close();
    }
  });
</script>

<dialog
  class="modal modal-bottom sm:modal-middle"
  bind:this={dialog_element}
  onclose={() => modalsStore.close('create_community')}
>
  <div class="modal-box">
    {#await current_form then Form}
      <Form.default {forms_state} {update_forms_state} {goto_form} />
    {/await}
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
