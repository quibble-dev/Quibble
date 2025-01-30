<script lang="ts">
  import { page } from '$app/state';
  import GoogleLogo from '$lib/components/icons/logos/google.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble-text.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import { cn } from '$lib/functions/classnames';
  import { JoinSchema } from '$lib/schemas/auth';
  import type { FormProps } from '../../types';
  import forms from '../forms';
  import type { HTMLInputAttributes } from 'svelte/elements';
  import { superForm } from 'sveltekit-superforms';
  import { zod } from 'sveltekit-superforms/adapters';

  let {}: FormProps<typeof forms> = $props();

  const { form, enhance, errors } = superForm(page.data.form_join, {
    resetForm: false,
    validators: zod(JoinSchema),
    onUpdate({ form }) {
      console.log(form);
    }
  });

  let auth_type = $state<'login' | 'register'>('login');
  let password_type = $state<HTMLInputAttributes['type']>('password');

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
    use:enhance
    class="flex flex-col gap-3"
    novalidate
  >
    <div class="flex flex-col gap-1">
      <label class="input input-bordered flex items-center gap-2 bg-transparent">
        <coreicons-shape-mail class="size-4"></coreicons-shape-mail>
        <input
          type="email"
          name="email"
          class="grow border-none p-2 text-sm font-medium focus:ring-0"
          placeholder="Email address*"
          bind:value={$form.email}
        />
      </label>
      {#if $errors.email}
        <span class="flex items-center gap-2 text-error">
          <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
          <span class="text-xs">{$errors.email}</span>
        </span>
      {/if}
    </div>
    <div class="flex flex-col gap-1">
      <label class="input input-bordered flex items-center gap-2 bg-transparent pr-2">
        <coreicons-shape-lock class="size-4"></coreicons-shape-lock>
        <input
          type={password_type}
          name="password"
          class="grow border-none p-2 text-sm font-medium focus:ring-0"
          placeholder="Password*"
          bind:value={$form.password}
        />
        <button
          type="button"
          class="btn btn-square btn-ghost btn-sm ml-auto border border-base-content/25 bg-transparent"
          class:btn-active={password_type === 'text'}
          aria-label="Show/hide password"
          onclick={handle_toggle_password_type}
        >
          <coreicons-shape-eye
            class="size-4"
            variant={password_type === 'password' ? 'open' : 'close'}
          ></coreicons-shape-eye>
        </button>
      </label>
      {#if $errors.password}
        <span class="flex items-center gap-2 text-error">
          <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
          <span class="text-xs">{$errors.password}</span>
        </span>
      {/if}
    </div>
    <div class="flex items-center gap-2">
      <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
      <span class="text-xs">Hint: you can switch b/w 'login' and 'register'.</span>
    </div>
    <div class="flex items-center gap-3">
      <button
        type="submit"
        class={cn(false && 'btn-active pointer-events-none', 'btn btn-primary flex-1')}
      >
        <!-- {#if pending} -->
        <!--   {auth_type === 'login' ? 'Logging in' : 'Registering'} -->
        <!--   <span class="loading loading-spinner loading-xs"></span> -->
        <!-- {:else} -->
        {auth_type === 'login' ? 'Log in' : 'Register'}
        <coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
        <!-- {/if} -->
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
