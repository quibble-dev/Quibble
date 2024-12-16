<script lang="ts">
  import type { PageData } from './$types';

  const { data }: { data: PageData } = $props();
</script>

<svelte:head>
  <title>q/{data.quiblet?.name}</title>
</svelte:head>

<div
  class="h-40 w-full rounded-2xl bg-cover bg-center"
  style="background-image: url({data.quiblet?.banner});"
></div>
