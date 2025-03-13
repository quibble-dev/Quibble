<script lang="ts">
  import { goto } from '$app/navigation';
  import { page } from '$app/state';
  import autosize from '$lib/actions/autosize';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { cn } from '$lib/functions/classnames';
  import { PostSubmitSchema } from '$lib/schemas/post-submit';
  import { createSidebarStore } from '$lib/stores/sidebar.svelte';
  import { superForm } from 'sveltekit-superforms';
  import { zod } from 'sveltekit-superforms/adapters';

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

  let { data } = $props();

  const sidebarStore = createSidebarStore();

  type Type = keyof typeof types;
  let active_type = $state<Type>('TEXT');

  let community = $state<(typeof communities_select_list)[number] | null>(null);
  let filter_query = $state('');

  const communities_select_list = $derived.by(() => {
    const merged = [...(sidebarStore.state.recent ?? []), ...(sidebarStore.state.your ?? [])];
    const deduped = Array.from(new Map(merged.map((c) => [c.id, c])).values());
    if (filter_query) return deduped.filter((c) => c.name.startsWith(filter_query.toLowerCase()));
    return deduped;
  });

  const { form, errors, enhance, delayed } = superForm(data.form, {
    resetForm: false,
    validators: zod(PostSubmitSchema)
  });

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

<div class="flex flex-1 flex-col gap-4 p-4">
  <h1 class="text-info text-xl font-semibold">Create Post</h1>
  <!-- select community dropdown and select -->
  <div class="flex flex-col gap-1">
    <div class="dropdown w-max">
      <div tabindex="0" role="button" class="btn btn-neutral btn-sm">
        <span>on: </span>
        <Avatar src={community?.avatar} />
        <span class="text-info">{community ? `q/${community.name}` : 'Select a community'}</span>
        <coreicons-shape-chevron variant="down" class="size-4"></coreicons-shape-chevron>
      </div>
      <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
      <ul tabindex="0" class="menu dropdown-content bg-base-100 rounded-box mt-2 gap-1">
        <fieldset class="fieldset pt-0">
          <input
            type="text"
            placeholder="Search filter..."
            class="input input-sm bg-base-200"
            bind:value={filter_query}
          />
          <p class="fieldset-label">Results: {communities_select_list.length}</p>
        </fieldset>
        {#each communities_select_list as item (item.id)}
          {@const selected = community === item}
          <li>
            <button
              class="flex items-center gap-2 p-1"
              class:menu-active={selected}
              onclick={() => {
                community = item;
                $form.community = item.id;
              }}
            >
              <Avatar src={item.avatar} />
              <span class="text-sm font-medium whitespace-nowrap">r/{item.name}</span>
              <div
                class="btn btn-circle btn-success ml-auto size-3.5 p-0"
                class:invisible={!selected}
              >
                <coreicons-shape-check class="size-2.5"></coreicons-shape-check>
              </div>
            </button>
          </li>
        {/each}
      </ul>
    </div>
    {#if $errors.community}
      <span class="text-error text-xs">{$errors.community[0]}</span>
    {/if}
  </div>
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
          <div class="bg-primary absolute -bottom-1.5 h-0.5 w-2/3"></div>
        {/if}
      </div>
    {/each}
  </div>
  <form method="POST" class="flex flex-col gap-2" use:enhance>
    <input type="hidden" name="community" value={community?.id} />

    <fieldset class="fieldset">
      <label class="floating-label">
        <span class="bg-base-300! text-base duration-100!">Title*</span>
        <input
          name="title"
          placeholder="Title*"
          class="input text-info w-full bg-transparent"
          class:input-error={$errors.title}
          aria-invalid={$errors.title ? 'true' : undefined}
          maxlength={300}
          bind:value={$form.title}
        />
      </label>
      <span class="fieldset-label" class:text-error={$errors.title}>
        <span>{$errors.title ? $errors.title[0] : 'Think of a title that grabs attention!'}</span>
        <span class="ml-auto">{$form.title.length}/300</span>
      </span>
    </fieldset>
    <textarea
      use:autosize
      name="content"
      class="textarea min-h-[10rem] w-full bg-transparent leading-normal"
      placeholder="What’s on your mind?"
      bind:value={$form.content}
    ></textarea>
    <div class="ml-auto flex items-center gap-2">
      <button type="button" class="btn btn-neutral" disabled>Save Draft</button>
      <button class={cn($delayed && 'btn-active pointer-events-none', 'btn btn-primary')}>
        Post
        {#if $delayed}<span class="loading loading-spinner loading-xs"></span>{/if}
      </button>
    </div>
  </form>
  <span class="[&>a]:link [&>a]:link-hover mt-auto flex items-center gap-2 self-center text-xs">
    <a href="/">Quibble Rules</a><a href="/">Privacy Policy</a><a href="/">User Agreement</a
    ><coreicons-shape-circle variant="filled" class="size-1"></coreicons-shape-circle><a href="/"
      >Quibble © 2025. All rights reserved.</a
    >
  </span>
</div>
<div class="hidden w-80 lg:flex"></div>
