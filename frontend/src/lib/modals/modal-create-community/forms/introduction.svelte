<script lang="ts">
  import autosize from '$lib/actions/autosize';
  import client from '$lib/clients';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { debounce } from '$lib/functions/debounce';
  import type { FormProps } from '../../types';
  import forms from '../forms';
  import { onMount } from 'svelte';
  import { defaults, superForm } from 'sveltekit-superforms';
  import { zod } from 'sveltekit-superforms/adapters';
  import { z } from 'zod';

  const schema = z.object({
    name: z
      .string()
      .min(3)
      .regex(/^[a-zA-Z0-9_]+$/, { message: 'Only letters, numbers, and underscores are allowed' }),
    description: z.string().min(1),
    avatar: z
      .instanceof(File)
      .refine((f) => f.size < 100_000, 'Max 100 kB upload size.')
      .optional(),
    banner: z
      .instanceof(File)
      .refine((f) => f.size < 100_000, 'Max 100 kB upload size.')
      .optional()
  });

  let { forms_state, update_forms_state }: FormProps<typeof forms> = $props();

  const initial_data = {
    ...(
      forms_state.introduction as {
        data: Partial<{
          name: string;
          description: string;
          avatar: File | undefined;
          banner: File | undefined;
        }>;
      }
    ).data
  };

  let name_taken = $state(false);
  let avatar_data_url = $state<string>();
  let banner_data_url = $state<string>();

  const { form, enhance, errors, validate, validateForm } = superForm(
    defaults(initial_data, zod(schema)),
    {
      SPA: true,
      resetForm: false,
      validators: zod(schema),
      validationMethod: 'oninput',
      onChange: async () => {
        const result = await validateForm({ update: false });
        update_forms_state('introduction', {
          valid: result.valid,
          data: { ...result.data }
        });
      }
    }
  );

  function handle_file_change(e: Event, type: 'avatar' | 'banner') {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (!file) return;

    // store the file directly
    $form[type] = file;

    // convert file to data url for preview
    const reader = new FileReader();
    reader.onload = function () {
      if (type === 'avatar') avatar_data_url = String(reader.result);
      if (type === 'banner') banner_data_url = String(reader.result);
    };
    reader.readAsDataURL(file);
  }

  async function handle_name_input(e: Event) {
    name_taken = false;
    // remove unncessarry characters
    $form.name = (e.currentTarget as HTMLInputElement).value.replace(/\s/g, '');
    await validate('name');

    if (!$errors.name) {
      // call API to validate name if it exists or not
      await debounced_handle_check_name_exists();
    }
  }

  function handle_description_input() {
    if (name_taken) return;
    validate('description');
  }

  async function handle_check_name_exists() {
    const { data, response } = await client.GET('/communities/{name}/exists/', {
      params: {
        path: { name: $form.name }
      }
    });

    if (data && response.ok) {
      return data.exists;
    } else {
      return false;
    }
  }

  const debounced_handle_check_name_exists = debounce(async () => {
    name_taken = await handle_check_name_exists();
  }, 500);

  onMount(async () => {
    await debounced_handle_check_name_exists();
    if (!name_taken) await validateForm();
  });
</script>

<div class="flex flex-col gap-4">
  <!-- header section -->
  <div class="flex flex-col gap-1">
    <h3 class="text-xl font-semibold text-info">Introduce your community</h3>
    <p class="text-sm">
      Give your community a name and a description that reflects its purpose and vibe.
    </p>
  </div>

  <!-- form section -->
  <form use:enhance class="flex flex-col-reverse items-start gap-2 md:flex-row md:gap-4">
    <!-- left column: input fields -->
    <div class="flex w-full flex-1 flex-col gap-2">
      <!-- name input -->
      <label class="form-control">
        <div class="label py-1">
          <span class="label-text">Name*</span>
          <span class="label-text-alt">{$form.name.length}/25</span>
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
        {#if name_taken || $errors.name}
          <div class="label py-1">
            <span class="label-text flex items-center gap-2 text-error">
              <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
              <span class="text-xs"
                >{name_taken ? `"q/${$form.name}" is already taken` : $errors.name?.[0]}</span
              >
            </span>
          </div>
        {/if}
      </label>

      <!-- description input -->
      <label class="form-control">
        <div class="label py-1">
          <span class="label-text">Description*</span>
          <span class="label-text-alt">{$form.description.length}/255</span>
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
              <span class="text-xs">{$errors.description[0]}</span>
            </span>
          </div>
        {/if}
      </label>
    </div>

    <!-- right column: avatar and banner -->
    <div class="flex flex-1 flex-col-reverse gap-2 md:flex-col">
      <!-- file inputs -->
      <div class="grid grid-cols-2 gap-4 md:gap-2">
        <label class="form-control">
          <div class="label py-1">
            <span class="label-text">Avatar</span>
          </div>
          <input
            type="file"
            accept="image/*"
            class="file-input file-input-bordered file-input-xs bg-transparent file:border-none file:bg-base-100"
            onchange={(e) => handle_file_change(e, 'avatar')}
          />

          <!-- error store -->
          {#if $errors.avatar}
            <div class="label py-1">
              <span class="label-text flex items-center gap-2 text-error">
                <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
                <span class="text-xs">{$errors.avatar?.[0]}</span>
              </span>
            </div>
          {/if}
        </label>
        <label class="form-control">
          <div class="label py-1">
            <span class="label-text">Banner</span>
          </div>
          <input
            type="file"
            accept="image/*"
            class="file-input file-input-bordered file-input-xs bg-transparent file:border-none file:bg-base-100"
            onchange={(e) => handle_file_change(e, 'banner')}
          />

          <!-- error store -->
          {#if $errors.banner}
            <div class="label py-1">
              <span class="label-text flex items-center gap-2 text-error">
                <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
                <span class="text-xs">{$errors.banner?.[0]}</span>
              </span>
            </div>
          {/if}
        </label>
      </div>

      <!-- preview section -->
      <div class="overflow-hidden rounded-2xl bg-base-100">
        <div
          class="flex h-10 bg-info bg-cover bg-center"
          style="background-image: url({banner_data_url});"
        ></div>
        <div class="flex flex-col gap-4 p-4">
          <div class="flex items-center gap-4">
            <Avatar
              src={avatar_data_url}
              class="size-12 flex-shrink-0 !bg-base-content/15 md:size-14"
            />
            <div class="flex flex-col">
              <span class="break-all text-base font-semibold text-info md:text-lg">
                q/{$form.name || 'communityname'}
              </span>
              <div class="flex items-center gap-2">
                <span class="text-xs">1 member</span>
                <coreicons-shape-circle class="size-0.5" variant="filled"></coreicons-shape-circle>
                <span class="text-xs">1 online</span>
              </div>
            </div>
          </div>
          <p class="whitespace-pre-line break-words text-sm">
            {$form.description || 'Community description'}
          </p>
        </div>
      </div>
    </div>
  </form>
</div>
