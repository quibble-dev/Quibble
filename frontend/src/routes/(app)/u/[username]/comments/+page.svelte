<script lang="ts">
  import CommentType from '$lib/pages/u/comment-type.svelte';
  import type { PageServerData } from './$types';

  const { data }: { data: PageServerData } = $props();
</script>

{#each data.comments ?? [] as comment}
  <CommentType {...comment} />
{/each}
