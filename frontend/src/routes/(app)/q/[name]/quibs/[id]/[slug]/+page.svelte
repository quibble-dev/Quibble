<script lang="ts">
  import { browser } from '$app/environment';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { FormatDate } from '$lib/functions/date';
  import { is_valid } from '$lib/functions/is_valid';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import type { PageData } from './$types';
  import readable from 'readable-numbers';

  const { data }: { data: PageData } = $props();
  const { quib, comments } = data;

  const authStore = createAuthStore();

  const is_upvoted = $derived.by(check_if_upvoted);
  function check_if_upvoted() {
    if (authStore.state.profile && quib.upvotes) {
      return quib.upvotes.includes(authStore.state.profile.id);
    } else {
      return false;
    }
  }

  function handle_back() {
    if (browser) window.history.back();
  }
</script>

<svelte:head>
  <title>{quib.title} : q/{quib.quiblet.name}</title>
</svelte:head>

<!-- quibber and quiblet details -->
<div class="flex items-center gap-2">
  <button
    onclick={handle_back}
    class="btn btn-neutral size-8 rounded-full p-0"
    aria-label="back"
  >
    <coreicons-shape-arrow variant="left" class="size-5"></coreicons-shape-arrow>
  </button>
  <div class="flex items-center gap-2">
    <a href="/q/{quib.quiblet.name}">
      <Avatar src={quib.quiblet.avatar} class="size-8 rounded-full" />
    </a>
    <div class="flex flex-col">
      <div class="flex items-center gap-2">
        <a href="/q/{quib.quiblet.name}" class="hover:text-accent hover:underline">
          <h3 class="text-xs font-semibold">q/{quib.quiblet.name}</h3>
        </a>
        <coreicons-shape-circle variant="filled" class="size-0.5 text-base-content/75"
        ></coreicons-shape-circle>
        <span class="text-xs font-medium text-base-content/75"
          >{new FormatDate(quib.created_at).timeAgo()}</span
        >
      </div>
      <a href="/u/{quib.quibber.username}" class="w-max hover:underline">
        <h3 class="text-xs">{quib.quibber.username}</h3>
      </a>
    </div>
  </div>
</div>
<!-- title -->
<h2 class="text-2xl font-bold text-info">{quib.title}</h2>
<!-- content or cover -->
{#if is_valid(quib.content)}
  <p class="text-sm font-normal">
    {quib.content}
  </p>
{:else}
  <div
    class="relative flex max-h-[25rem] cursor-pointer justify-center overflow-hidden rounded-2xl bg-cover bg-center inner-border inner-border-base-content/15"
  >
    <img src={quib.cover} alt="" />
  </div>
{/if}
<!-- quib options like vote share and more -->
<div class="flex items-center gap-4">
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
  <button class="ml-auto flex items-center gap-2" aria-label="more">
    <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
  </button>
</div>
<!-- add comment dynamic box -->
<button class="flex items-center gap-2 rounded-2xl border border-neutral p-2.5 text-sm">
  <coreicons-shape-message-circle class="size-5"></coreicons-shape-message-circle>
  Add a comment...
</button>
<!-- render comments -->
{#if comments}
  {#each comments as comment}
    {comment.path}
    {comment.content}
  {/each}
{/if}
