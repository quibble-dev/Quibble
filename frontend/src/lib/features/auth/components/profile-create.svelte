<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { cn } from '$lib/functions/classnames';
  import { ProfileCreateSchema } from '$lib/schemas/auth';
  import { defaults, superForm } from 'sveltekit-superforms';
  import { zod } from 'sveltekit-superforms/adapters';

  type ImageInputType = 'avatar' | 'cover';

  interface Props {
    onback: () => void;
  }

  let { onback }: Props = $props();

  let avatar_data_url = $state<string>(),
    cover_data_url = $state<string>();

  const { form, enhance, errors, delayed } = superForm(defaults(zod(ProfileCreateSchema)), {
    resetForm: false
  });

  function resize_image(file: File, max_width: number, max_height: number): Promise<string> {
    return new Promise((resolve, reject) => {
      const img = new Image();
      const reader = new FileReader();

      reader.onload = (e) => {
        img.src = e.target?.result as string;
      };

      img.onload = () => {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d', { willReadFrequently: true });

        if (!ctx) {
          reject(new Error('Could not get canvas context'));
          return;
        }

        let width = img.width;
        let height = img.height;

        // maintain aspect ratio
        const aspect_ratio = width / height;
        if (width > height) {
          if (width > max_width) {
            width = max_width;
            height = width / aspect_ratio;
          }
        } else {
          if (height > max_height) {
            height = max_height;
            width = height * aspect_ratio;
          }
        }

        canvas.width = width;
        canvas.height = height;

        ctx.drawImage(img, 0, 0, width, height);
        resolve(canvas.toDataURL('image/jpeg', 0.8));
      };

      img.onerror = (err) => reject(err);
      reader.readAsDataURL(file);
    });
  }

  async function handle_file_on_change(e: Event, type: ImageInputType) {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (!file) return;

    $form[type] = file;

    try {
      const dimensions: Record<ImageInputType, [number, number]> = {
        avatar: [400, 400],
        cover: [1200, 400]
      };

      const data_url = await resize_image(file, dimensions[type][0], dimensions[type][1]);

      if (type === 'avatar') avatar_data_url = data_url;
      if (type === 'cover') cover_data_url = data_url;
    } catch (err) {
      console.error(err);
    }
  }
</script>

<form
  class="flex flex-col gap-16"
  method="POST"
  action="?/create"
  enctype="multipart/form-data"
  use:enhance
>
  <div
    class="relative h-20 rounded-btn bg-base-100 bg-cover bg-center p-4"
    style="background-image: url({cover_data_url});"
  >
    <input
      type="file"
      accept="image/*"
      id="cover"
      name="cover"
      class="hidden"
      onchange={(e) => handle_file_on_change(e, 'cover')}
    />
    <div
      class={cn(
        $errors.cover && 'tooltip-open before:text-error',
        'tooltip tooltip-left absolute right-2.5 top-2.5'
      )}
      data-tip={$errors.cover?.[0] ?? 'Edit cover'}
    >
      <label class="btn btn-circle size-8 p-0" for="cover">
        <coreicons-shape-edit variant="pencil" class="size-4"></coreicons-shape-edit>
      </label>
    </div>
    <div class="absolute -bottom-12 flex items-end gap-4">
      <div class="relative size-20">
        <Avatar src={avatar_data_url} class="size-full ring-8 ring-base-300" />
        <input
          type="file"
          accept="image/*"
          id="avatar"
          name="avatar"
          class="hidden"
          onchange={(e) => handle_file_on_change(e, 'avatar')}
        />
        <div
          class={cn(
            $errors.avatar && 'tooltip-open before:text-error',
            'tooltip tooltip-right absolute -right-2.5 top-0'
          )}
          data-tip={$errors.avatar?.[0] ?? 'Edit avatar'}
        >
          <label class="btn btn-circle size-8 p-0" for="avatar">
            <coreicons-shape-edit variant="pencil" class="size-4"></coreicons-shape-edit>
          </label>
        </div>
      </div>
      <div class="flex flex-col">
        <label class="flex items-center text-lg">
          <span class="leading-none">u/</span>
          <input
            type="text"
            name="username"
            class="bg-transparent font-medium text-info outline-none placeholder:font-normal placeholder:text-base-content/50"
            placeholder="username*"
            bind:value={$form.username}
          />
        </label>
        <span class="text-xs text-error" class:invisible={!$errors.username}
          >{$errors.username?.[0] ?? 'error!'}</span
        >
      </div>
    </div>
  </div>
  <div class="flex items-center gap-4">
    <button type="button" class="btn flex-1" aria-label="Back" onclick={onback}>Back</button>
    <button
      class={cn($delayed && 'btn-active pointer-events-none', 'btn btn-primary flex-1')}
      aria-label="Create"
    >
      Create
      {#if $delayed}
        <span class="loading loading-spinner loading-xs"></span>
      {:else}
        <coreicons-shape-arrow variant="right" class="size-4"></coreicons-shape-arrow>
      {/if}
    </button>
  </div>
</form>
