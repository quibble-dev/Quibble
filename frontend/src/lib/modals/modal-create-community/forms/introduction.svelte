<script lang="ts">
  import autosize from '$lib/actions/autosize';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import ZodErrors from '$lib/components/zod-errors.svelte';
  import type { FormProps } from '../../types';
  import forms from '../forms';
  import { defaults, superForm } from 'sveltekit-superforms';
  import { zod } from 'sveltekit-superforms/adapters';
  import { z } from 'zod';

  const schema = z.object({
    name: z
      .string()
      .min(3)
      .regex(/^[a-zA-Z0-9_]+$/, { message: 'Only letters, numbers, and underscores are allowed' }),
    description: z.string().min(1)
  });

  let { update_forms_state, forms_state }: FormProps<typeof forms> = $props();

  const { form, enhance, errors, validate } = superForm(defaults(zod(schema)), {
    SPA: true,
    resetForm: false,
    validators: zod(schema),
    onUpdate({ form }) {
      console.log(form);
      if (form.valid) {
        // call an external API with form.data, await the result and update form
      }
    },
    onChange({ get }) {
      console.log('get', get('name'));
    }
  });

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
    if (!file) return;

    // convert image file to data uri
    const reader = new FileReader();
    reader.onload = () => {
      if (type === 'avatar') introduction_data.avatar = String(reader.result);
      if (type === 'banner') introduction_data.banner = String(reader.result);
    };
    reader.readAsDataURL(file);
  }

  function handle_name_input(e: Event) {
    // remove unncessarry characters
    $form.name = (e.currentTarget as HTMLInputElement).value.replace(/\s/g, '');
    validate('name');
  }

  function handle_description_input() {
    validate('description');
  }
</script>

<div class="flex flex-col gap-4">
  <!-- header section -->
  <div class="flex flex-col gap-2">
    <h3 class="text-xl font-semibold text-info">Introduce your community</h3>
    <p class="text-sm">
      Give your community a name and a description that reflects its purpose and vibe.
    </p>
  </div>

  <!-- form section -->
  <form use:enhance class="flex flex-col-reverse items-start gap-2 md:flex-row md:gap-6">
    <!-- left column: input fields -->
    <div class="flex w-full flex-1 flex-col gap-2">
      <!-- name input -->
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
            type="text"
            class="grow border-none p-0 text-sm placeholder:font-normal placeholder:opacity-50 focus:ring-0"
            placeholder="eg: quibble"
            maxlength={25}
            bind:value={$form.name}
            oninput={handle_name_input}
          />
        </label>

        <!-- error store -->
        {#if $errors.name}
          <div class="label py-1">
            <span class="label-text flex items-center gap-2 text-error">
              <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
              <span class="text-xs">{$errors.name[0]}</span>
            </span>
          </div>
        {/if}
      </label>

      <!-- description input -->
      <label class="form-control">
        <div class="label py-1">
          <span class="label-text">Description*</span>
          <span class="label-text-alt">{introduction_data.description?.length ?? 0}/255</span>
        </div>
        <textarea
          use:autosize
          class="textarea textarea-bordered max-h-[15rem] min-h-[7.5rem] bg-transparent leading-normal placeholder:opacity-50"
          placeholder="Tell something nice about your community..."
          maxlength={255}
          bind:value={$form.description}
          oninput={handle_description_input}
        ></textarea>

        <!-- error store -->
        {#if $errors.description}
          <div class="label py-1">
            <span class="label-text flex items-center gap-2 text-error">
              <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
              <span class="text-xs">{$errors.description}</span>
            </span>
          </div>
        {/if}
      </label>
    </div>

    <!-- right column: avatar and banner -->
    <div class="flex flex-col-reverse gap-2 md:w-72 md:flex-col">
      <!-- file inputs -->
      <div class="grid grid-cols-2 gap-4 md:gap-2">
        <label class="form-control">
          <div class="label py-1">
            <span class="label-text">Avatar</span>
          </div>
          <input
            type="file"
            class="file-input file-input-bordered file-input-xs bg-transparent file:border-none file:bg-base-100"
            onchange={(e) => handle_file_change(e, 'avatar')}
          />
        </label>
        <label class="form-control">
          <div class="label py-1">
            <span class="label-text">Banner</span>
          </div>
          <input
            type="file"
            class="file-input file-input-bordered file-input-xs bg-transparent file:border-none file:bg-base-100"
            onchange={(e) => handle_file_change(e, 'banner')}
          />
        </label>
      </div>

      <!-- preview section -->
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
              <span class="break-all text-base font-semibold text-info md:text-lg">
                q/{introduction_data.name || 'communityname'}
              </span>
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
