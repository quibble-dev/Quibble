<script lang="ts">
  import type { ZodIssue } from 'zod';

  let { errors }: { errors: ZodIssue[] } = $props();
</script>

<ul class="flex flex-col gap-1">
  {#each errors as { message, path }}
    <li class="flex items-center gap-1 text-xs text-error">
      <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
      {path[0]} -- {message}
    </li>
  {/each}
</ul>
