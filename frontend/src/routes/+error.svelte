<script lang="ts">
  import Quibble404 from '$lib/assets/vectors/quibble_404.svg';
  import { page } from '$app/stores';
</script>

<svelte:head>
  <title>Not Found</title>
</svelte:head>

<div class="mt-5 flex flex-1 items-end justify-center gap-5">
  <img src={Quibble404} class="w-28" alt="" />
  <div class="flex flex-col">
    <h4 class="text-xl font-bold text-error">oops!!</h4>
    <h5>{$page.error?.message}</h5>
    <a href="/" aria-label="home" class="btn btn-primary btn-sm mt-4 w-max">
      <coreicons-shape-home class="size-4"></coreicons-shape-home>
      Back to home
    </a>
  </div>
</div>
