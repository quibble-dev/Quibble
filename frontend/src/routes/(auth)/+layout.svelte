<script lang="ts" module>
  type RenderProfileOfType = 'select' | 'create';

  export interface LoginData {
    type: RenderProfileOfType;
  }
</script>

<script lang="ts">
  import GoogleLogo from '$lib/components/icons/logos/google.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble-text.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import { ProfileSelect, ProfileCreate } from '$lib/features/auth';
  import type { Nullable } from '$lib/types/shared';
  import { setContext } from 'svelte';

  let { children } = $props();

  let render_profile_of_type = $state<Nullable<RenderProfileOfType>>(null);

  setContext('handle_login_success', handle_login_success);

  function handle_login_success(data: LoginData) {
    render_profile_of_type = data.type;
  }
</script>

<div class="relative flex flex-1 items-end justify-center p-4 md:items-center">
  <div
    class="absolute inset-0 bg-base-100 [mask-image:url('/assets/svgs/standalone-auth-bg.svg')] [mask-size:cover]"
  ></div>
  <div class="relative flex flex-col gap-4 rounded-box bg-base-300 p-6 md:w-[25rem]">
    <!-- header section -->
    <div class="flex flex-col items-center justify-center gap-4">
      <a href="/" class="flex items-center gap-2">
        <QuibbleLogo class="size-7" />
        <QuibbleTextLogo class="h-7 w-auto" />
      </a>
      <span class="flex flex-col text-center font-medium">
        {#if render_profile_of_type === 'select'}
          Who's quibbling?
          <span class="text-xs font-normal"
            >You can later switch b/w profiles from settings page</span
          >
        {:else if render_profile_of_type === 'create'}
          Let's create a new one!
          <span class="text-xs font-normal"
            >You can later switch b/w profiles from settings page</span
          >
        {:else}
          Join in, share your take, and<br /> make some waves!
        {/if}
      </span>
    </div>
    {#if render_profile_of_type === 'select'}
      <ProfileSelect
        onclick={(type) => {
          if (type === 'back') render_profile_of_type = null;
          else if (type === 'create') render_profile_of_type = 'create';
        }}
      />
    {:else if render_profile_of_type === 'create'}
      <ProfileCreate
        onback={() => (render_profile_of_type = 'select')}
        onsuccess={() => (render_profile_of_type = 'select')}
      />
    {:else}
      <!-- oauth section -->
      <div class="flex w-full items-center gap-3">
        <!-- oauth section: google -->
        <button class="btn flex-1">
          <GoogleLogo class="size-5" />
          Google
        </button>
        <!-- oauth section: github -->
        <button class="btn flex-1">
          <coreicons-logo-github class="size-5"></coreicons-logo-github>
          Github
        </button>
      </div>
      <div class="divider my-0 text-xs font-bold">OR</div>
      <!-- rest pages -->
      {@render children()}
      <!-- footer section -->
      <p class="text-center text-xs">
        By continuing, you agree to the <a
          href="/support/terms-and-conditions"
          class="font-medium text-info underline">Terms of use</a
        >,
        <a href="/support/privary" class="font-medium text-info underline">Privacy</a>
        and <a href="/support/policy" class="font-medium text-info underline">Policy</a> Preplaced.
      </p>
    {/if}
  </div>
</div>
