<script lang="ts">
  import api from '$lib/api';
  import { cn } from '$lib/functions/classnames';
  import { throttle } from '$lib/functions/throttle';
  import { auth_store } from '$lib/stores/auth.svelte';
  import readable from 'readable-numbers';

  type Props = {
    id: string;
    ratio: number;
    upvotes?: number[];
    downvotes?: number[];
    comments?: number[];
    class?: string;
  };

  let { id, ratio, upvotes, downvotes, comments, class: _class }: Props = $props();
  let reaction = $state<ReturnType<typeof get_reaction>>();

  $effect(() => {
    reaction = get_reaction();
  });

  function get_reaction(): 'upvoted' | 'downvoted' | null {
    if (auth_store.value.user) {
      if (upvotes?.includes(auth_store.value.user.profile.id)) return 'upvoted';
      else if (downvotes?.includes(auth_store.value.user.profile.id)) return 'downvoted';
      else return null;
    } else {
      return null;
    }
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

      const { response } = await api.PATCH('/posts/{id}/reaction/', {
        body: { action },
        params: { path: { id } }
      });

      if (!response.ok) throw new Error(`request failed with status: ${response.status}`);
    } catch (err) {
      console.error(err);
    }
  }
</script>

<div class={cn(_class, 'flex items-center gap-2')}>
  <div class="bg-neutral rounded-field relative flex items-center gap-1">
    <button
      class="btn btn-primary btn-soft btn-sm btn-square"
      class:btn-active={reaction === 'upvoted'}
      aria-label="Upvote post"
      onclick={() => throttled_handle_reaction('upvote')}
    >
      <coreicons-shape-thumbs variant="up" class="size-4"></coreicons-shape-thumbs>
    </button>
    <span class="text-xs font-medium md:text-sm">{readable(ratio)}</span>
    <button
      class="btn btn-accent btn-soft btn-sm btn-square"
      class:btn-active={reaction === 'downvoted'}
      aria-label="Downvote post"
      onclick={() => throttled_handle_reaction('downvote')}
    >
      <coreicons-shape-thumbs variant="down" class="size-4"></coreicons-shape-thumbs>
    </button>
  </div>
  <button class="btn btn-sm btn-neutral relative px-2">
    <coreicons-shape-forum class="size-4"></coreicons-shape-forum>
    <span class="text-xs font-medium md:text-sm">{readable(comments?.length ?? 0)}</span>
  </button>
  <button class="btn btn-sm btn-neutral relative hidden md:flex">
    <coreicons-shape-share class="size-4"></coreicons-shape-share>
    <span class="text-sm font-medium">Share</span>
  </button>
  <button class="btn btn-sm btn-ghost hover:btn-neutral btn-square relative" aria-label="more">
    <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
  </button>
</div>
