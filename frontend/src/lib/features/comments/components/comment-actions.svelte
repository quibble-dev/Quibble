<script lang="ts">
  import api, { type components } from '$lib/api';
  import { cn } from '$lib/functions/classnames';
  import { throttle } from '$lib/functions/throttle';
  import { auth_store } from '$lib/stores/auth.svelte';

  // internal types
  type Commenter = components['schemas']['ProfileBasic'];

  type Props = {
    class?: string;
    on_reply_click?: () => void;
    id: number;
    ratio: number;
    upvotes?: number[];
    downvotes?: number[];
    commenter?: Commenter;
  };

  let { id, ratio, upvotes, downvotes, class: _class, on_reply_click, commenter }: Props = $props();
  let reaction = $state<ReturnType<typeof get_reaction>>(get_reaction());

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

<div class={cn(_class, 'flex items-center gap-2')}>
  <div class="flex items-center gap-1">
    <button
      class="btn btn-sm btn-square btn-neutral"
      aria-label="upvote"
      onclick={() => throttled_handle_reaction('upvote')}
    >
      <coreicons-shape-thumbs
        variant="up"
        class="size-4"
        class:text-primary={reaction === 'upvoted'}
      ></coreicons-shape-thumbs>
    </button>
    <span class="text-sm font-medium">{ratio}</span>
    <button
      class="btn btn-sm btn-square btn-neutral"
      aria-label="downvote"
      onclick={() => throttled_handle_reaction('downvote')}
    >
      <coreicons-shape-thumbs
        variant="down"
        class="size-4"
        class:text-accent={reaction === 'downvoted'}
      ></coreicons-shape-thumbs>
    </button>
  </div>
  <button
    class="btn btn-sm btn-neutral flex cursor-pointer items-center gap-2"
    onclick={on_reply_click}
  >
    <coreicons-shape-message-circle class="size-4"></coreicons-shape-message-circle>
    <span class="text-sm font-medium">Reply</span>
  </button>
  <button class="btn btn-sm btn-neutral flex cursor-pointer items-center gap-2" disabled>
    <coreicons-shape-share class="size-4"></coreicons-shape-share>
    <span class="text-sm font-medium">Share</span>
  </button>
  <div class="dropdown-end dropdown">
    <div
      tabindex="0"
      role="button"
      class="btn btn-sm btn-square btn-ghost flex cursor-pointer items-center gap-2"
    >
      <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
    </div>
    <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
    <ul tabindex="0" class="menu dropdown-content bg-base-100 z-10 mt-2 gap-1 rounded-2xl p-1.5">
      <li>
        <button class="flex items-center gap-2 rounded-xl p-2">
          <coreicons-shape-flag class="size-4"></coreicons-shape-flag>
          <span class="text-sm font-medium capitalize">Report</span>
        </button>
      </li>
      <li class="menu-disabled">
        <button class="flex items-center gap-2 rounded-xl p-2">
          <coreicons-shape-calendar class="size-4"></coreicons-shape-calendar>
          <span class="text-sm font-medium capitalize">Save</span>
        </button>
      </li>
      {#if commenter?.id === auth_store.value.user?.profile.id}
        <li>
          <button class="text-error flex items-center gap-2 rounded-xl p-2">
            <coreicons-shape-trash variant="without-lines" class="size-4"></coreicons-shape-trash>
            <span class="text-sm font-medium capitalize">Delete</span>
          </button>
        </li>
      {/if}
    </ul>
  </div>
</div>
