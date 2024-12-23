<script lang="ts">
  import { enhance } from '$app/forms';
  import { invalidateAll } from '$app/navigation';
  import client from '$lib/clients/client';
  import type { components } from '$lib/clients/v1';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
  import Image from '$lib/components/ui/image.svelte';
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import type { FormProps } from '../types';
  import type { SubmitFunction } from '@sveltejs/kit';
  import { onMount } from 'svelte';

  type Profile = components['schemas']['Profile'];

  let { update_forms_state, forms_state, goto_form }: FormProps = $props();

  let pending = $state(false);
  let status_text = $state<string | null>(null);

  let profiles = $state<Profile[]>([]);

  const modalsStore = createModalsStore();

  const handle_submit: SubmitFunction = async () => {
    pending = true;
    status_text = 'Setting up profile...';

    return async () => {
      // re-run load functions and close this modal
      await invalidateAll();
      modalsStore.close('auth');

      pending = false;
      status_text = null;
    };
  };

  onMount(async () => {
    // check if forms_state has profiles
    // so avoid a query
    if ((forms_state.profile_select as { profiles: Profile[] }).profiles) {
      profiles = (forms_state.profile_select as { profiles: Profile[] }).profiles;
    } else {
      pending = true;
      status_text = 'Fetching profiles...';

      const { data, error, response } = await client.GET('/api/v1/users/me/profiles/', {
        headers: {
          Authorization: `Bearer ${(forms_state.login as { token: string }).token}`
        }
      });

      if (response.ok && data) {
        profiles = data;
        // add to forms_state
        update_forms_state('profile_select', { profiles });
      } else if (error) {
        console.log(error);
      }

      pending = false;
      status_text = null;
    }
  });
</script>

{#if pending}
  <span class="loading loading-spinner loading-md absolute right-2.5 top-2.5"></span>
{/if}
<div class="flex flex-col gap-4">
  <div class="flex flex-col items-center justify-center gap-4">
    <div class="flex items-center gap-2">
      <QuibbleLogo class="size-7" />
      <QuibbleTextLogo class="h-7 w-auto" />
    </div>
    <div class="flex flex-col gap-1">
      <p class="text-center font-medium">
        {status_text ?? "Who's quibbling?"}
      </p>
      <span class="self-center text-xs"
        >You can later switch b/w profiles on settings page.</span
      >
    </div>
  </div>
  <div
    class="flex flex-wrap items-center justify-center gap-x-6 gap-y-4 self-center"
    class:pointer-events-none={pending}
  >
    {#each profiles as profile}
      <form method="POST" action="/settings/profile?/select" use:enhance={handle_submit}>
        <input type="hidden" name="profile_id" value={profile.id} />
        <button
          type="submit"
          class="group flex flex-col items-center justify-center gap-2.5"
        >
          <Image
            class="size-20 rounded-2xl outline outline-offset-4 outline-neutral"
            src={profile.avatar}
          />
          <span class="line-clamp-1 max-w-20 break-all text-xs font-medium"
            >u/{profile.username}</span
          >
        </button>
      </form>
    {/each}
    {#if !(profiles.length >= 3)}
      <button
        onclick={() => goto_form('profile_create')}
        class="flex flex-col items-center justify-center gap-2.5"
      >
        <div
          class="grid size-20 place-items-center rounded-2xl bg-neutral outline outline-offset-4 outline-neutral"
        >
          <coreicons-shape-plus variant="no-border" class="size-8"></coreicons-shape-plus>
        </div>
        <span class="text-xs font-medium">Create new</span>
      </button>
    {/if}
  </div>
</div>
