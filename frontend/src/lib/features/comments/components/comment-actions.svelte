<script lang="ts">
  import api from '$lib/api';
  import { cn } from '$lib/functions/classnames';
  import { throttle } from '$lib/functions/throttle';
  import { authStore } from '$lib/stores/auth.svelte';

  type Props = {
    id: number;
    ratio: number;
    upvotes?: number[];
    downvotes?: number[];
    class?: string;
    on_reply_click?: () => void;
  };

  let { id, ratio, upvotes, downvotes, class: _class, on_reply_click }: Props = $props();
  let reaction = $state<ReturnType<typeof get_reaction>>(get_reaction());

  $effect(() => {
    reaction = get_reaction();
  });

  function get_reaction(): 'upvoted' | 'downvoted' | null {
    if (authStore.value.user) {
      if (upvotes?.includes(authStore.value.user.profile.id)) return 'upvoted';
      else if (downvotes?.includes(authStore.value.user.profile.id)) return 'downvoted';
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

      const { response } = await api.PATCH('/comments/{id}/reaction/', {
        body: { action },
        params: { path: { id } }
      });

      if (!response.ok) throw new Error(`request failed with status: ${response.status}`);
    } catch (err) {
      console.error(err);
    }
  }
</script>

<div class={cn(_class, 'flex items-center gap-4')}>
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
  <button class="flex cursor-pointer items-center gap-2" onclick={on_reply_click}>
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
