<script lang="ts">
  import type { PageData } from './$types';

  const { data }: { data: PageData } = $props();
</script>

<svelte:head>
  <title>q/{data.quiblet?.name}</title>
</svelte:head>

Hey quiblet page here!
{data.quiblet?.name}
