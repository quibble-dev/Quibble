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
          banner: string;
        }>;
      }
    ).data
  });

  function handle_file_change(e: Event, type: 'avatar' | 'banner') {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        if (type === 'avatar') introduction_data.avatar = String(reader.result);
        if (type === 'banner') introduction_data.banner = String(reader.result);
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
  <form class="flex flex-col-reverse items-start gap-2 md:flex-row md:gap-6">
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
            class="grow border-none p-0 text-sm placeholder:font-normal placeholder:opacity-50 focus:ring-0"
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
          class="textarea textarea-bordered max-h-[15rem] min-h-[7.5rem] bg-transparent leading-normal placeholder:opacity-50"
          placeholder="Tell something nice about your community..."
          maxlength={255}
          oninput={handle_input}
        ></textarea>
      </label>
      {#if errors}
        <ZodErrors {errors} />
      {/if}
    </div>
    <div class="flex flex-col-reverse gap-2 md:w-72 md:flex-col">
      <div class="grid grid-cols-2 gap-4 md:gap-2">
        <label class="form-control">
          <div class="label py-1">
            <span class="label-text">Avatar</span>
          </div>
          <input
            type="file"
            class="file-input file-input-bordered file-input-xs bg-transparent
            file:border-none file:bg-base-100"
            onchange={(e) => handle_file_change(e, 'avatar')}
          />
        </label>
        <label class="form-control">
          <div class="label py-1">
            <span class="label-text">Banner</span>
          </div>
          <input
            type="file"
            class="file-input file-input-bordered file-input-xs bg-transparent
            file:border-none file:bg-base-100"
            onchange={(e) => handle_file_change(e, 'banner')}
          />
        </label>
      </div>
      <div class="overflow-hidden rounded-2xl bg-base-100">
        <div
          class="flex h-10 bg-info bg-cover bg-center"
          style="background-image: url({introduction_data.banner});"
        ></div>
        <div class="flex flex-col gap-4 p-4">
          <div class="flex items-center gap-4">
            <Avatar
              src={introduction_data.avatar}
              class="size-12 flex-shrink-0 !bg-base-content/15 md:size-14"
            />
            <div class="flex flex-col">
              <span class="break-all text-base font-semibold text-info md:text-lg"
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
