<script lang="ts">
  import { page } from '$app/stores';
  import type { components } from '$lib/clients/v1';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import BackdropImage from '$lib/components/ui/backdrop_image.svelte';
  import Zoom from '$lib/components/ui/zoom.svelte';
  import { cn } from '$lib/functions/classnames';
  import { FormatDate } from '$lib/functions/date';
  import { is_valid } from '$lib/functions/is_valid';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import { createViewStore } from '$lib/stores/view.svelte';
  import readable from 'readable-numbers';

  type QuibProps = components['schemas']['Quib'];

  let quib: QuibProps = $props();

  const authStore = createAuthStore(),
    viewStore = createViewStore();

  let is_expanded = $state(false);

  const is_upvoted = $derived.by(check_if_upvoted);
  function check_if_upvoted() {
    if (authStore.state.profile && quib.upvotes) {
      return quib.upvotes.includes(authStore.state.profile.id);
    } else {
      return false;
    }
  }

  function get_avatar() {
    return $page.url.pathname.includes('/q/') ? quib.quibber.avatar : quib.quiblet.avatar;
  }

  function get_name() {
    return $page.url.pathname.includes('/q/')
      ? `u/${quib.quibber.username}`
      : `q/${quib.quiblet.name}`;
  }
</script>

{#snippet content_or_cover()}
  {#if is_valid(quib.content)}
    <p class="text-sm font-normal">
      {quib.content}
    </p>
  {:else}
    <BackdropImage src={quib.cover} class="z-10">
      <Zoom>
        <img src={quib.cover} alt="" class="max-h-[25rem] object-contain" />
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
      >{new FormatDate(quib.created_at).timeAgo()}</span
    >
    <button class="ml-auto flex items-center gap-2" aria-label="more">
      <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
    </button>
  </div>
{/snippet}

{#snippet vote_comment_share()}
  <div class="flex items-center gap-2">
    <button class="flex items-center gap-2" aria-label="upvote">
      <coreicons-shape-thumbs variant="up" class="size-4" class:text-primary={is_upvoted}
      ></coreicons-shape-thumbs>
    </button>
    <span class="text-sm font-medium">{readable(quib.upvotes?.length ?? 0)}</span>
    <button class="flex items-center gap-2" aria-label="downvote">
      <coreicons-shape-thumbs variant="down" class="size-4"></coreicons-shape-thumbs>
    </button>
  </div>
  <button class="flex items-center gap-2">
    <coreicons-shape-forum class="size-4"></coreicons-shape-forum>
    <span class="text-sm font-medium">{readable(quib.comments?.length ?? 0)} comments</span>
  </button>
  <button class="flex items-center gap-2">
    <coreicons-shape-share class="size-4"></coreicons-shape-share>
    <span class="text-sm font-medium">Share</span>
  </button>
{/snippet}

{#snippet href_overlay()}
  <a
    href="/q/{quib.quiblet.name}/quibs/{quib.id}/{quib.slug}"
    class="absolute inset-0"
    aria-label={quib.title}
  ></a>
{/snippet}

<div
  class={cn(
    viewStore.state === 'compact' && 'transition-colors hover:bg-base-200',
    'relative flex flex-col overflow-hidden border-neutral bg-base-300 md:rounded-2xl md:border'
  )}
>
  {#if viewStore.state === 'card'}
    <div class="relative flex flex-col gap-2 p-4 transition-colors hover:bg-base-200">
      {@render href_overlay()}
      {@render avatar_name_date_more()}
      <h2 class="text-xl font-bold text-info">{quib.title}</h2>
      {@render content_or_cover()}
    </div>
    <div
      class="flex items-center gap-4 border-neutral px-4 pb-2.5 pt-0 md:border-t md:pt-2.5"
    >
      {@render vote_comment_share()}
    </div>
  {:else}
    <div class="flex flex-1 gap-4 p-4 p-4">
      {@render href_overlay()}
      <div
        class="size-20 flex-shrink-0 cursor-pointer rounded-xl bg-cover bg-center bg-no-repeat
            inner-border inner-border-base-content/15"
        class:relative={quib.cover}
        class:bg-base-100={!quib.cover}
        style="background-image: url({quib.cover});"
      ></div>
      <div class="flex w-full flex-col gap-1">
        {@render avatar_name_date_more()}
        <h2 class="text-lg font-bold text-info">{quib.title}</h2>
        <div class="mt-auto flex items-center gap-4">
          <button
            onclick={() => (is_expanded = !is_expanded)}
            class="relative flex items-center gap-2"
          >
            {#if is_expanded}
              <coreicons-shape-shrink class="size-4 text-primary"></coreicons-shape-shrink>
              <span class="text-sm font-medium">Shrink</span>
            {:else}
              <coreicons-shape-expand class="size-4"></coreicons-shape-expand>
              <span class="text-sm font-medium">Expand</span>
            {/if}
          </button>
          {@render vote_comment_share()}
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
