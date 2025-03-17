<script lang="ts">
  import api from '$lib/api';
  import type { components } from '$lib/api';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { cn } from '$lib/functions/classnames';
  import { FormatDate } from '$lib/functions/date';
  import { throttle } from '$lib/functions/throttle';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import type { CommentTree } from '$lib/types/comment';
  import CommentBlock from './comment-block.svelte';
  import CommentBox from './comment-box.svelte';

  type Comment = components['schemas']['Comment'];

  let comment_prop: CommentTree = $props();
  let comment = $state(comment_prop);

  const authStore = createAuthStore();

  let collapsed = $state(comment.collapsed);
  let show_comment_box = $state(false);

  let ratio = $state(comment.ratio);
  let reaction = $state<ReturnType<typeof get_reaction>>(get_reaction());

  $effect(() => {
    reaction = get_reaction();
  });

  function get_reaction(): 'upvoted' | 'downvoted' | null {
    if (authStore.state.user) {
      if (comment.upvotes?.includes(authStore.state.user.profile.id)) return 'upvoted';
      else if (comment.downvotes?.includes(authStore.state.user.profile.id)) return 'downvoted';
      else return null;
    } else {
      return null;
    }
  }

  function toggle_collapse() {
    collapsed = !collapsed;
  }

  async function handle_comment(data: { comment: Comment }) {
    show_comment_box = false;

    const new_comment: CommentTree = { ...data.comment, children: [], collapsed: false };
    comment.children.unshift(new_comment);
  }

  const throttled_handle_reaction = throttle(handle_reaction, 500);
  async function handle_reaction(action: 'upvote' | 'downvote') {
    try {
      if (reaction === `${action}d`) {
        // undo reaction
        reaction = null;
        ratio += action === 'upvote' ? -1 : 1;
      } else {
        if (reaction === 'upvoted') ratio -= 1;
        if (reaction === 'downvoted') ratio += 1;

        reaction = `${action}d`;
        if (reaction === 'upvoted') ratio += 1;
        if (reaction === 'downvoted') ratio -= 1;
      }

      const { response } = await api.PATCH('/comments/{id}/reaction/', {
        body: { action },
        params: { path: { id: comment.id } }
      });

      if (!response.ok) throw new Error(`request failed with status: ${response.status}`);
    } catch (err) {
      console.error(err);
    }
  }
</script>

<div class="flex items-start gap-2">
  {#if collapsed}
    <button
      onclick={toggle_collapse}
      class="btn btn-neutral ml-1 size-6 rounded-full p-0"
      aria-label="toggle collapse"
    >
      <coreicons-shape-plus variant="circle" class="size-4"></coreicons-shape-plus>
    </button>
  {:else}
    <div class="flex flex-col items-center gap-2 self-stretch">
      {#if comment.deleted}
        <Avatar class="size-8 shrink-0" />
      {:else}
        <a href="/u/{comment.commenter?.username}">
          <Avatar src={comment.commenter?.avatar} class="size-8 shrink-0" />
        </a>
      {/if}
      <button
        onclick={toggle_collapse}
        aria-label="toggle collapse"
        class="group grid size-full place-items-center"
      >
        <div
          class="bg-neutral group-hover:bg-primary h-full w-px rounded-full transition-colors
        group-hover:w-0.5"
        ></div>
      </button>
    </div>
  {/if}
  <div class={cn(collapsed && 'ml-1 self-center', 'flex w-full flex-col gap-2')}>
    <div class="flex items-center gap-1.5">
      {#if comment.deleted}
        <h3 class="text-xs font-semibold">[deleted]</h3>
      {:else}
        <a
          href="/u/{comment.commenter?.username}"
          class="hover:text-accent flex items-center gap-2 hover:underline"
        >
          <h3 class="text-xs font-semibold">u/{comment.commenter?.username}</h3>
        </a>
      {/if}
      <coreicons-shape-circle variant="filled" class="text-base-content/75 size-0.5"
      ></coreicons-shape-circle>
      <span class="text-base-content/75 text-xs font-medium"
        >{new FormatDate(comment.created_at).timeAgo()}</span
      >
    </div>
    <div class="flex flex-col gap-2" class:hidden={collapsed}>
      <p class="text-info text-sm whitespace-pre-wrap">{comment.content}</p>
      <!-- comment options -->
      <div class="flex items-center gap-4">
        <div class="flex items-center gap-2 [&>button]:flex [&>button]:cursor-pointer">
          <button aria-label="upvote" onclick={() => throttled_handle_reaction('upvote')}>
            <coreicons-shape-thumbs
              variant="up"
              class="size-4"
              class:text-primary={reaction === 'upvoted'}
            ></coreicons-shape-thumbs>
          </button>
          <span class="text-sm font-medium">{ratio}</span>
          <button aria-label="downvote" onclick={() => throttled_handle_reaction('downvote')}>
            <coreicons-shape-thumbs
              variant="down"
              class="size-4"
              class:text-accent={reaction === 'downvoted'}
            ></coreicons-shape-thumbs>
          </button>
        </div>
        <button
          class="flex cursor-pointer items-center gap-2"
          onclick={() => (show_comment_box = true)}
        >
          <coreicons-shape-message-circle class="size-4"></coreicons-shape-message-circle>
          <span class="text-sm font-medium">Reply</span>
        </button>
        <button class="flex cursor-pointer items-center gap-2">
          <coreicons-shape-share class="size-4"></coreicons-shape-share>
          <span class="text-sm font-medium">Share</span>
        </button>
        <button class="flex cursor-pointer items-center gap-2" aria-label="more">
          <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
        </button>
      </div>
      {#if show_comment_box}
        <!-- reply comment -->
        <CommentBox
          path={comment.path}
          oncancel={() => (show_comment_box = false)}
          oncomment={handle_comment}
        />
      {/if}
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
</div>
