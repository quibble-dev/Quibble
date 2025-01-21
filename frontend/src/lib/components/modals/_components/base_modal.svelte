<script lang="ts">
  import type { Nullable } from '$lib/types/shared';
  import type { Snippet } from 'svelte';

  type Props = {
    children: Snippet<[]>;
    open: boolean;
    onclose: () => void;
    dialog_el: Nullable<HTMLDialogElement>;
  };

  let { children, open, onclose, dialog_el = $bindable() }: Props = $props();

  $effect(() => {
    if (open) {
      dialog_el?.showModal();
    } else {
      dialog_el?.close();
    }
  });
</script>

<dialog bind:this={dialog_el} class="modal modal-bottom sm:modal-middle" {onclose}>
  {@render children()}
  <form method="dialog" class="modal-backdrop">
    <button>close</button>
  </form>
</dialog>
