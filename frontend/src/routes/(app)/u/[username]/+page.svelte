<script lang="ts">
  import type { components } from '$lib/api';
  import CommentType from '$lib/pages/u/comment-type.svelte';
  import PostType from '$lib/pages/u/post-type.svelte';
  import type { PageServerData } from './$types';

  type OverviewItem = components['schemas']['Overview'];
  type Comment = components['schemas']['Comment'];
  type Post = components['schemas']['Post'];

  // type guards
  function is_comment_type(item: OverviewItem): item is OverviewItem & { content: Comment } {
    return item.content_type === 'comment';
  }

  function is_post_type(item: OverviewItem): item is OverviewItem & { content: Post } {
    return item.content_type === 'post';
  }

  const { data }: { data: PageServerData } = $props();
</script>

{#each data.overview ?? [] as item}
  {#if is_comment_type(item)}
    <CommentType {...item.content} />
  {:else if is_post_type(item)}
    <PostType {...item.content} />
  {/if}
{/each}
