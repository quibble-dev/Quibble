<script lang="ts">
  import type { components } from '$lib/clients/v1';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import readable from 'readable-numbers';

  type Props = components['schemas']['Quib'];

  let props: Props = $props();
</script>

<div
  class="relative flex flex-col gap-2 rounded-2xl border border-neutral bg-base-300 p-4 transition-colors hover:bg-base-200"
>
  <a
    href="/q/{props.quiblet.name}/quibs/{props.id}/{props.slug}"
    class="absolute inset-0"
    aria-label={props.title}
  ></a>
  <div class="flex items-center gap-2">
    <a href="/q/{props.quiblet.name}" class="relative flex items-center gap-2">
      <Avatar src={props.quiblet.avatar} alt={props.quiblet.name} />
      <h3 class="text-xs font-bold">q/{props.quiblet.name}</h3>
    </a>
    <coreicons-shape-circle variant="filled" class="size-0.5 text-base-content/75"
    ></coreicons-shape-circle>
    <span class="text-xs font-medium text-base-content/75">{props.created_at}</span>
  </div>

  <h2 class="text-xl font-extrabold text-white">{props.title}</h2>

  <p class="line-clamp-3 text-sm font-normal text-base-content" class:hidden={props.cover}>
    {props.content}
  </p>

  <img class="rounded-xl" src={props.cover} alt="" />

  <div class="relative mt-2 flex gap-4">
    <button class="flex items-center gap-2">
      <coreicons-shape-thumbs variant="up" class="size-4"></coreicons-shape-thumbs>
      <span class="text-sm font-semibold">{readable(props.likes?.length || 0)}</span>
    </button>
    <button class="flex items-center gap-2">
      <coreicons-shape-thumbs variant="down" class="size-4"></coreicons-shape-thumbs>
      <span class="text-sm font-semibold">{readable(props.dislikes?.length || 0)}</span>
    </button>
    <button class="flex items-center gap-2">
      <coreicons-shape-forum class="size-4"></coreicons-shape-forum>
      <span class="text-sm font-semibold">{readable(234)} Quibble(s)</span>
    </button>
    <button class="flex items-center gap-2">
      <coreicons-shape-share class="size-4"></coreicons-shape-share>
      <span class="text-sm font-semibold">Share</span>
    </button>
    <button class="ml-auto flex items-center gap-2" aria-label="more">
      <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
    </button>
  </div>
</div>
