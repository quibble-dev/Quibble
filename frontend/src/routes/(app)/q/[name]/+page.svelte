<script lang="ts">
  import Quib from '$lib/components/pages/home/quib.svelte';
  import QuibsHeader from '$lib/components/pages/home/quibs_header.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { cn } from '$lib/functions/classnames';
  import type { PageData } from './$types';

  const { data }: { data: PageData } = $props();
  const { quiblet, quibs } = data;
</script>

<svelte:head>
  <title>q/{quiblet?.name}</title>
</svelte:head>

<div class="relative">
  <div
    class={cn(
      !quiblet?.banner ? 'h-24 bg-neutral' : 'h-40 bg-cover bg-center',
      'w-full rounded-2xl'
    )}
    style="background-image: url({quiblet?.banner});"
  ></div>
  <div class="absolute inset-x-0 -bottom-12 flex items-end justify-between px-4">
    <div class="flex items-end gap-2">
      <Avatar class="!size-20 outline outline-8 outline-base-300" src={quiblet?.avatar} />
      <h3 class="text-2xl font-bold text-info">q/{quiblet?.name}</h3>
    </div>
    <div class="flex items-center gap-2">
      <button class="btn btn-primary h-10 px-3" aria-label="Create a Post">
        <coreicons-shape-plus variant="no-border" class="size-5"></coreicons-shape-plus>
        <span class="text-sm font-medium">Create Quib</span>
      </button>
      <button class="btn btn-secondary h-10 px-3" aria-label="Join quiblet">
        <span class="text-sm font-medium">Join</span>
      </button>
      <button class="btn btn-neutral size-10 p-0" aria-label="More options">
        <coreicons-shape-more class="size-5 rotate-90"></coreicons-shape-more>
      </button>
    </div>
  </div>
</div>
<div class="h-12"></div>
<QuibsHeader />
{#if quibs}
  {#each quibs as quib}
    <Quib {...quib} />
  {/each}
{/if}
