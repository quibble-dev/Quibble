<script lang="ts">
  import Quibble404 from '$lib/assets/svgs/quibble_404.svg';
  import { page } from '$app/stores';
</script>

<div class="mt-5 flex flex-1 items-end justify-center gap-5">
  <img src={Quibble404} class="w-28" alt="" />
  <div class="flex flex-col">
    <h4 class="text-xl font-bold text-error">oh noh!!</h4>
    <h5 class="text-error">{$page.error?.message}</h5>
    <a href="/" aria-label="home" class="btn btn-primary btn-sm mt-4 w-max">
      <coreicons-shape-home class="size-4"></coreicons-shape-home>
      Back to home
    </a>
  </div>
</div>
