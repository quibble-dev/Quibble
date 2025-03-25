<script lang="ts" module>
  export interface SettingItem {
    title: string;
    sub_title?: string;
    value?: string;
    aria_label: string;
    disabled?: boolean;
    is_dangerous?: boolean;
  }
</script>

<script lang="ts">
  import { createAuthStore } from '$lib/stores/auth.svelte';

  const authStore = createAuthStore();

  const general_settings: SettingItem[] = $derived([
    {
      title: 'Email address',
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

  const advanced_settings: SettingItem[] = [
    {
      title: 'Delete account',
      value: 'Not revertable!',
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
    {@render setting_item(setting)}
  {/each}
  <div></div>
  <h3 class="text-lg font-medium">Advanced</h3>
  <div class="divider"></div>
  {#each advanced_settings as setting}
    {@render setting_item(setting)}
  {/each}
</div>

{#snippet setting_item({ title, value, aria_label, disabled, is_dangerous }: SettingItem)}
  <div class="flex items-center justify-between" class:text-error={is_dangerous}>
    <span class="text-sm">{title}</span>
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
