<script lang="ts">
  import type { Snippet } from 'svelte';
  import type { PageData } from './$types';
  import { FormatDate } from '$lib/functions/date';
  import { pluralize } from '$lib/functions/pluralize';
  import Image from '$lib/components/ui/image.svelte';

  const { data, children }: { data: PageData; children: Snippet } = $props();
  const { quiblet } = data;
</script>

<div class="flex h-max flex-1 flex-col gap-4 p-4">
  {@render children()}
</div>
<div class="w-80">
  <div
    class="fixed top-[3.75rem] flex h-[calc(100dvh-3.75rem)] w-80 flex-col gap-4 overflow-y-scroll p-4 scrollbar-none"
  >
    <div class="flex flex-col gap-2">
      <h3 class="font-medium">{quiblet?.title ?? `q/${quiblet?.name}`}</h3>
      <p class="text-sm text-base-content/75">{quiblet?.description}</p>
      <div class="flex items-center gap-2 text-xs">
        <coreicons-shape-gift class="size-4"></coreicons-shape-gift>
        Created {new FormatDate(quiblet?.created_at ?? '').format()}
      </div>
      <div class="flex items-center gap-2 text-xs">
        <coreicons-shape-globe class="size-4"></coreicons-shape-globe>
        {quiblet?.is_public ? 'Public' : 'Private'}
      </div>
    </div>
    <div class="flex items-center gap-4">
      <div class="flex flex-col">
        <span class="text-sm text-info">{quiblet?.members?.length}</span>
        <span class="text-xs text-base-content/75"
          >{pluralize('Member', quiblet?.members?.length ?? 0)}</span
        >
      </div>
      <div class="flex flex-col">
        <span class="text-sm text-info">{quiblet?.quibs}</span>
        <span class="text-xs text-base-content/75"
          >{pluralize('Quib', quiblet?.quibs ?? 0)}</span
        >
      </div>
    </div>
    <div class="divider my-0 before:h-px after:h-px"></div>
    <div class="flex items-center gap-2">
      <h3 class="text-sm font-medium">Rangers</h3>
      <div class="tooltip tooltip-right flex" data-tip="Moderators">
        <coreicons-shape-help-circle class="size-[0.85rem]"></coreicons-shape-help-circle>
      </div>
    </div>
    {#if quiblet?.rangers}
      <div class="flex flex-col gap-2">
        {#each quiblet?.rangers as ranger}
          <div class="flex items-center gap-2">
            <Image src={ranger.avatar} class="size-6 rounded-full" />
            <div class="flex flex-col">
              <a href="/u/{ranger.username}" class="text-sm font-medium"
                >u/{ranger.username}</a
              >
              <span class="text-xs text-base-content/75">{ranger.name}</span>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</div>
