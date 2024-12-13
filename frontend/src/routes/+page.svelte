<script lang="ts">
  import Quib from '$lib/components/pages/home/quib.svelte';
  import QuibsHeader from '$lib/components/pages/home/quibs_header.svelte';
  import RecentQuibs from '$lib/components/pages/home/recent_quibs.svelte';
  import posts from '$lib/data/mock/posts.json';
</script>

<svelte:head>
  <title>Quibble - Delve into real conversations.</title>
</svelte:head>

<div class="mx-auto flex flex-1 xl:max-w-5xl">
  <div class="flex h-max flex-1 flex-col gap-4 p-4">
    <QuibsHeader />
    <div class="flex flex-1 flex-col gap-4">
      {#each posts as post}
        <!-- <Quib {...post} /> -->
      {/each}
    </div>
  </div>
  <div class="w-80">
    <RecentQuibs />
  </div>
</div>
