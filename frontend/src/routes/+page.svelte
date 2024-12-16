<script lang="ts">
  import Quib from '$lib/components/pages/home/quib.svelte';
  import QuibsHeader from '$lib/components/pages/home/quibs_header.svelte';
  import RecentQuibs from '$lib/components/pages/home/recent_quibs.svelte';
  import type { PageData } from './$types';

  const { data }: { data: PageData } = $props();
</script>

<svelte:head>
  <title>Quibble - Delve into real conversations.</title>
</svelte:head>

<div class="flex h-max flex-1 flex-col gap-4 p-4">
  <QuibsHeader />
  <div class="flex flex-1 flex-col gap-4">
    {#if data.quibs}
      {#each data.quibs as quib}
        <Quib {...quib} />
      {/each}
    {/if}
  </div>
</div>
<div class="w-80">
  <div
    class="fixed top-[3.75rem] flex h-[calc(100dvh-3.75rem)] w-72 flex-col gap-4 overflow-y-scroll p-4 scrollbar-none"
  >
    <RecentQuibs />
  </div>
</div>
