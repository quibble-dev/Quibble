<script lang="ts">
  import { cn } from '$lib/functions/classnames';
  import { toast } from './toast.svelte';

  type Props = {
    inside_modal?: boolean;
  };

  let { inside_modal = false }: Props = $props();
</script>

<div
  class={cn(inside_modal && 'toast-top md:toast-bottom', 'toast toast-center z-[999] md:toast-end')}
>
  {#each toast.toasts.filter((t) => t.inside_modal === inside_modal) as t (t.id)}
    <div
      class="alert flex items-center gap-2 rounded-2xl border border-neutral bg-base-300 p-2.5 pl-3"
    >
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
