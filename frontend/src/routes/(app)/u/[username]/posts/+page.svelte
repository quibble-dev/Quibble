<script lang="ts">
  import PostCard from '$lib/features/posts/components/post-card.svelte';
  import type { PageServerData } from './$types';

  const { data }: { data: PageServerData } = $props();
</script>

{#each data.posts ?? [] as post}
  <PostCard always_on_card={true} {...post} />
{/each}
