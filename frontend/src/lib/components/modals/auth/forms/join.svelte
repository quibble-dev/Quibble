<script lang="ts">
  import { enhance } from '$app/forms';
  import GoogleLogo from '$lib/components/icons/logos/google.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
  import { cn } from '$lib/functions/classnames';
  import type { FormProps } from '../types';
  import type { SubmitFunction } from '@sveltejs/kit';
  import type { HTMLInputAttributes } from 'svelte/elements';

  let { update_forms_state, goto_form }: FormProps = $props();

  let auth_type = $state<'login' | 'register'>('login');
  let password_type = $state<HTMLInputAttributes['type']>('password');

  let errors = $state<Record<string, string> | undefined>();
  let pending = $state(false);

  const handle_submit: SubmitFunction = async () => {
    pending = true;

    return async ({ result }) => {
      if (result.type === 'success') {
        errors = undefined;
        if (auth_type === 'login') {
          // save token on forms_state
          update_forms_state('join', { token: result.data?.token });
          // next form
          goto_form('profile_select');
        } else if (auth_type === 'register') {
          auth_type = 'login';
        }
      } else if (result.type === 'failure') {
        errors = result.data;
      }
      pending = false;
    };
  };

  function handle_auth_type_change() {
    auth_type = auth_type === 'login' ? 'register' : 'login';
  }

  function handle_toggle_password_type() {
    password_type = password_type === 'password' ? 'text' : 'password';
  }
</script>

<div class="flex flex-col gap-4">
  <div class="flex flex-col items-center justify-center gap-4">
    <div class="flex items-center gap-2">
      <QuibbleLogo class="size-7" />
      <QuibbleTextLogo class="h-7 w-auto" />
    </div>
    <p class="text-center font-medium">
      Join in, share your take, and<br /> make some waves!
    </p>
  </div>
  <button class="btn btn-ghost btn-active">
    <GoogleLogo class="size-5" />
    Continue with Google
  </button>
  <div class="divider my-0 text-xs font-bold">OR</div>
  <form
    method="POST"
    action="/auth?/{auth_type}"
    use:enhance={handle_submit}
    class="flex flex-col gap-3"
  >
    <label class="input input-bordered flex items-center gap-2">
      <coreicons-shape-mail class="size-4"></coreicons-shape-mail>
      <input
        type="email"
        name="email"
        required
        class="grow border-none p-2 text-sm font-medium focus:ring-0"
        placeholder="Email address*"
      />
    </label>
    <label class="input input-bordered flex items-center gap-2 pr-2">
      <coreicons-shape-lock class="size-4"></coreicons-shape-lock>
      <input
        type={password_type}
        name="password"
        required
        minlength="8"
        class="grow border-none p-2 text-sm font-medium focus:ring-0"
        placeholder="Password*"
      />
      <button
        type="button"
        class={cn(
          password_type === 'password'
            ? 'btn-neutral border border-base-content/25'
            : 'btn-ghost btn-active',
          'btn btn-square btn-sm ml-auto hover:btn-ghost'
        )}
        aria-label="Show/hide password"
        onclick={handle_toggle_password_type}
      >
        <coreicons-shape-eye
          class="size-4"
          variant={password_type === 'password' ? 'open' : 'close'}
        ></coreicons-shape-eye>
      </button>
    </label>
    <div class="flex items-center gap-2">
      {#if errors?.detail}
        <coreicons-shape-alert-triangle class="size-3 text-error"
        ></coreicons-shape-alert-triangle>
        <span class="text-xs text-error">{errors.detail}</span>
      {:else}
        <coreicons-shape-info class="size-3"></coreicons-shape-info>
        <span class="text-xs">Hint: you can switch b/w 'login' and 'register'.</span>
      {/if}
    </div>
    <div class="flex items-center gap-3">
      <button
        type="submit"
        class={cn(pending && 'btn-active pointer-events-none', 'btn btn-primary flex-1')}
      >
        {#if pending}
          {auth_type === 'login' ? 'Logging in' : 'Registering'}
          <span class="loading loading-spinner loading-xs"></span>
        {:else}
          {auth_type === 'login' ? 'Log in' : 'Register'}
          <coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
        {/if}
      </button>
      <button
        type="button"
        class="btn btn-secondary"
        onclick={handle_auth_type_change}
        aria-label="Switch b/w authentication type"
      >
        <coreicons-shape-refresh class="size-4"></coreicons-shape-refresh>
      </button>
    </div>
  </form>
  <div class="flex hidden items-center gap-2 text-sm">
    <span>Not a member?</span>
    <button class="font-info font-medium">Signup now!</button>
  </div>
  <p class="text-center text-xs">
    By continuing, you agree to the <a
      href="/support/terms-and-conditions"
      class="font-medium text-info">Terms of use</a
    >,
    <a href="/support/privary" class="font-medium text-info">Privacy</a>
    and <a href="/support/policy" class="font-medium text-info">Policy</a> Preplaced.
  </p>
</div>
