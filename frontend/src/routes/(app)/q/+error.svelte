<script lang="ts">
  import { page } from '$app/state';
  import Quibble404 from '$lib/assets/vectors/quibble_404.svg';
</script>

<svelte:head>
  <title>Community not found</title>
</svelte:head>

<div class="mt-5 flex flex-1 items-end justify-center gap-5">
  <img src={Quibble404} class="w-28" alt="" />
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
