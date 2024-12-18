<script lang="ts">
  import Quib from '$lib/components/pages/home/quib.svelte';
  import QuibsHeader from '$lib/components/pages/home/quibs_header.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { cn } from '$lib/functions/classnames';
  import type { PageData } from './$types';

  const { data }: { data: PageData } = $props();
  const { quiblet, quibs, highlighted_quibs } = data;
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
{#if highlighted_quibs}
  <div class="flex flex-col gap-4">
    <div class="flex items-center gap-2">
      <coreicons-shape-hash class="size-5"></coreicons-shape-hash>
      <h4 class="text-sm font-medium">Highlights</h4>
    </div>
    <div class="grid grid-cols-3">
      {#each highlighted_quibs as quib}
        <div
          class="relative h-40 w-full rounded-2xl bg-cover bg-center outline outline-1 outline-offset-[-1px] outline-base-content/50"
          class:bg-neutral={!quib.cover}
          style="background-image: url({quib.cover});"
        >
          <div
            class="absolute inset-0 bg-gradient-to-t from-base-300/75 to-base-300/25"
          ></div>
          <span class="absolute inset-x-0 bottom-0 p-4 font-medium text-info"
            >{quib.title}</span
          >
          <a
            href="./{quiblet?.name}/quibs/{quib.id}/{quib.slug}"
            class="absolute inset-0"
            aria-label={quib.title}
          ></a>
        </div>
      {/each}
    </div>
  </div>
{/if}
{#if quibs}
  {#each quibs as quib}
    <Quib {...quib} />
  {/each}
{/if}
