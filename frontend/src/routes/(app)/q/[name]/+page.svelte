<script lang="ts">
  import type { PageData } from './$types';

  const { data }: { data: PageData } = $props();
</script>

Hey quiblet page here!
{data.quiblet?.name}
