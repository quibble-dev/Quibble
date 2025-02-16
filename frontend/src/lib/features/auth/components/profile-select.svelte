<script lang="ts">
  import { goto, invalidateAll } from '$app/navigation';
  import client from '$lib/clients/v1/client';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { PROFILE_CREATE_LIMIT } from '$lib/constants/limits';
  import { cn } from '$lib/functions/classnames';
  import type { Nullable } from '$lib/types/shared';

  interface Props {
    token?: string;
    onback: () => void;
  }

  let { token, onback }: Props = $props();

  let pending = $state(false);
  let selected_profile_id = $state<Nullable<number>>(null);

  async function fetch_profiles() {
    try {
      const { data, error, response } = await client.GET('/u/me/profiles/', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });

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
    try {
      pending = true;
      selected_profile_id = id;

      const res = await fetch('/api/v1/u/login/select', {
        method: 'POST',
        body: JSON.stringify({ id })
      });

      if (res.ok) {
        const data = await res.json();
        if (!data.success) return;

        goto('/');
        await invalidateAll();
      }
    } catch (err) {
      console.error(err);
    } finally {
      pending = false;
    }
  }
</script>

<div class="tooltip tooltip-right absolute left-2.5 top-2.5 flex before:capitalize" data-tip="Back">
  <button class="btn btn-square btn-circle btn-ghost btn-sm" aria-label="Back" onclick={onback}>
    <coreicons-shape-arrow class="size-5" variant="left"></coreicons-shape-arrow>
  </button>
</div>

<div class="flex flex-wrap items-center justify-center gap-4 self-center">
  {#await fetch_profiles()}
    <span class="loading loading-dots loading-md"></span>
  {:then profiles}
    {#if profiles}
      {#each profiles as profile}
        <button
          class="group relative flex flex-col items-center justify-center gap-1.5"
          class:pointer-events-none={pending}
          onclick={() => handle_profile_select(profile.id, profile.username)}
        >
          <div
            class={cn(
              pending ? 'opacity-100' : 'opacity-0',
              'absolute inset-0 z-10 grid place-items-center bg-base-300/50 transition-opacity duration-300'
            )}
          >
            {#if selected_profile_id === profile.id}
              <span class="loading loading-spinner -translate-y-2.5 transform"></span>
            {/if}
          </div>
          <Avatar
            src={profile.avatar}
            class={cn(
              !profile.avatar && 'border-2',
              'size-24 rounded-box border-base-content/25 !bg-base-300'
            )}
          />
          <span class="line-clamp-1 max-w-24 break-all text-xs font-medium"
            >u/{profile.username}</span
          >
        </button>
      {/each}
    {/if}
    {#if (profiles?.length ?? 0) < PROFILE_CREATE_LIMIT}
      <button
        class={cn(
          pending && 'pointer-events-none opacity-50',
          'flex flex-col items-center justify-center gap-1.5 transition-opacity duration-300'
        )}
      >
        <div class="grid size-24 place-items-center rounded-box bg-base-300">
          <coreicons-shape-plus variant="no-border" class="size-8"></coreicons-shape-plus>
        </div>
        <span class="text-xs font-medium">Create new</span>
      </button>
    {/if}
  {/await}
</div>
