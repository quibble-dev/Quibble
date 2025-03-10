<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { FormatDate } from '$lib/functions/date';
  import { pluralize } from '$lib/functions/pluralize';
  import type { PageData } from './$types';
  import type { Snippet } from 'svelte';

  const { data, children }: { data: PageData; children: Snippet } = $props();
  const { community } = $derived(data);
</script>

<div class="flex h-max flex-1 flex-col gap-4 p-4">
  {@render children()}
</div>
<!-- fixed sidebar about community details -->
<div class="hidden w-80 lg:flex">
  <div
    class="fixed top-[3.75rem] flex h-[calc(100dvh-3.75rem)] w-80 flex-col gap-4 overflow-y-scroll p-4 scrollbar-none"
  >
    <!-- basic details -->
    <div class="flex flex-col gap-2">
      <h3 class="font-medium">{community?.title ?? `q/${community?.name}`}</h3>
      <p class="text-sm text-base-content/75">{community?.description}</p>
      <div class="flex items-center gap-2 text-xs">
        <coreicons-shape-gift class="size-4"></coreicons-shape-gift>
        Created {new FormatDate(community?.created_at ?? '').format()}
      </div>
      <div class="flex items-center gap-2 text-xs">
        <coreicons-shape-globe class="size-4"></coreicons-shape-globe>
        {community.type}
      </div>
    </div>
    <div class="flex items-center gap-4">
      <div class="flex flex-col">
        <span class="text-sm text-info">{community?.members?.length}</span>
        <span class="text-xs text-base-content/75"
          >{pluralize('Member', community?.members?.length ?? 0)}</span
        >
      </div>
      <div class="flex flex-col">
        <span class="text-sm text-info">{community?.posts_count}</span>
        <span class="text-xs text-base-content/75"
          >{pluralize('Quib', community?.posts_count ?? 0)}</span
        >
      </div>
    </div>
    <div class="divider my-0 h-max before:h-px after:h-px"></div>

    <!-- moderators section: title -->
    <h3 class="text-sm font-medium">Moderators</h3>
    <!-- moderators list -->
    {#if community?.moderators}
      <div class="flex flex-col gap-2">
        {#each community?.moderators as moderator}
          <div class="flex items-center gap-2">
            <Avatar src={moderator.avatar} class="size-6 rounded-full" />
            <div class="flex flex-col">
              <a href="/u/{moderator.username}" class="text-sm font-medium"
                >u/{moderator.username}</a
              >
              <span class="text-xs text-base-content/75">{moderator.name}</span>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</div>
