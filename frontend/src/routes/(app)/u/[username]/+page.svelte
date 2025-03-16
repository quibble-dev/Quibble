<script lang="ts">
  import type { PageData } from './$types';

  const { data }: { data: PageData } = $props();
  const { profile } = $derived(data);
</script>

<svelte:head>
  <title>{profile?.first_name} (u/{profile?.username})</title>
</svelte:head>

<div class="flex h-max flex-1 flex-col gap-4 p-4">{profile?.username}</div>
<div class="hidden w-80 lg:flex">
  <div
    class="scrollbar-none fixed top-[3.75rem] flex h-[calc(100dvh-3.75rem)] w-80 flex-col gap-4 overflow-y-scroll p-4"
  ></div>
</div>
