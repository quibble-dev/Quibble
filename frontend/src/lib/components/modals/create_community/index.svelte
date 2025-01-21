<script lang="ts">
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import type { Nullable } from '$lib/types/shared';

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
    Create a community!
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
