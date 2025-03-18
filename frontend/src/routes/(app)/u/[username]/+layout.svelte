<script lang="ts">
  import { page } from '$app/state';
  import LegalLinks from '$lib/components/legal-links.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { cn } from '$lib/functions/classnames';
  import { FormatDate } from '$lib/functions/date';
  import type { LayoutData } from './$types';
  import type { Snippet } from 'svelte';

  const types = {
    '': {
      label: 'Overview',
      disabled: false,
      class: 'flex'
    },
    posts: {
      label: 'Posts',
      disabled: false,
      class: 'flex'
    },
    comments: {
      label: 'Comments',
      disabled: false,
      class: 'flex'
    },
    saved: {
      label: 'Saved',
      disabled: true,
      class: 'hidden sm:flex'
    },
    upvoted: {
      label: 'Upvoted',
      disabled: true,
      class: 'hidden sm:flex md:hidden xl:flex'
    },
    downvoted: {
      label: 'Downvoted',
      disabled: true,
      class: 'hidden sm:flex md:hidden xl:flex'
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
  <div class="flex flex-wrap items-center gap-2">
    {#each Object.entries(types) as [key, item]}
      {@const active = check_is_active(key)}

      <div class={cn(item.class, 'relative flex-col items-center')}>
        <a
          href={`${base_path}/${key}`}
          class={cn(
            active && 'btn-active',
            item.disabled && 'btn-disabled pointer-events-none',
            'btn btn-ghost h-max p-2.5'
          )}>{item.label}</a
        >
        {#if active}
          <div class="bg-primary absolute -bottom-1.5 h-0.5 w-2/3"></div>
        {/if}
      </div>
    {/each}
  </div>
  <div class="flex flex-col gap-4">
    {@render children()}
  </div>
</div>
<div class="hidden w-80 lg:flex">
  <div
    class="scrollbar-none fixed top-[3.75rem] flex h-[calc(100dvh-3.75rem)] w-80 flex-col gap-2 overflow-y-scroll p-4"
  >
    <div
      class="bg-neutral rounded-box h-20 bg-cover bg-center bg-no-repeat"
      style="background-image: url({profile?.banner});"
    ></div>
    <h3 class="font-medium">{profile?.name ?? `u/${profile?.username}`}</h3>
    <p class="text-base-content/75 text-sm">{profile?.bio}</p>
    <div class="flex items-center gap-2 text-xs">
      <coreicons-shape-gift class="size-4"></coreicons-shape-gift>
      Cake day, {new FormatDate(profile?.created_at ?? '').format()}
    </div>
    <div class="divider my-0 before:h-px after:h-px"></div>
    <LegalLinks />
  </div>
</div>
