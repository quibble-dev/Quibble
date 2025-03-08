<script lang="ts">
  import { toast } from './toast.svelte';

  // internal types
  type Props = {
    inside_modal?: boolean;
  };

  let { inside_modal = false }: Props = $props();
</script>

<div class="toast toast-center toast-bottom z-[999]">
  {#each toast.toasts.filter((t) => t.inside_modal === inside_modal) as t (t.id)}
    <div class="alert flex flex-col items-center gap-2 rounded-2xl p-2.5 pl-3 md:flex-row">
      <coreicons-shape-info class="size-4"></coreicons-shape-info>
      <span class="text-sm">{t.message}</span>
      <button
        class="btn btn-square btn-ghost size-4 rounded-lg md:size-6"
        aria-label="Close toast"
        onclick={() => toast.dismiss(t.id)}
      >
        <coreicons-shape-x variant="no-border" class="size-4"></coreicons-shape-x>
      </button>
    </div>
  {/each}
</div>
