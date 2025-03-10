<script lang="ts" module>
  type RenderType = 'select' | 'create' | 'code';

  export interface Data {
    type: RenderType;
    email?: string;
  }
</script>

<script lang="ts">
  import GoogleLogo from '$lib/components/icons/logos/google.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import { ProfileSelect, ProfileCreate, Code } from '$lib/features/auth';
  import type { Nullable } from '$lib/types/shared';
  import { setContext } from 'svelte';

  let { children } = $props();

  let data = $state<Nullable<Data>>(null);
  let render_type = $state<Nullable<RenderType>>(null);

  setContext('handle_success', handle_success);

  function handle_success(_data: Data) {
    data = { ..._data };
    render_type = _data.type;
  }
</script>

<div class="relative flex flex-1 items-center justify-center p-4">
  <div
    class="bg-base-100 absolute inset-0 [mask-image:url('/assets/svgs/standalone-auth-bg.svg')] [mask-size:cover]"
  ></div>
  <div class="relative flex flex-col gap-2">
    <div class="rounded-box bg-base-300 grid w-[40rem] grid-cols-2 gap-5 p-8">
      <div class="flex flex-col gap-2">
        <a href="/" class="w-max"><QuibbleLogo class="size-7" /></a>
        <h2 class="text-info text-3xl font-medium">Sign in</h2>
        <span class="flex flex-col text-sm">
          {#if render_type === 'select'}
            Who's quibbling?
            <span class="text-xs font-normal"
              >You can later switch b/w profiles from settings page</span
            >
          {:else if render_type === 'create'}
            Let's create a new one!
            <span class="text-xs font-normal"
              >You can later switch b/w profiles from settings page</span
            >
          {:else if render_type === 'code'}
            Verify your email
            <span class="text-xs font-normal">Enter the 6-digit code we sent to {data?.email}</span>
          {:else}
            Join in, share your take, and<br /> make some waves!
          {/if}
        </span>
      </div>
      <div class="flex flex-col gap-2">
        {#if render_type === 'select'}
          <ProfileSelect
            onclick={(type) => {
              if (type === 'back') render_type = null;
              else if (type === 'create') render_type = 'create';
            }}
          />
        {:else if render_type === 'create'}
          <ProfileCreate
            onback={() => (render_type = 'select')}
            onsuccess={() => (render_type = 'select')}
          />
        {:else if render_type === 'code'}
          <Code email={data?.email} onback={() => (render_type = null)} />
        {:else}
          {@render children()}
          <div class="divider text-xs font-bold uppercase">or</div>
          <div class="flex gap-2">
            <button class="btn flex-1" aria-label="Login with Google">
              <GoogleLogo class="size-5" />
              Google
            </button>
            <button class="btn flex-1" aria-label="Login with Github">
              <coreicons-logo-github class="size-5"></coreicons-logo-github>
              Github
            </button>
          </div>
        {/if}
      </div>
    </div>
    <div class="flex items-center justify-between px-2 text-xs">
      <span>English (United States)</span>
      <div class="flex items-center gap-2">
        <a href="/">Help</a>
        <a href="/">Privacy</a>
        <a href="/">Terms</a>
      </div>
    </div>
  </div>
</div>
