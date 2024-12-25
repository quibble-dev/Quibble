<script lang="ts">
  import { browser } from '$app/environment';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { FormatDate } from '$lib/functions/date';
  import { is_valid } from '$lib/functions/is_valid';
  import type { PageData } from './$types';

  const { data }: { data: PageData } = $props();
  const { quib } = data;

  function handle_back() {
    if (browser) window.history.back();
  }
</script>

<svelte:head>
  <title>{quib.title} : q/{quib.quiblet.name}</title>
</svelte:head>

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
<h2 class="text-2xl font-bold text-info">{quib.title}</h2>
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
