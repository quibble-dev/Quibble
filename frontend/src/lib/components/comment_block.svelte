<script lang="ts">
  import { FormatDate } from '$lib/functions/date';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import type { CommentTree } from '$lib/types/comment';
  import CommentBlock from './comment_block.svelte';
  import Avatar from './ui/avatar.svelte';

  let comment: CommentTree = $props();

  const authStore = createAuthStore();

  const is_upvoted = $derived.by(check_if_upvoted);
  function check_if_upvoted() {
    if (authStore.state.profile && comment.upvotes) {
      return comment.upvotes.includes(authStore.state.profile.id);
    } else {
      return false;
    }
  }
</script>

<div class="flex items-start gap-2">
  <div class="flex flex-col items-center gap-2 self-stretch">
    {#if comment.deleted}
      <Avatar class="size-8 flex-shrink-0" />
    {:else}
      <a href="/u/{comment.quibbler?.username}">
        <Avatar src={comment.quibbler?.avatar} class="size-8 flex-shrink-0" />
      </a>
    {/if}
    <div role="button" class="group grid size-full place-items-center">
      <div
        class="h-full w-px rounded-full bg-neutral transition-colors group-hover:w-0.5
        group-hover:bg-primary"
      ></div>
    </div>
  </div>
  <div class="flex flex-col gap-2">
    <div class="flex items-center gap-1.5">
      {#if comment.deleted}
        <h3 class="text-xs font-semibold">[deleted]</h3>
      {:else}
        <a
          href="/u/{comment.quibbler?.username}"
          class="flex items-center gap-2 hover:text-accent hover:underline"
        >
          <h3 class="text-xs font-semibold">u/{comment.quibbler?.username}</h3>
        </a>
      {/if}
      <coreicons-shape-circle variant="filled" class="size-0.5 text-base-content/75"
      ></coreicons-shape-circle>
      <span class="text-xs font-medium text-base-content/75"
        >{new FormatDate(comment.created_at).timeAgo()}</span
      >
    </div>
    <p class="whitespace-pre-wrap text-sm text-info">{comment.content}</p>
    <!-- comment options -->
    <div class="flex items-center gap-4">
      <div class="flex items-center gap-2">
        <button class="flex items-center gap-2" aria-label="upvote">
          <coreicons-shape-thumbs
            variant="up"
            class="size-4"
            class:text-primary={is_upvoted}
          ></coreicons-shape-thumbs>
        </button>
        <span class="text-sm font-medium">{comment.ratio}</span>
        <button class="flex items-center gap-2" aria-label="downvote">
          <coreicons-shape-thumbs variant="down" class="size-4"></coreicons-shape-thumbs>
        </button>
      </div>
      <button class="flex items-center gap-2">
        <coreicons-shape-share class="size-4"></coreicons-shape-share>
        <span class="text-sm font-medium">Share</span>
      </button>
      <button class="flex items-center gap-2" aria-label="more">
        <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
      </button>
    </div>
    <!-- extra space -->
    <div></div>
    <!-- render reply comments if any -->
    {#if comment.children && comment.children.length > 0}
      {#each comment.children as child}
        <CommentBlock {...child} />
      {/each}
    {/if}
  </div>
</div>
