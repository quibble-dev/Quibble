<script lang="ts">
  import { FormatDate } from '$lib/functions/date';
  import type { CommentTree } from '$lib/types/comment';
  import Comment from './comment.svelte';
  import Avatar from './ui/avatar.svelte';

  let { children, quibbler, created_at, deleted, content }: CommentTree = $props();
</script>

<div class="flex items-start gap-2">
  {#if deleted}
    <Avatar class="size-8" />
  {:else}
    <a href="/u/{quibbler?.username}">
      <Avatar src={quibbler?.avatar} class="size-8" />
    </a>
  {/if}
  <div class="flex flex-col gap-2">
    <div class="flex items-center gap-1.5">
      {#if deleted}
        <h3 class="text-xs font-semibold">[deleted]</h3>
      {:else}
        <a
          href="/u/{quibbler?.username}"
          class="flex items-center gap-2 hover:text-accent hover:underline"
        >
          <h3 class="text-xs font-semibold">u/{quibbler?.username}</h3>
        </a>
      {/if}
      <coreicons-shape-circle variant="filled" class="size-0.5 text-base-content/75"
      ></coreicons-shape-circle>
      <span class="text-xs font-medium text-base-content/75"
        >{new FormatDate(created_at).timeAgo()}</span
      >
    </div>
    <p class="text-sm">{content}</p>
    {#if children && children.length > 0}
      {#each children as child}
        <Comment {...child} />
      {/each}
    {/if}
  </div>
</div>
