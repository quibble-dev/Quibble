<script lang="ts">
  import { page } from '$app/state';
  import api from '$lib/api';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { PROFILE_CREATE_LIMIT } from '$lib/constants/limits';
  import { cn } from '$lib/functions/classnames';
  import type { Nullable } from '$lib/types/shared';
  import { onDestroy } from 'svelte';

  interface Props {
    onclick: (type: 'back' | 'create') => void;
  }

  let { onclick }: Props = $props();

  let pending = $state(false);
  let selected_profile_id = $state<Nullable<number>>(null);

  async function fetch_profiles() {
    try {
      const { data, error, response } = await api.GET('/u/me/profiles/');

      if (response.ok && data) {
        return data;
      } else if (error) {
        console.error(error);
      }
    } catch (err) {
      console.error(err);
    }
  }

  async function handle_profile_select(id: number) {
    pending = true;
    selected_profile_id = id;

    try {
      await api.POST('/auth/select/{profile_id}/', {
        params: { path: { profile_id: id } }
      });

      try {
        const dest_param = page.url.searchParams.get('dest') ?? '/';
        const dest = new URL(dest_param, window.location.origin);

        if (window.location.origin === dest.origin) {
          window.location.href = dest.href;
        } else {
          console.warn('invalid destination URL: ', dest.href);
          window.location.href = '/';
        }
      } catch {
        // normal case
        window.location.href = '/';
      }
    } catch (err) {
      console.error(err);
    }
  }

  onDestroy(() => {
    // if user select a profile and window is redirecting,
    // keep these states pending
    // clean only after destroyed
    pending = false;
    selected_profile_id = null;
  });
</script>

<div class="tooltip tooltip-right absolute left-2.5 top-2.5 flex before:capitalize" data-tip="Back">
  <button
    class="btn btn-square btn-circle btn-ghost btn-sm"
    aria-label="Back"
    onclick={() => onclick('back')}
  >
    <coreicons-shape-arrow class="size-5" variant="left"></coreicons-shape-arrow>
  </button>
</div>

<div class="grid grid-cols-3 place-items-center gap-2 md:gap-4">
  {#await fetch_profiles()}
    <span class="loading loading-dots loading-md col-span-3"></span>
  {:then profiles}
    {#if profiles}
      {#each profiles as profile (profile.id)}
        <button
          class="group relative flex size-full flex-col items-center justify-center gap-1.5"
          class:pointer-events-none={pending}
          onclick={() => handle_profile_select(profile.id)}
        >
          <div
            class={cn(
              pending ? 'opacity-100' : 'opacity-0',
              'absolute inset-0 z-10 grid place-items-center bg-base-300/50 transition-opacity duration-300'
            )}
          >
            {#if selected_profile_id === profile.id}
              <span class="loading loading-spinner -translate-y-[0.5rem] transform"></span>
            {/if}
          </div>
          <Avatar
            src={profile.avatar}
            class={cn(
              !profile.avatar && 'border-2',
              'aspect-square size-full rounded-box border-base-content/25 !bg-base-300'
            )}
          />
          <span class="line-clamp-1 break-all text-xs font-medium md:max-w-24"
            >u/{profile.username}</span
          >
        </button>
      {/each}
    {/if}
    {#if (profiles?.length ?? 0) < PROFILE_CREATE_LIMIT}
      <button
        onclick={() => onclick('create')}
        class={cn(
          pending && 'pointer-events-none opacity-50',
          'flex size-full flex-col items-center justify-center gap-1.5 transition-opacity duration-300'
        )}
      >
        <div class="grid aspect-square size-full place-items-center rounded-box bg-base-300">
          <coreicons-shape-plus variant="no-border" class="size-8"></coreicons-shape-plus>
        </div>
        <span class="line-clamp-1 text-xs font-medium md:max-w-24">Create new</span>
      </button>
    {/if}
  {/await}
</div>
