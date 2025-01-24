<script lang="ts">
  import { page } from '$app/state';
  import Quibble_404 from '$lib/icons/vectors/quibble_404.svelte';
</script>

<svelte:head>
  <title>Community not found</title>
</svelte:head>

<div class="mt-5 flex flex-1 items-end justify-center gap-5">
  <Quibble_404 class="h-auto w-28" />
  <div class="flex flex-col">
    <h4 class="text-xl font-bold text-error">oh noh!!</h4>
    <!-- eslint-disable svelte/no-at-html-tags -->
    <h5>{@html page.error?.message}</h5>
    <!-- eslint-enable svelte/no-at-html-tags -->
    <a href="/" aria-label="home" class="btn btn-primary btn-sm mt-4 w-max">
      <coreicons-shape-home class="size-4"></coreicons-shape-home>
      Back to home
    </a>
  </div>
</div>
