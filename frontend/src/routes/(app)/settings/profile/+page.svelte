<script lang="ts">
  import SettingItem, { type ISettingItem } from '$lib/pages/settings/setting-item.svelte';
  import { createAuthStore } from '$lib/stores/auth.svelte';

  const authStore = createAuthStore();

  const general_settings: ISettingItem[] = [
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

  const advanced_settings: ISettingItem[] = $derived([
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
    <SettingItem {...setting} />
  {/each}
  <div></div>
  <h3 class="text-lg font-medium">Advanced</h3>
  <div class="divider"></div>
  {#each advanced_settings as setting}
    <SettingItem {...setting} />
  {/each}
</div>
