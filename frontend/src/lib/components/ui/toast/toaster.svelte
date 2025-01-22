<script lang="ts">
  import { toast } from './toast.svelte';
</script>

{#each toast.state as t (t.id)}
  <div class="toast">
    <div class="alert alert-info">
      <span>{t.message}</span>
    </div>
  </div>
{/each}
