<script lang="ts">
  import type { ISettingItem } from '$lib/pages/settings/setting-item.svelte';
  import SettingItem from '$lib/pages/settings/setting-item.svelte';
  import { createAuthStore } from '$lib/stores/auth.svelte';

  const authStore = createAuthStore();

  const general_settings: ISettingItem[] = $derived([
    {
      title: 'Email address',
      sub_title: 'Changing your email address will affect all your profiles',
      value: authStore.state.user?.email ?? 'Not set',
      aria_label: 'Change email address',
      disabled: true
    },
    {
      title: 'Gender',
      value: 'Not set',
      aria_label: 'Change gender',
      disabled: true
    },
    {
      title: 'Location customization',
      value: 'Use approximate (based on IP)',
      aria_label: 'Change location',
      disabled: true
    }
  ]);

  const advanced_settings: ISettingItem[] = [
    {
      title: 'Delete account',
      sub_title: 'Not revertable!',
      aria_label: 'Delete account',
      is_dangerous: true
    }
  ];
</script>

<svelte:head>
  <title>Settings - Account</title>
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
