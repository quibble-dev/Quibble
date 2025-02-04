<script lang="ts">
  import Toaster from '$lib/components/ui/toast';
  import { cn } from '$lib/functions/classnames';
  import type { Nullable } from '$lib/types/shared';
  import type { Snippet } from 'svelte';

  type Props = {
    children: Snippet<[]>;
    open: boolean;
    onclose: () => void;
    class?: string;
  };

  let { children, open, onclose, class: klass }: Props = $props();

  let dialog_el = $state<Nullable<HTMLDialogElement>>(null);

  $effect(() => {
    if (open) {
      dialog_el?.showModal();
    } else {
      dialog_el?.close();
    }
  });
</script>

<dialog
  bind:this={dialog_el}
  class="modal modal-bottom px-4 backdrop-blur sm:modal-middle"
  {onclose}
>
  <div
    class={cn(
      klass,
      'modal-box !rounded-t-2xl border border-neutral bg-base-300 p-4 duration-300 scrollbar-none md:!rounded-2xl'
    )}
  >
    {@render children()}
  </div>
  <form method="dialog" class="modal-backdrop">
    <button>close</button>
  </form>
  <!-- render toasts -->
  <!-- https://stackoverflow.com/questions/77099074/layering-toast-alerts-above-dialog-modal -->
  <!-- https://github.com/saadeghi/daisyui/issues/2858#issuecomment-2010246981 -->
  <Toaster inside_modal={true} />
</dialog>
