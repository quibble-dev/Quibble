<script lang="ts">
  import autosize from '$lib/actions/autosize';
  import Avatar from '$lib/components/ui/avatar.svelte';

  type Type = keyof typeof types;
  let active_type = $state<Type>('text');

  const types = {
    text: {
      label: 'Text',
      onclick: () => null,
      disabled: false
    },
    images_and_video: {
      label: 'Images & Video',
      onclick: () => null,
      disabled: true
    },
    link: {
      label: 'Link',
      onclick: () => null,
      disabled: true
    },
    poll: {
      label: 'Poll',
      onclick: () => null,
      disabled: true
    }
  };
</script>

<svelte:head>
  <title>Submit to Quibble</title>
</svelte:head>

<div class="flex h-max flex-1 flex-col gap-4 p-4">
  <!-- section title -->
  <h2 class="text-xl font-semibold text-info">Create Post</h2>
  <!-- select community dropdown and select -->
  <div>
    <div class="btn btn-neutral h-max p-1 hover:btn-ghost">
      <Avatar />
      <span class="text-info">Select a community</span>
      <coreicons-shape-chevron variant="down" class="size-4"></coreicons-shape-chevron>
    </div>
  </div>
  <!-- select post type section -->
  <div class="flex items-center gap-2">
    {#each Object.entries(types) as [key, value]}
      {@const active = active_type === key}

      <div class="relative flex flex-col items-center">
        <button
          class="btn btn-ghost h-max p-2.5"
          onclick={() => (active_type = key as Type)}
          disabled={value.disabled}>{value.label}</button
        >
        {#if active}
          <div class="absolute -bottom-1.5 h-0.5 w-2/3 bg-primary"></div>
        {/if}
      </div>
    {/each}
  </div>
  <!-- post form -->
  <form class="flex flex-col gap-2">
    <label class="form-control w-full">
      <input
        type="text"
        name="title"
        placeholder="Title*"
        class="input input-bordered w-full bg-transparent text-info"
        maxlength={300}
      />
      <div class="label py-1">
        <span class="label-text-alt"></span>
        <span class="label-text-alt">0/300</span>
      </div>
    </label>
    <textarea
      use:autosize
      name="content"
      class="textarea textarea-bordered min-h-[10rem] w-full bg-transparent leading-normal placeholder:opacity-75"
      placeholder="What’s on your mind?"
    ></textarea>
    <div class="ml-auto flex items-center gap-2">
      <button type="button" class="btn btn-neutral h-10">Save Draft</button>
      <button class="btn btn-primary h-10">Post</button>
    </div>
  </form>
</div>
<div class="hidden w-80 md:flex"></div>
