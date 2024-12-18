<script lang="ts">
  import { cn } from '$lib/functions/classnames';

  type Props = {
    src?: string | null;
    class?: string;
  };

  let { src, class: klass }: Props = $props();

  let valid_src = $state(false);

  $effect.pre(() => {
    if (!src) {
      valid_src = false;
      return;
    }
    // create img instance
    const img = new Image();
    img.onload = () => (valid_src = true);
    img.onerror = () => (valid_src = false);
    img.src = src;
  });
</script>

<div
  class={cn(
    klass,
    'grid size-6 place-items-center overflow-hidden rounded-full bg-neutral'
  )}
>
  {#if valid_src}
    <img {src} alt="" />
  {:else}
    <svg
      class="w-1/2 text-neutral-content"
      viewBox="0 0 157 86"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M143.6 13L113.366 43L143.6 73M13 13L43.2344 43L13 73"
        stroke="currentColor"
        stroke-width="25"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
  {/if}
</div>
