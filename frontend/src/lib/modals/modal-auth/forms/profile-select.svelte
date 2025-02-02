<script lang="ts">
  import { enhance } from '$app/forms';
  import { invalidateAll } from '$app/navigation';
  import client from '$lib/clients';
  import type { components } from '$lib/clients/v1/schema';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble-text.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { toast } from '$lib/components/ui/toast/toast.svelte';
  import { PROFILE_CREATE_LIMIT } from '$lib/constants/limits';
  import { cn } from '$lib/functions/classnames';
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import type { FormProps } from '../../types';
  import forms from '../forms';
  import type { SubmitFunction } from '@sveltejs/kit';
  import { onMount } from 'svelte';

  type Profile = components['schemas']['Profile'];

  let { update_forms_state, forms_state, goto_form }: FormProps<typeof forms> = $props();

  let pending = $state(false);
  let status_text = $state<string | null>(null);
  let profiles = $state<Profile[]>([]);

  const modalsStore = createModalsStore();

  const handle_submit: SubmitFunction = async () => {
    pending = true;
    status_text = 'Setting up profile...';

    return async ({ formData }) => {
      // re-run load functions and close this modal
      await invalidateAll();
      modalsStore.close('auth');
      toast.push({ message: `Logged in as u/${String(formData.get('profile_username'))}` });

      pending = false;
      status_text = null;
    };
  };

  const fetch_profiles = async () => {
    pending = true;
    status_text = 'Fetching profiles...';

    const { data, error, response } = await client.GET('/u/me/profiles/', {
      headers: {
        Authorization: `Bearer ${(forms_state.join as { token: string }).token}`
      }
    });

    if (response.ok && data) {
      profiles = data;
      update_forms_state('profile_select', {
        token: (forms_state.join as { token: string }).token,
        profiles
      });
    } else if (error) {
      console.error(error);
    }

    pending = false;
    status_text = null;
  };

  onMount(async () => {
    // check if forms_state has profiles and tokens are same
    // if tokens are same- it means, user is same, otherwise- different (fetch)
    // so avoid some query

    const join_state = forms_state.join as { token: string };
    const profile_select_state = forms_state.profile_select as {
      token: string;
      profiles?: Profile[];
    };

    if (join_state.token === profile_select_state.token && profile_select_state.profiles) {
      // requested for same user (re-use)
      profiles = profile_select_state.profiles;
    } else {
      // new request (fetch)
      await fetch_profiles();
    }
  });
</script>

<!-- loading spinner on actions -->
{#if pending}
  <span class="loading loading-spinner loading-md absolute right-2.5 top-2.5"></span>
{/if}

<div class="flex flex-col gap-4">
  <!-- header section -->
  <div class="flex flex-col items-center justify-center gap-4">
    <div class="flex items-center gap-2">
      <QuibbleLogo class="size-7" />
      <QuibbleTextLogo class="h-7 w-auto" />
    </div>

    <!-- helper texts -->
    <div class="flex flex-col gap-1">
      <p class="text-center font-medium">
        {status_text ?? "Who's quibbling?"}
      </p>
      <span class="self-center text-xs">You can later switch b/w profiles on settings page.</span>
    </div>
  </div>

  <!-- list profiles accosiated with user and show create new btn -->
  <div
    class="flex flex-wrap items-center justify-center gap-4 self-center"
    class:pointer-events-none={pending}
  >
    <!-- list profiles -->
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

    <!-- show create new profile option only when profiles count is under limit -->
    {#if profiles.length < PROFILE_CREATE_LIMIT}
      <button
        onclick={() => goto_form('profile_create')}
        class="flex flex-col items-center justify-center gap-1.5"
      >
        <div class="grid size-24 place-items-center rounded-box bg-base-300">
          <coreicons-shape-plus variant="no-border" class="size-8"></coreicons-shape-plus>
        </div>
        <span class="text-xs font-medium">Create new</span>
      </button>
    {/if}
  </div>
</div>
