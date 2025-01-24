<script lang="ts">
  import { page } from '$app/state';
  import type { components } from '$lib/clients/v1';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import BackdropImage from '$lib/components/ui/backdrop-image.svelte';
  import Zoom from '$lib/components/ui/zoom.svelte';
  import { cn } from '$lib/functions/classnames';
  import { FormatDate } from '$lib/functions/date';
  import { is_valid } from '$lib/functions/is_valid';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import { createLayoutTypeStore } from '$lib/stores/layout_type.svelte';
  import readable from 'readable-numbers';

  type PostProps = components['schemas']['Post'];

  let post: PostProps = $props();

  const authStore = createAuthStore(),
    layoutTypeStore = createLayoutTypeStore();

  let is_expanded = $state(false);

  const is_upvoted = $derived.by(check_if_upvoted);
  function check_if_upvoted() {
    if (authStore.state.profile && post.upvotes) {
      return post.upvotes.includes(authStore.state.profile.id);
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
  {:else}
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
      class="relative flex items-center gap-2 hover:text-accent hover:underline"
    >
      <Avatar src={get_avatar()} class="size-6 rounded-full" />
      <h3 class="text-xs font-semibold">{get_name()}</h3>
    </a>
    <coreicons-shape-circle variant="filled" class="size-0.5 text-base-content/75"
    ></coreicons-shape-circle>
    <span class="text-xs font-medium text-base-content/75"
      >{new FormatDate(post.created_at).timeAgo()}</span
    >
    <button class="ml-auto hidden items-center gap-2 md:flex" aria-label="more">
      <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
    </button>
  </div>
{/snippet}

{#snippet vote_comment_share_more()}
  <div class="flex items-center gap-2">
    <button class="flex items-center gap-2" aria-label="upvote">
      <coreicons-shape-thumbs variant="up" class="size-4" class:text-primary={is_upvoted}
      ></coreicons-shape-thumbs>
    </button>
    <span class="text-xs font-medium md:text-sm">{readable(post.upvotes?.length ?? 0)}</span>
    <button class="flex items-center gap-2" aria-label="downvote">
      <coreicons-shape-thumbs variant="down" class="size-4"></coreicons-shape-thumbs>
    </button>
  </div>
  <button class="flex items-center gap-2">
    <coreicons-shape-forum class="size-4"></coreicons-shape-forum>
    <span class="text-xs font-medium md:text-sm"
      >{readable(post.comments?.length ?? 0)} comments</span
    >
  </button>
  <button class="hidden items-center gap-2 md:flex">
    <coreicons-shape-share class="size-4"></coreicons-shape-share>
    <span class="text-sm font-medium">Share</span>
  </button>
  <button class="flex items-center gap-2 md:hidden" aria-label="more">
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
    layoutTypeStore.state === 'compact' && 'transition-colors hover:bg-base-200',
    'relative flex flex-col overflow-hidden rounded-2xl border border-neutral bg-base-300'
  )}
>
  {#if layoutTypeStore.state === 'card'}
    <div class="relative flex flex-col gap-2 p-4 transition-colors hover:bg-base-200">
      {@render href_overlay()}
      {@render avatar_name_date_more()}
      <h2 class="text-lg font-bold text-info md:text-xl">{post.title}</h2>
      {@render content_or_cover()}
    </div>
    <div class="flex items-center gap-4 border-t border-neutral px-4 py-2.5">
      {@render vote_comment_share_more()}
    </div>
  {:else}
    <div class="flex flex-1 flex-row-reverse gap-4 p-4 p-4 md:flex-row">
      {@render href_overlay()}
      <div
        class={cn(
          post.cover ? 'relative' : 'hidden bg-transparent md:flex',
          'size-20 flex-shrink-0 cursor-pointer rounded-xl bg-cover bg-center bg-no-repeat inner-border inner-border-base-content/15'
        )}
        style="background-image: url({post.cover});"
      ></div>
      <div class="flex w-full flex-col gap-1">
        {@render avatar_name_date_more()}
        <h2 class="text-base font-bold text-info md:text-lg">{post.title}</h2>
        <div class="mt-auto flex items-center gap-4">
          <button
            onclick={() => (is_expanded = !is_expanded)}
            class="relative flex hidden items-center gap-2 md:flex"
          >
            {#if is_expanded}
              <coreicons-shape-shrink class="size-4 text-primary"></coreicons-shape-shrink>
              <span class="text-sm font-medium">Shrink</span>
            {:else}
              <coreicons-shape-expand class="size-4"></coreicons-shape-expand>
              <span class="text-sm font-medium">Expand</span>
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
