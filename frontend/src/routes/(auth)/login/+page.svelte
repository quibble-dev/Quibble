<script lang="ts">
  import { page } from '$app/state';
  import api from '$lib/api';
  import { cn } from '$lib/functions/classnames';
  import type { LoginData } from '../+layout.svelte';
  import { getContext } from 'svelte';
  import { superForm } from 'sveltekit-superforms';

  let { data } = $props();

  const dest_param = page.url.searchParams.get('dest');
  const href_register = dest_param
    ? `/register?dest=${encodeURIComponent(dest_param)}`
    : '/register';

  const handle_login_success: (data: LoginData) => void = getContext('handle_login_success');

  const { form, enhance, delayed, errors, message } = superForm(data.form, {
    resetForm: false,
    async onResult({ result }) {
      if (result.type === 'success') {
        const { data } = await api.GET('/u/me/profiles/total-count/');
        // if no profiles- show creation form, otherwise- show selection
        const type: LoginData['type'] = data && data.total_count > 0 ? 'select' : 'create';
        handle_login_success({ type });
      }
    }
  });
</script>

<!-- site head and seo -->
<svelte:head>
  <title>Log in to Quibble</title>
</svelte:head>

<!-- form element: email and password -->
<form method="POST" action="?/login" class="flex flex-col gap-3" use:enhance novalidate>
  <!-- email input field with errors store -->
  <div class="flex flex-col gap-1">
    <label class="input input-bordered flex items-center gap-2 bg-transparent">
      <coreicons-shape-mail class="size-4"></coreicons-shape-mail>
      <input
        type="email"
        name="email"
        class="grow border-none p-2 text-sm font-medium focus:ring-0"
        placeholder="Email address*"
        aria-invalid={$errors.email ? 'true' : undefined}
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
  <!-- password input field with errors store -->
  <div class="flex flex-col gap-1">
    <label class="input input-bordered flex items-center gap-2 bg-transparent pr-2">
      <coreicons-shape-lock class="size-4"></coreicons-shape-lock>
      <input
        type="password"
        name="password"
        class="grow border-none p-2 text-sm font-medium focus:ring-0"
        placeholder="Password*"
        aria-invalid={$errors.password ? 'true' : undefined}
        bind:value={$form.password}
      />
      <button
        type="button"
        class="btn btn-square btn-ghost btn-sm ml-auto border border-base-content/25 bg-transparent"
        aria-label="Show/hide password"
      >
        <coreicons-shape-eye class="size-4" variant="open"></coreicons-shape-eye>
      </button>
    </label>
    {#if $errors.password}
      <span class="flex items-center gap-2 text-error">
        <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
        <span class="text-xs">{$errors.password}</span>
      </span>
    {/if}
  </div>
  <div class="flex items-center justify-between gap-1">
    <span class="text-sm">
      New to Quibble?
      <a href={href_register} class="font-medium text-accent">Sign up</a>
    </span>
    <a href="/password" class="text-sm text-accent">Forgot password?</a>
  </div>
  {#if $message}
    <div class="flex items-center gap-2 text-error" class:text-error={$message}>
      <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
      <span class="text-xs">{$message}</span>
    </div>
  {/if}
  <button class={cn($delayed && 'btn-active pointer-events-none', 'btn btn-primary')}>
    Log in
    {#if $delayed}
      <span class="loading loading-spinner loading-xs"></span>
    {:else}
      <coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
    {/if}
  </button>
</form>
