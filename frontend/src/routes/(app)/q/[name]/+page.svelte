<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { cn } from '$lib/functions/classnames';
  import type { PageData } from './$types';

  const { data }: { data: PageData } = $props();
  const { quiblet } = data;
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
  <div class="absolute inset-x-0 -bottom-10 flex items-end px-4">
    <div class="flex items-end">
      <Avatar class="!size-20 outline outline-8 outline-base-300" src={quiblet?.avatar} />
      <h3>q/{quiblet?.name}</h3>
    </div>
  </div>
</div>
