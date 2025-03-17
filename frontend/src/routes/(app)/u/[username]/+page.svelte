<script lang="ts">
  import type { components } from '$lib/api';
  import CommentType from '$lib/pages/u/comment-type.svelte';
  import PostType from '$lib/pages/u/post-type.svelte';
  import type { CommentOverview as Comment } from '$lib/types/comment';
  import type { PageServerData } from './$types';

  // internal types
  type Overview = components['schemas']['Overview'];
  type Post = components['schemas']['Post'];

  // generic types
  interface TypedOverview<T extends Record<string, unknown>> extends Overview {
    content: T;
  }

  // type guards
  function is_comment_type(item: Overview): item is TypedOverview<Comment> {
    return item.content_type === 'comment';
  }

  function is_post_type(item: Overview): item is TypedOverview<Post> {
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
