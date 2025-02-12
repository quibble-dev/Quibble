<script lang="ts">
  import { goto } from '$app/navigation';
  import { page } from '$app/state';
  import autosize from '$lib/actions/autosize';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { cn } from '$lib/functions/classnames';
  import { PostSubmitSchema } from '$lib/schemas/post-submit';
  import { superForm } from 'sveltekit-superforms';
  import { zod } from 'sveltekit-superforms/adapters';

  let { data } = $props();

  type Type = keyof typeof types;
  let active_type = $state<Type>('TEXT');

  const { form, errors, enhance, delayed } = superForm(data.form, {
    resetForm: false,
    validators: zod(PostSubmitSchema)
  });

  const types = {
    TEXT: {
      label: 'Text',
      onclick: () => null,
      disabled: false
    },
    IMAGE: {
      label: 'Images & Video',
      onclick: () => null,
      disabled: true
    },
    LINK: {
      label: 'Link',
      onclick: () => null,
      disabled: true
    },
    POLL: {
      label: 'Poll',
      onclick: () => null,
      disabled: true
    }
  };

  $effect(() => {
    const url = new URL(page.url);
    const params = url.searchParams;
    const param_type = params.get('type')?.toUpperCase();

    if (param_type && param_type in types) {
      const type_info = types[param_type as Type];

      if (!type_info.disabled) {
        active_type = param_type as Type;
      }
    }

    if (params.get('type') !== active_type) {
      params.set('type', active_type);
      goto(`?${params.toString()}`, { replaceState: true });
    }
  });
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
  <form method="POST" class="flex flex-col gap-2" use:enhance>
    <!-- title input -->
    <label class="form-control w-full">
      <input
        type="text"
        name="title"
        placeholder="Title*"
        class="input input-bordered w-full bg-transparent text-info"
        maxlength={300}
        bind:value={$form.title}
      />
      <div class="label py-1">
        <!-- error store and helptext -->
        <span class="label-text-alt flex items-center gap-2" class:text-error={$errors.title}>
          {#if $errors.title}
            <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
            <span class="text-xs">{$errors.title[0]}</span>
          {:else}
            <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
            <span class="text-xs">Think of a title that grabs attention!</span>
          {/if}
        </span>
        <span class="label-text-alt">0/300</span>
      </div>
    </label>
    <!-- content input -->
    <textarea
      use:autosize
      name="content"
      class="textarea textarea-bordered min-h-[10rem] w-full bg-transparent leading-normal placeholder:opacity-75"
      placeholder="What’s on your mind?"
      bind:value={$form.content}
    ></textarea>
    <!-- form actions -->
    <div class="ml-auto flex items-center gap-2">
      <!-- draft feature later -->
      <button type="button" class="btn btn-neutral" disabled>Save Draft</button>
      <!-- create post with delayed state -->
      <button class={cn($delayed && 'btn-active pointer-events-none', 'btn btn-primary')}>
        Post
        {#if $delayed}<span class="loading loading-spinner loading-xs"></span>{/if}
      </button>
    </div>
  </form>
</div>
<div class="hidden w-80 md:flex"></div>
