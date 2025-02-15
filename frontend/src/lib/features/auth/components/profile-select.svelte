<script lang="ts">
  import { enhance } from '$app/forms';
  import { invalidateAll } from '$app/navigation';
  import client from '$lib/clients/v1/client';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { toast } from '$lib/components/ui/toast';
  import { PROFILE_CREATE_LIMIT } from '$lib/constants/limits';
  import { cn } from '$lib/functions/classnames';
  import type { SubmitFunction } from '@sveltejs/kit';

  let { token }: { token?: string } = $props();

  const handle_submit: SubmitFunction = async () => {
    return async ({ formData }) => {
      // re-run load functions and close this modal
      await invalidateAll();
      toast.push(`Logged in as u/${String(formData.get('profile_username'))}`);
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
</script>

<div class="flex flex-wrap items-center justify-center gap-4 self-center">
  {#await fetch_profiles()}
    <span class="loading loading-dots loading-md"></span>
  {:then profiles}
    {#if profiles}
      {#each profiles as profile}
        <form method="POST" action="/auth?/profile_select" use:enhance={handle_submit}>
          <input type="hidden" name="profile_id" value={profile.id} />
          <input type="hidden" name="profile_username" value={profile.username} />
          <button type="submit" class="group flex flex-col items-center justify-center gap-1.5">
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
        </form>
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
