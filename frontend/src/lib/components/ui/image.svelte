<script lang="ts">
  import { cn } from '$lib/functions/classnames';

  type Props = {
    src?: string | null;
    class?: string;
  };

  let { src, class: klass }: Props = $props();

  let valid_src = $state(false);

  const object_classes: string[] = [];
  const _klass = klass
    ?.split(/\s+/)
    .filter((cls) => {
      if (cls.startsWith('object-')) {
        object_classes.push(cls);
        return false;
      }
      return true;
    })
    .join(' ');

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

<div class={cn(_klass, 'grid place-items-center overflow-hidden bg-neutral')}>
  {#if valid_src}
    <img {src} alt="" class={cn('h-full w-full', ...object_classes)} />
  {:else}
    <svg
      class="w-1/2 max-w-10 text-neutral-content"
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
