<script lang="ts">
  import { page } from '$app/state';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { cn } from '$lib/functions/classnames';
  import type { LayoutData } from './$types';
  import type { Snippet } from 'svelte';

  const types = {
    '': {
      label: 'Overview',
      disabled: false
    },
    posts: {
      label: 'Posts',
      disabled: false
    },
    comments: {
      label: 'Comments',
      disabled: false
    },
    upvoted: {
      label: 'Upvoted',
      disabled: false
    },
    downvoted: {
      label: 'Downvoted',
      disabled: false
    }
  };

  const { data, children }: { data: LayoutData; children: Snippet } = $props();
  const { profile } = $derived(data);
  const base_path = $derived(`/u/${profile?.username}`);

  function check_is_active(key: string) {
    if (key === '') return page.url.pathname === base_path;
    return page.url.pathname === `${base_path}/${key}`;
  }
</script>

<svelte:head>
  <title>{`${profile?.name ?? profile?.username} (u/${profile?.username})`.trim()} - Quibble</title>
</svelte:head>

<div class="flex h-max flex-1 flex-col gap-4 p-4">
  <div class="flex items-center gap-4">
    <Avatar src={profile?.avatar} class="size-20" />
    <div class="flex flex-col">
      <h2 class="text-info text-xl font-medium">{profile?.name ?? profile?.username}</h2>
      <span class="text-sm">u/{profile?.username}</span>
    </div>
  </div>
  <div class="flex items-center gap-2">
    {#each Object.entries(types) as [key, item]}
      {@const active = check_is_active(key)}

      <div class="relative flex flex-col items-center">
        <a
          href={`${base_path}/${key}`}
          class={cn(active && 'btn-neutral btn-active', 'btn btn-ghost h-max p-2.5')}
          >{item.label}</a
        >
        {#if active}
          <div class="bg-primary absolute -bottom-1.5 h-0.5 w-2/3"></div>
        {/if}
      </div>
    {/each}
  </div>
  <div class="flex flex-col gap-2">
    {@render children()}
  </div>
</div>
<div class="hidden w-80 lg:flex">
  <div
    class="scrollbar-none fixed top-[3.75rem] flex h-[calc(100dvh-3.75rem)] w-80 flex-col gap-4 overflow-y-scroll p-4"
  ></div>
</div>
