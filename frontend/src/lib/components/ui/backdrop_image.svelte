<script lang="ts">
  import { cn } from '$lib/functions/classnames';
  import type { Nullable } from '$lib/types/shared';

  type Props = Partial<{
    src: Nullable<string>;
    class: string;
    img_class: string;
    backdrop_class: string;
  }>;

  let { src, class: klass, img_class, backdrop_class }: Props = $props();
</script>

<div
  class={cn(
    klass,
    'relative flex cursor-pointer justify-center overflow-hidden rounded-2xl inner-border inner-border-base-content/15'
  )}
>
  <!-- blurred img -->
  <div
    class={cn(
      backdrop_class,
      'absolute inset-0 -z-10 scale-150 bg-cover bg-center opacity-50 blur-xl'
    )}
    style="background-image: url({src});"
  ></div>
  <!-- original img -->
  <img {src} alt="" class={cn(img_class, 'object-contain')} />
</div>
