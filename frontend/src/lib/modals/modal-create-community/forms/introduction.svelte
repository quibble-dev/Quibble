<script lang="ts">
  import autosize from '$lib/actions/autosize';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import ZodErrors from '$lib/components/zod-errors.svelte';
  import type { FormProps } from '../../types';
  import forms from '../forms';
  import { z } from 'zod';

  const schema = z.object({
    name: z
      .string()
      .min(3)
      .regex(/^[a-zA-Z0-9_]+$/, { message: 'Only letters, numbers and underscore are allowed' }),
    description: z.string().min(1)
  });

  let { update_forms_state, forms_state }: FormProps<typeof forms> = $props();

  let errors = $state<z.ZodIssue[]>();
  const introduction_data = $state({
    ...(
      forms_state.introduction as {
        data: Partial<{
          name: string;
          description: string;
          avatar: string;
          cover: string;
        }>;
      }
    ).data
  });

  function handle_file_change(e: Event, type: 'avatar' | 'cover') {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        if (type === 'avatar') introduction_data.avatar = String(reader.result);
        if (type === 'cover') introduction_data.cover = String(reader.result);
      };
      reader.readAsDataURL(file);
    }
  }

  function handle_input() {
    const result = schema.safeParse({
      name: introduction_data.name ?? '',
      description: introduction_data.description ?? ''
    });

    errors = result.error?.errors;

    update_forms_state('introduction', {
      valid: errors === undefined,
      data: { ...introduction_data }
    });
  }
</script>

<div class="flex flex-col gap-4">
  <div class="flex flex-col gap-2">
    <h3 class="text-xl font-semibold text-info">Introduce your community</h3>
    <p class="text-sm">
      Give your community a name and a description that reflects its purpose and vibe.
    </p>
  </div>
  <form class="flex items-start gap-6">
    <div class="flex w-full flex-1 flex-col gap-2">
      <label class="form-control">
        <div class="label py-1">
          <span class="label-text">Name*</span>
          <span class="label-text-alt">{introduction_data.name?.length ?? 0}/25</span>
        </div>
        <label
          class="input input-bordered flex h-10 items-center gap-2 bg-transparent text-sm font-medium"
        >
          q/
          <input
            bind:value={introduction_data.name}
            type="text"
            class="grow border-none p-0 text-sm placeholder:opacity-50 focus:ring-0"
            placeholder="eg: quibble"
            maxlength={25}
            oninput={(e) => {
              introduction_data.name = e.currentTarget.value.replace(/\s/g, '');
              handle_input();
            }}
          />
        </label>
      </label>
      <label class="form-control">
        <div class="label py-1">
          <span class="label-text">Description*</span>
          <span class="label-text-alt">{introduction_data.description?.length ?? 0}/255</span>
        </div>
        <textarea
          bind:value={introduction_data.description}
          use:autosize
          class="textarea textarea-bordered max-h-40 min-h-[5.5rem] bg-transparent leading-normal placeholder:opacity-50"
          placeholder="Tell something nice about your community..."
          maxlength={255}
          oninput={handle_input}
        ></textarea>
      </label>
      {#if errors}
        <ZodErrors {errors} />
      {/if}
    </div>
    <div class="hidden w-72 flex-col md:flex">
      <span class="py-1 text-sm">Preview</span>
      <div class="overflow-hidden rounded-2xl bg-base-100">
        <div
          class="flex h-10 bg-info bg-cover bg-center"
          style="background-image: url({introduction_data.cover});"
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
              <Avatar
                src={introduction_data.avatar}
                class="size-14 flex-shrink-0 !bg-base-content/15"
              />
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
                >q/{introduction_data.name || 'communityname'}</span
              >
              <div class="flex items-center gap-2">
                <span class="text-xs">1 member</span>
                <coreicons-shape-circle class="size-0.5" variant="filled"></coreicons-shape-circle>
                <span class="text-xs">1 online</span>
              </div>
            </div>
          </div>
          <p class="whitespace-pre-line break-words text-sm">
            {introduction_data.description || 'Community description'}
          </p>
        </div>
      </div>
    </div>
  </form>
</div>
