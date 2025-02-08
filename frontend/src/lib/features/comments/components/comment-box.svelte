<script lang="ts">
  import autosize from '$lib/actions/autosize';
  import { onMount } from 'svelte';

  type Props = {
    oncancel: () => void;
    oncomment: (value: string) => void;
  };

  let { oncancel, oncomment }: Props = $props();
  let textarea_el = $state<HTMLTextAreaElement>();

  onMount(() => {
    textarea_el?.focus();
  });
</script>

<div class="flex flex-col rounded-2xl border border-base-content/25">
  <textarea
    use:autosize
    class="max-h-40 min-h-10 bg-transparent p-2.5 text-sm leading-normal outline-none
    placeholder:text-base-content/75"
    placeholder="Add a comment..."
    bind:this={textarea_el}
  ></textarea>
  <div class="flex w-full items-center gap-2 p-2">
    <button class="btn btn-ghost btn-sm ml-auto" onclick={oncancel}>Cancel</button>
    <button class="btn btn-primary btn-sm" onclick={() => oncomment(String(textarea_el?.value))}>
      Comment
      <coreicons-shape-message-circle class="size-4"></coreicons-shape-message-circle>
    </button>
  </div>
</div>
