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
        // normal case
        if (dest_param.startsWith('/')) window.location.href = dest_param;
        // handle encoded paths
        else if (dest_param.startsWith('%2F')) {
          window.location.href = decodeURIComponent(dest_param);
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

<div class="flex flex-1 flex-col gap-2">
  {#await fetch_profiles()}
    <div class="col-span-3 m-auto flex flex-col items-center">
      <span class="loading loading-dots loading-md"></span>
      <span class="text-xs">fetching profiles...</span>
    </div>
  {:then profiles}
    {#if profiles}
      <div class="grid grid-cols-3 place-items-center gap-2 md:gap-4">
        {#each profiles as profile (profile.id)}
          <div hidden class="relative flex flex-col items-center gap-1.5">
            <button
              class="btn disabled:before:bg-base-300/50 relative flex-1 bg-transparent! p-0
              disabled:before:absolute disabled:before:inset-0 disabled:before:z-10"
              disabled={pending}
              class:pointer-events-none={pending}
              onclick={() => handle_profile_select(profile.id)}
            >
              {#if pending && selected_profile_id === profile.id}
                <div class="absolute inset-0 z-20 grid place-items-center">
                  <span class="loading loading-spinner text-info"></span>
                </div>
              {/if}
              <Avatar
                src={profile.avatar}
                class={cn('rounded-box bg-base-300! aspect-square h-auto! w-full!')}
              />
            </button>
            <span class="line-clamp-1 text-xs font-medium break-all md:max-w-24"
              >u/{profile.username}</span
            >
          </div>
          <button
            class="relative flex size-full cursor-pointer flex-col items-center justify-center gap-1.5"
            class:pointer-events-none={pending}
            onclick={() => handle_profile_select(profile.id)}
          >
            <div
              class={cn(
                pending ? 'opacity-100' : 'opacity-0',
                'bg-base-300/50 absolute inset-0 z-10 grid place-items-center transition-opacity duration-300'
              )}
            >
              {#if selected_profile_id === profile.id}
                <span class="loading loading-spinner -translate-y-[0.5rem] transform"></span>
              {/if}
            </div>
            <Avatar
              src={profile.avatar}
              class={cn('rounded-box bg-base-300! aspect-square h-auto! w-full!')}
            />
            <span class="line-clamp-1 text-xs font-medium break-all md:max-w-24"
              >u/{profile.username}</span
            >
          </button>
        {/each}
      </div>
    {/if}
    <div class="flex items-center gap-4">
      <button type="button" class="btn flex-1" aria-label="Back" onclick={() => onclick('back')}>
        <coreicons-shape-arrow variant="left" class="size-4"></coreicons-shape-arrow>
        Back
      </button>
      <button
        class="btn btn-primary flex-1"
        aria-label="Create"
        onclick={() => onclick('create')}
        disabled={(profiles?.length ?? 0) >= PROFILE_CREATE_LIMIT}
      >
        Create new
        <coreicons-shape-arrow variant="right" class="size-4"></coreicons-shape-arrow>
      </button>
    </div>
  {/await}
</div>
