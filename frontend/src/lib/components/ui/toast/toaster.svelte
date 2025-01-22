<script lang="ts">
  import { toast } from './toast.svelte';
</script>

{#each toast.toasts as t (t.id)}
  <div class="toast z-[999]">
    <div class="alert gap-2 rounded-2xl border-none bg-base-100 p-2.5 pl-3">
      <coreicons-shape-info class="size-4"></coreicons-shape-info>
      <span class="text-sm">{t.message}</span>
      <button
        class="btn btn-square btn-ghost size-6 rounded-lg"
        aria-label="Close toast"
        onclick={() => toast.dismiss(t.id)}
      >
        <coreicons-shape-x variant="no-border" class="size-4"></coreicons-shape-x>
      </button>
    </div>
  </div>
{/each}
