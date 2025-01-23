<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { zod_required_string } from '$lib/utils/zod';
  import type { FormProps } from '../../types';
  import forms from '../forms';
  import { onDestroy } from 'svelte';

  const name_schema = zod_required_string({ field_name: 'Name' }).min(3, {
    message: 'Name must contain at least 3 character(s)'
  });
  const description_schema = zod_required_string({ field_name: 'Description' });

  let { update_forms_state, forms_state }: FormProps<typeof forms> = $props();

  let name = $state((forms_state.introduction as { name: string }).name ?? '');
  let description = $state((forms_state.introduction as { description: string }).description ?? '');
  let avatar = $state((forms_state.introduction as { avatar: string }).avatar ?? '');
  let cover = $state((forms_state.introduction as { cover: string }).cover ?? '');
  // error states
  let errors = $state<Partial<{ name: string; description: string }>>({});

  function handle_file_change(e: Event, type: 'avatar' | 'cover') {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        if (type === 'avatar') avatar = String(reader.result);
        if (type === 'cover') cover = String(reader.result);
      };
      reader.readAsDataURL(file);
    }
  }

  function handle_input_blur(field: 'name' | 'description') {
    if (field === 'name') {
      const result = name_schema.safeParse(name);
      errors = { ...errors, name: result.success ? undefined : result.error.errors[0]?.message };
    } else if (field === 'description') {
      const result = description_schema.safeParse(description);
      errors = {
        ...errors,
        description: result.success ? undefined : result.error.errors[0]?.message
      };
    }
  }

  // when changes form update forms_state
  onDestroy(() => {
    update_forms_state('introduction', {
      name,
      description,
      avatar,
      cover
    });
  });
</script>

<div class="flex flex-col gap-4">
  <div class="flex flex-col gap-2">
    <h3 class="text-xl font-semibold text-info">Introduce your community</h3>
    <p class="text-sm">
      Give your community a name and a description that reflects its purpose and vibe. This will
      help others discover and connect with it.
    </p>
  </div>
  <form class="flex items-start gap-6">
    <div class="flex-1">
      <label class="form-control">
        <div class="label pt-0">
          <span class="label-text font-medium">Community name*</span>
        </div>
        <label
          class="input input-bordered flex items-center gap-2 text-sm font-medium"
          class:input-error={errors?.name}
        >
          q/
          <input
            bind:value={name}
            type="text"
            class="grow border-none p-0 text-sm focus:ring-0"
            placeholder="eg: quibble"
            maxlength={25}
            onblur={() => handle_input_blur('name')}
            oninput={() => (name = name.replace(/\s/g, ''))}
          />
        </label>
        <div class="label">
          <span class="label-text-alt flex items-center gap-1.5" class:text-error={errors?.name}>
            {#if errors?.name}
              <coreicons-shape-alert-triangle class="size-4"></coreicons-shape-alert-triangle>
              {errors.name}
            {:else}
              <coreicons-shape-info class="size-4"></coreicons-shape-info>
              Name it unique and cool!
            {/if}
          </span>
          <span class="label-text-alt">{name.length}/25</span>
        </div>
      </label>
      <label class="form-control">
        <div class="label pt-0">
          <span class="label-text font-medium">Description*</span>
        </div>
        <textarea
          bind:value={description}
          class="textarea textarea-bordered h-40 leading-normal"
          class:textarea-error={errors?.description}
          placeholder="Tell something nice about your community..."
          maxlength={255}
          onblur={() => handle_input_blur('description')}
        ></textarea>
        <div class="label">
          <span
            class="label-text-alt flex items-center gap-1.5"
            class:text-error={errors?.description}
          >
            {#if errors?.description}
              <coreicons-shape-alert-triangle class="size-4"></coreicons-shape-alert-triangle>
              {errors.description}
            {:else}
              <coreicons-shape-info class="size-4"></coreicons-shape-info>
              A quick cool introduction!
            {/if}
          </span>
          <span class="label-text-alt">{description.length}/255</span>
        </div>
      </label>
    </div>
    <div class="flex w-72 flex-col gap-2">
      <span class="text-sm font-medium">Preview</span>
      <div class="overflow-hidden rounded-2xl bg-neutral shadow-xl">
        <div
          class="flex h-10 bg-base-content bg-cover bg-center"
          style="background-image: url({cover});"
        >
          <input
            id="community-cover-upload"
            type="file"
            accept="image/*"
            class="hidden"
            onchange={(e) => handle_file_change(e, 'cover')}
          />
          <label
            for="community-cover-upload"
            class="btn btn-square btn-circle btn-sm m-1 ml-auto border-none bg-base-300/50"
            aria-label="Upload community cover"
          >
            <coreicons-shape-edit variant="line-with-pencil" class="size-4"></coreicons-shape-edit>
          </label>
        </div>
        <div class="flex flex-col gap-4 p-4">
          <div class="flex items-center gap-4">
            <div
              class="group relative flex items-center justify-center overflow-hidden rounded-full"
            >
              <Avatar src={avatar} class="size-14 flex-shrink-0 !bg-base-content/25" />
              <input
                id="community-avatar-upload"
                type="file"
                accept="image/*"
                class="hidden"
                onchange={(e) => handle_file_change(e, 'avatar')}
              />
              <label
                for="community-avatar-upload"
                class="btn btn-square btn-circle btn-sm absolute m-0 translate-y-12 transform opacity-100 transition-transform duration-300 group-hover:translate-y-0 group-hover:opacity-100"
                aria-label="Upload community avatar"
              >
                <coreicons-shape-edit variant="line-with-pencil" class="size-4"
                ></coreicons-shape-edit>
              </label>
            </div>
            <div class="flex flex-col">
              <span class="break-all text-lg font-semibold text-info"
                >q/{name || 'communityname'}</span
              >
              <div class="flex items-center gap-2">
                <span class="text-xs">1 member</span>
                <coreicons-shape-circle class="size-0.5" variant="filled"></coreicons-shape-circle>
                <span class="text-xs">1 online</span>
              </div>
            </div>
          </div>
          <p class="whitespace-pre-line text-sm">
            {description || 'Community description'}
          </p>
        </div>
      </div>
    </div>
  </form>
</div>
