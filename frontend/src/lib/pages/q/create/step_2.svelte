<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';
  import type { CommunityCreateFormType } from '$lib/schemas/community-create';
  import { fileProxy } from 'sveltekit-superforms';

  let { form }: { form: CommunityCreateFormType } = $props();

  const avatar_file = fileProxy(form, 'avatar');
  const banner_file = fileProxy(form, 'banner');
</script>

<div class="grid grid-cols-2 gap-2">
  <label class="form-control w-full">
    <div class="label py-1">
      <span class="label-text">Avatar</span>
    </div>
    <input
      type="file"
      name="avatar"
      accept="image/*"
      class="file-input file-input-bordered file-input-xs bg-transparent file:border-none file:bg-base-100"
      bind:files={$avatar_file}
    />
  </label>
  <label class="form-control w-full">
    <div class="label py-1">
      <span class="label-text">Banner</span>
    </div>
    <input
      type="file"
      name="banner"
      accept="image/*"
      class="file-input file-input-bordered file-input-xs bg-transparent file:border-none file:bg-base-100"
      bind:files={$banner_file}
    />
  </label>
</div>
<div class="relative mb-12 h-20 rounded-btn bg-neutral bg-cover bg-center p-4">
  <div class="absolute -bottom-12 flex items-end gap-4">
    <Avatar class="size-20 ring-8 ring-base-300" />
    <div class="flex flex-col">
      <span class="line-clamp-1 text-lg font-semibold">q/{$form.name}</span>
      <div class="flex items-center gap-2">
        <span class="text-xs">1 member</span>
        <coreicons-shape-circle class="size-0.5" variant="filled"></coreicons-shape-circle>
        <span class="text-xs">1 online</span>
      </div>
    </div>
  </div>
</div>
