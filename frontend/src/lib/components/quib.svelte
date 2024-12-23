<script lang="ts">
  import type { components } from '$lib/clients/v1';
  import Image from '$lib/components/ui/image.svelte';
  import readable from 'readable-numbers';
  import { FormatDate } from '$lib/functions/date';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import { page } from '$app/stores';

  type QuibProps = components['schemas']['Quib'];

  let quib: QuibProps = $props();

  const authStore = createAuthStore();

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

<div class="flex flex-col overflow-hidden rounded-2xl border border-neutral bg-base-300">
  <div
    class="relative flex flex-col gap-2 bg-base-300 p-4 transition-colors hover:bg-base-200"
  >
    <a
      href="/q/{quib.quiblet.name}/quibs/{quib.id}/{quib.slug}"
      class="absolute inset-0"
      aria-label={quib.title}
    ></a>
    <div class="flex items-center gap-2">
      <a
        href="/{get_name()}"
        class="relative flex items-center gap-2 hover:text-accent hover:underline"
      >
        <Image src={get_avatar()} class="size-6 rounded-full" />
        <h3 class="text-xs font-semibold">{get_name()}</h3>
      </a>
      <coreicons-shape-circle variant="filled" class="size-0.5 text-base-content/75"
      ></coreicons-shape-circle>
      <span class="text-xs font-medium text-base-content/75"
        >{new FormatDate(quib.created_at).timeAgo()}</span
      >
    </div>

    <h2 class="text-xl font-bold text-info">{quib.title}</h2>

    {#if quib.content?.trim()}
      <p class="line-clamp-3 text-sm font-normal" class:hidden={quib.cover}>
        {quib.content}
      </p>
    {:else}
      <img
        class="rounded-2xl inner-border inner-border-base-content/15"
        src={quib.cover}
        alt=""
      />
    {/if}
  </div>

  <div class="flex items-center gap-4 border-t border-neutral px-4 py-2.5">
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
      <span class="text-sm font-medium"
        >{readable(quib.comments?.length ?? 0)} comments</span
      >
    </button>
    <button class="flex items-center gap-2">
      <coreicons-shape-share class="size-4"></coreicons-shape-share>
      <span class="text-sm font-medium">Share</span>
    </button>
    <button class="ml-auto flex items-center gap-2" aria-label="more">
      <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
    </button>
  </div>
</div>
