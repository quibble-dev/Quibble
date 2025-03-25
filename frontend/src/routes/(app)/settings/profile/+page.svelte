<script lang="ts">
  import BaseModal from '$lib/components/ui/base-modal.svelte';
  import FormName from '$lib/pages/settings/profile/form-name.svelte';
  import SettingItem, { type ISettingItem } from '$lib/pages/settings/setting-item.svelte';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import type { Nullable } from '$lib/types/shared';
  import type { Component } from 'svelte';

  type Settings = 'name' | 'bio' | 'avatar' | 'banner' | 'title';

  const authStore = createAuthStore();

  const general_settings: Record<Settings, ISettingItem> = {
    name: {
      title: 'Display name',
      sub_title: 'Changing your display name won’t change your username',
      value: authStore.state.user?.profile.name ?? 'Not set',
      aria_label: 'Change name'
    },
    bio: {
      title: 'Description/bio',
      aria_label: 'Change description/bio'
    },
    avatar: {
      title: 'Avatar',
      sub_title: 'Edit your avatar or upload an image',
      aria_label: 'Change avatar'
    },
    banner: {
      title: 'Banner',
      sub_title: 'Upload an image',
      aria_label: 'Change banner'
    },
    title: {
      title: 'Social links',
      aria_label: 'Change social links',
      disabled: true
    }
  };

  const advanced_settings: ISettingItem[] = $derived([
    {
      title: `Delete profile u/${authStore.state.user?.profile.username}`,
      sub_title: 'Not revertable!',
      aria_label: 'Delete profile',
      is_dangerous: true
    }
  ]);

  const settings_component_mapping: Record<Settings, Component> = {
    name: FormName,
    bio: FormName,
    avatar: FormName,
    banner: FormName,
    title: FormName
  };

  let show_modal = $state(false);
  let show_setting = $state<Nullable<Settings>>(null);
  const SettingComponent = $derived(
    show_setting !== null ? settings_component_mapping[show_setting] : null
  );
</script>

<svelte:head>
  <title>Settings - Profile</title>
</svelte:head>

<div class="flex flex-col gap-2">
  <h3 class="text-lg font-medium">General</h3>
  <div class="divider"></div>
  {#each Object.entries(general_settings) as [key, setting]}
    <SettingItem
      {...setting}
      onclick={() => {
        show_modal = true;
        show_setting = key as Settings;
      }}
    />
  {/each}
  <div></div>
  <h3 class="text-lg font-medium">Advanced</h3>
  <div class="divider"></div>
  {#each advanced_settings as setting}
    <SettingItem {...setting} />
  {/each}
</div>

<BaseModal open={show_modal} onclose={() => (show_modal = false)} class="flex flex-col">
  {#if SettingComponent}
    <SettingComponent />
  {/if}
  <div class="flex items-center justify-end gap-2">
    <button onclick={() => (show_modal = false)} class="btn">Cancel</button>
    <button class="btn btn-primary">
      Save <coreicons-shape-check class="size-4"></coreicons-shape-check>
    </button>
  </div>
</BaseModal>
