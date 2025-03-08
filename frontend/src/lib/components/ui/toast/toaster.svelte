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
    <div
      class="alert flex items-center gap-2 rounded-2xl border-none p-2.5 pl-3 text-xs sm:text-sm"
    >
      <coreicons-shape-info class="hidden sm:flex"></coreicons-shape-info>
      <span>{t.message}</span>
      <button
        class="btn btn-square btn-ghost btn-xs hidden rounded-lg sm:flex"
        aria-label="Close toast"
        onclick={() => toast.dismiss(t.id)}
      >
        <coreicons-shape-x variant="no-border"></coreicons-shape-x>
      </button>
    </div>
  {/each}
</div>
