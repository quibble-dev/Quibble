<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { createAuthStore } from '$lib/stores/auth.svelte';

  const authStore = createAuthStore();
</script>

<div class="flex flex-col">
  <h3 class="text-info font-medium">Avatar</h3>
  <span class="text-base-content/75 text-sm"> Edit your avatar or upload an image </span>
</div>
<div class="flex gap-4">
  <Avatar src={authStore.state.user?.profile.avatar} class="size-20" />
  <div class="flex flex-1 flex-col gap-1">
    <input hidden type="file" id="avatar-input" accept="image/*" />
    <label
      for="avatar-input"
      class="rounded-box border-base-content/25 hover:border-base-content/50 flex flex-1 cursor-pointer items-center justify-center gap-2 border-2 border-dashed duration-300"
    >
      <coreicons-shape-upload variant="cloud" class="size-5"></coreicons-shape-upload>
      <span class="text-xs">Drag and drop or browse</span>
    </label>
    <span class="text-base-content/75 text-xs">Max size 5MB</span>
  </div>
</div>
