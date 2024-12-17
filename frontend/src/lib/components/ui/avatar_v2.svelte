<script lang="ts">
  import { cn } from '$lib/functions/classnames';
  import QuibbleEye from '$lib/components/vectors/quibble_eye.svelte';

  type Props = {
    src?: string | null;
    class?: string;
  };

  let { src, class: klass }: Props = $props();
</script>

<div
  class={cn(
    klass,
    'grid size-6 place-items-center overflow-hidden rounded-full bg-neutral'
  )}
>
  {#if src}
    <img {src} alt="" />
  {:else}
    <QuibbleEye class="w-1/2 text-neutral-content" />
  {/if}
</div>
