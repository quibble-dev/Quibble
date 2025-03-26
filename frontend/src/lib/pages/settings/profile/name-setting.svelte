<script lang="ts">
  import { createAuthStore } from '$lib/stores/auth.svelte';

  const authStore = createAuthStore();
</script>

<div class="flex flex-col">
  <h3 class="text-info font-medium">Display name</h3>
  <span class="text-base-content/75 text-sm"
    >Changing your display name won't change your username</span
  >
</div>
<label class="floating-label">
  <span class="bg-base-300! duration-100!">Display name</span>
  <div class="input w-full bg-transparent">
    <coreicons-shape-user variant="normal" class="size-4 shrink-0 opacity-50"
    ></coreicons-shape-user>
    <input
      name="name"
      placeholder="Display name"
      defaultValue={authStore.state.user?.profile.name ?? ''}
    />
  </div>
</label>
