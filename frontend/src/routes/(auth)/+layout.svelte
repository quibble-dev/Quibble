<script lang="ts" module>
  const RENDER_TYPE = ['select', 'create', 'code'] as const;
  type RenderType = (typeof RENDER_TYPE)[number];

  export interface Data {
    type: RenderType;
    email?: string;
  }

  const TYPE_TITLES: Record<string, string> = {
    '/login': 'Sign in',
    '/register': 'Sign up',
    '/password': 'Password'
  };
</script>

<script lang="ts">
  import { page } from '$app/state';
  import { PUBLIC_GOOGLE_OAUTH_CLIENT_ID, PUBLIC_OAUTH_CALLBACK_URL } from '$env/static/public';
  import GoogleLogo from '$lib/components/icons/logos/google.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import { ProfileSelect, ProfileCreate, Code } from '$lib/features/auth';
  import type { Nullable } from '$lib/types/shared';
  import { setContext, untrack } from 'svelte';

  let { children } = $props();

  let data = $state<Nullable<Data>>(null);
  let render_type = $state<Nullable<RenderType>>(null);

  setContext('handle_success', handle_success);

  function handle_success(_data: Data) {
    data = { ..._data };
    render_type = _data.type;
  }

  function handle_google_click() {
    window.location.replace(
      `https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=${PUBLIC_OAUTH_CALLBACK_URL}&prompt=consent&response_type=code&client_id=${PUBLIC_GOOGLE_OAUTH_CLIENT_ID}&scope=openid%20email%20profile&access_type=offline`
    );
  }

  function is_render_type(type: string): type is RenderType {
    return RENDER_TYPE.includes(type as RenderType);
  }

  $effect(() => {
    const type_param = page.url.searchParams.get('type');
    if (type_param && is_render_type(type_param)) {
      const email_param = page.url.searchParams.get('email');
      if (email_param) data = { ...untrack(() => data as Data), email: email_param };
      render_type = type_param;
    }
  });
</script>

<div class="relative flex flex-1 items-center justify-center p-4">
  <div
    class="bg-base-100 absolute inset-0 [mask-image:url('/assets/svgs/standalone-auth-bg.svg')] [mask-size:cover]"
  ></div>
  <div class="relative flex flex-col gap-2">
    <div class="rounded-box bg-base-300 grid gap-5 p-8 md:w-[40rem] md:grid-cols-2">
      <div class="flex flex-col gap-2">
        <a href="/" class="w-max"><QuibbleLogo class="size-7" /></a>
        <h2 class="text-info text-3xl font-medium">{TYPE_TITLES[page.url.pathname]}</h2>
        <span class="flex flex-col text-sm">
          {#if render_type === 'select'}
            Who's quibbling? You can later switch b/w profiles from settings page.
          {:else if render_type === 'create'}
            Let's create a new one! You can later edit this from settings page.
          {:else if render_type === 'code'}
            Verify your e-mail, enter the 6-digit code we sent to {data?.email}.
          {:else}
            Join in, share your take, and make some waves!
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
          <div class="divider my-0 h-max text-xs font-bold uppercase before:h-px after:h-px">
            or
          </div>
          <div class="flex gap-2">
            <button class="btn flex-1" aria-label="Login with Google" onclick={handle_google_click}>
              <GoogleLogo class="size-5" />
              Google
            </button>
            <button class="btn flex-1" aria-label="Login with Github" disabled>
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
