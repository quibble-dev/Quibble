<script lang="ts">
  import { enhance } from '$app/forms';
  // import { invalidateAll } from '$app/navigation';
  import client from '$lib/clients/v1/client';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { PROFILE_CREATE_LIMIT } from '$lib/constants/limits';
  import { cn } from '$lib/functions/classnames';
  import type { SubmitFunction } from '@sveltejs/kit';

  interface Props {
    token?: string;
    onback: () => void;
  }

  let { token, onback }: Props = $props();

  const handle_submit: SubmitFunction = async () => {
    return async () => {
      // re-run load functions and close this modal
      // await invalidateAll();
    };
  };

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

  async function handle_profile_select(id: number, username: string) {
    try {
      const res = await fetch('/api/v1/login/select', {
        method: 'POST',
        body: JSON.stringify({ id, username })
      });

      if (res.ok) {
        const data = await res.json();
        console.log(data);
      }
    } catch (err) {
      console.error(err);
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
          class="group flex flex-col items-center justify-center gap-1.5"
          onclick={() => handle_profile_select(profile.id, profile.username)}
        >
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
      <button class="flex flex-col items-center justify-center gap-1.5">
        <div class="grid size-24 place-items-center rounded-box bg-base-300">
          <coreicons-shape-plus variant="no-border" class="size-8"></coreicons-shape-plus>
        </div>
        <span class="text-xs font-medium">Create new</span>
      </button>
    {/if}
  {/await}
</div>
