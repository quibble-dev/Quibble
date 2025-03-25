<script lang="ts">
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import type { SettingItem } from '../+page.svelte';

  const authStore = createAuthStore();

  const general_settings: SettingItem[] = [
    {
      title: 'Display name',
      sub_title: 'Changing your display name won’t change your username',
      value: authStore.state.user?.profile.name ?? 'Not set',
      aria_label: 'Change name'
    },
    {
      title: 'Description/bio',
      aria_label: 'Change description/bio'
    },
    {
      title: 'Avatar',
      sub_title: 'Edit your avatar or upload an image',
      aria_label: 'Change avatar'
    },
    {
      title: 'Banner',
      sub_title: 'Upload an image',
      aria_label: 'Change banner'
    },
    {
      title: 'Social links',
      aria_label: 'Change social links',
      disabled: true
    }
  ];

  const advanced_settings: SettingItem[] = $derived([
    {
      title: `Delete profile u/${authStore.state.user?.profile.username}`,
      sub_title: 'Not revertable!',
      aria_label: 'Delete profile',
      is_dangerous: true
    }
  ]);
</script>

<svelte:head>
  <title>Settings - Profile</title>
</svelte:head>

<div class="flex flex-col gap-2">
  <h3 class="text-lg font-medium">General</h3>
  <div class="divider"></div>
  {#each general_settings as setting}
    {@render setting_item(setting)}
  {/each}
  <div></div>
  <h3 class="text-lg font-medium">Advanced</h3>
  <div class="divider"></div>
  {#each advanced_settings as setting}
    {@render setting_item(setting)}
  {/each}
</div>

{#snippet setting_item({
  title,
  sub_title,
  value,
  aria_label,
  disabled,
  is_dangerous
}: SettingItem)}
  <div class="flex items-center justify-between" class:text-error={is_dangerous}>
    <div class="flex flex-col">
      <span class="text-info text-sm">{title}</span>
      <span class="text-base-content/75 text-xs">{sub_title}</span>
    </div>
    <div class="flex items-center gap-2 text-xs">
      <span>{value}</span>
      <button
        class="btn btn-xs btn-circle"
        class:btn-error={is_dangerous}
        aria-label={aria_label}
        {disabled}
      >
        <coreicons-shape-chevron variant="right" class="size-4"></coreicons-shape-chevron>
      </button>
    </div>
  </div>
{/snippet}
