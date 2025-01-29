<script lang="ts">
  import { page } from '$app/state';
  import Quibble404 from '$lib/components/vectors/quibble-404.svelte';
</script>

<!-- site head and seo -->
<svelte:head>
  <title>Not Found</title>
</svelte:head>

<div class="mt-5 flex flex-1 items-end justify-center gap-5">
  <!-- left column: icon -->
  <Quibble404 class="h-auto w-28" />

  <!-- right column: error message and anchor -->
  <div class="flex flex-col">
    <h4 class="text-xl font-bold text-error">oops!!</h4>
    <h5>{page.error?.message}</h5>
    <a href="/" aria-label="home" class="btn btn-primary btn-sm mt-4 w-max">
      <coreicons-shape-home class="size-4"></coreicons-shape-home>
      Back to home
    </a>
  </div>
</div>
