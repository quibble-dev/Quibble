<script lang="ts">
  import { page } from '$app/state';
  import type { components } from '$lib/api';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import BackdropImage from '$lib/components/ui/backdrop-image.svelte';
  import Zoom from '$lib/components/ui/zoom.svelte';
  import { cn } from '$lib/functions/classnames';
  import { FormatDate } from '$lib/functions/date';
  import { is_valid } from '$lib/functions/is-valid';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import { createLayoutTypeStore } from '$lib/stores/layout-type.svelte';
  import readable from 'readable-numbers';

  type PostProps = components['schemas']['Post'];

  let post: PostProps = $props();

  const authStore = createAuthStore(),
    layoutTypeStore = createLayoutTypeStore();

  let is_expanded = $state(false);

  const is_upvoted = $derived.by(check_if_upvoted);
  function check_if_upvoted() {
    if (authStore.state.user && post.upvotes) {
      return post.upvotes.includes(authStore.state.user.profile.id);
    } else {
      return false;
    }
  }

  function get_avatar() {
    return page.url.pathname.includes('/q/') ? post.poster.avatar : post.poster.avatar;
  }

  function get_name() {
    return page.url.pathname.includes('/q/')
      ? `u/${post.poster.username}`
      : `q/${post.community.name}`;
  }
</script>

{#snippet content_or_cover()}
  {#if is_valid(post.content)}
    <p class="text-sm font-normal">
      {post.content}
    </p>
  {:else if is_valid(post.cover)}
    <BackdropImage src={post.cover} class="z-10">
      <Zoom>
        <img src={post.cover} alt="" class="max-h-[25rem] object-contain" />
      </Zoom>
    </BackdropImage>
  {/if}
{/snippet}

{#snippet avatar_name_date_more()}
  <div class="flex items-center gap-2">
    <a
      href="/{get_name()}"
      class="hover:text-accent relative flex items-center gap-2 hover:underline"
    >
      <Avatar src={get_avatar()} class="size-6 rounded-full" />
      <h3 class="text-xs font-semibold">{get_name()}</h3>
    </a>
    <coreicons-shape-circle variant="filled" class="text-base-content/75 size-0.5"
    ></coreicons-shape-circle>
    <span class="text-base-content/75 text-xs font-medium"
      >{new FormatDate(post.created_at).timeAgo()}</span
    >
  </div>
{/snippet}

{#snippet vote_comment_share_more()}
  <div class="bg-neutral rounded-field relative flex items-center gap-1">
    <button
      class="btn btn-primary btn-soft btn-sm btn-square"
      class:btn-active={is_upvoted}
      aria-label="Upvote post"
    >
      <coreicons-shape-thumbs variant="up" class="size-4"></coreicons-shape-thumbs>
    </button>
    <span class="text-xs font-medium md:text-sm">{readable(post.ratio)}</span>
    <button class="btn btn-accent btn-soft btn-sm btn-square" aria-label="Downvote post">
      <coreicons-shape-thumbs variant="down" class="size-4"></coreicons-shape-thumbs>
    </button>
  </div>
  <button class="btn btn-sm btn-neutral relative px-2">
    <coreicons-shape-forum class="size-4"></coreicons-shape-forum>
    <span class="text-xs font-medium md:text-sm">{readable(post.comments?.length ?? 0)}</span>
  </button>
  <button class="btn btn-sm btn-neutral relative hidden md:flex">
    <coreicons-shape-share class="size-4"></coreicons-shape-share>
    <span class="text-sm font-medium">Share</span>
  </button>
  <button class="btn btn-sm btn-ghost hover:btn-neutral btn-square relative" aria-label="more">
    <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
  </button>
{/snippet}

{#snippet href_overlay()}
  <a
    href="/q/{post.community.name}/posts/{post.id}/{post.slug}"
    class="absolute inset-0"
    aria-label={post.title}
  ></a>
{/snippet}

<div
  class={cn(
    layoutTypeStore.state === 'compact' && 'hover:bg-base-200 transition-colors',
    'border-neutral bg-base-300 rounded-box relative flex flex-col overflow-hidden border'
  )}
>
  {#if layoutTypeStore.state === 'card'}
    <div
      class="hover:bg-base-200 group relative flex flex-col gap-1 p-4 transition-colors duration-75"
    >
      {@render href_overlay()}
      {@render avatar_name_date_more()}
      <h2 class="text-info text-lg font-bold md:text-xl">{post.title}</h2>
      {@render content_or_cover()}
      <div class="mt-1.5 flex items-center gap-2.5">
        {@render vote_comment_share_more()}
      </div>
    </div>
  {:else}
    <div class="group flex flex-1 flex-row-reverse gap-4 p-4 p-4 md:flex-row">
      {@render href_overlay()}
      <div
        class={cn(
          post.cover ? 'relative' : 'hidden bg-transparent md:flex',
          'inner-border inner-border-base-content/15 size-20 shrink-0 cursor-pointer rounded-xl bg-cover bg-center bg-no-repeat'
        )}
        style="background-image: url({post.cover});"
      ></div>
      <div class="flex w-full flex-col gap-1">
        {@render avatar_name_date_more()}
        <h2 class="text-info text-base font-bold md:text-lg">{post.title}</h2>
        <div class="mt-auto flex items-center gap-2.5">
          <button
            onclick={() => (is_expanded = !is_expanded)}
            class="btn btn-sm btn-square btn-neutral relative hidden md:flex"
          >
            {#if is_expanded}
              <coreicons-shape-shrink class="text-primary size-4"></coreicons-shape-shrink>
            {:else}
              <coreicons-shape-expand class="size-4"></coreicons-shape-expand>
            {/if}
          </button>
          {@render vote_comment_share_more()}
        </div>
      </div>
    </div>
    {#if is_expanded}
      <div class="p-4 pt-0">
        {@render content_or_cover()}
      </div>
    {/if}
  {/if}
</div>
