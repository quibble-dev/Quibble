<script lang="ts">
  import { goto } from '$app/navigation';
  import { page } from '$app/state';
  import api from '$lib/api';
  import { toast } from '$lib/components/ui/toast';
  import { cn } from '$lib/functions/classnames';
  import type { Data } from '../+layout.svelte';
  import { getContext, untrack } from 'svelte';
  import { superForm } from 'sveltekit-superforms';

  let { data } = $props();

  let show_password = $state(false);

  const dest_param = page.url.searchParams.get('dest');
  const href_register = dest_param
    ? `/register?dest=${encodeURIComponent(dest_param)}`
    : '/register?ref=auth_page';

  const handle_success: (data: Data) => void = getContext('handle_success');

  const { form, enhance, submitting, errors, message } = superForm(data.form, {
    resetForm: false,
    async onResult({ result }) {
      // if e-mail address is not verified
      if (
        result.type === 'failure' &&
        result.data &&
        result.data.form.message.includes('not verified')
      ) {
        const email = result.data.form.data.email;
        const { response } = await api.POST('/auth/registration/resend-email/', {
          body: { email }
        });
        if (response.ok) goto(`/verification?email=${email}`);
      } else if (result.type === 'success') {
        const { data } = await api.GET('/u/me/profiles/total-count/');
        // if no profiles- show creation form, otherwise- show selection
        const type: Data['type'] = data && data.total_count > 0 ? 'select' : 'create';
        handle_success({ type });
      }
    }
  });

  $effect(() => {
    const _message = $message;
    if (_message) untrack(() => toast.push(_message));
  });
</script>

<!-- site head and seo -->
<svelte:head>
  <title>Log in to Quibble</title>
</svelte:head>

<!-- form element: email and password -->
<form method="POST" action="?/login" class="flex flex-col gap-2" use:enhance novalidate>
  <!-- email input field with errors store -->
  <div class="flex flex-col gap-1">
    <label class="floating-label">
      <span class="bg-base-300! duration-100!">E-mail address*</span>
      <div class="input w-full bg-transparent" class:input-error={$errors.email}>
        <coreicons-shape-mail class="size-4 shrink-0 opacity-50"></coreicons-shape-mail>
        <input
          type="email"
          name="email"
          placeholder="E-mail address*"
          aria-invalid={$errors.email ? 'true' : undefined}
          bind:value={$form.email}
        />
      </div>
    </label>
    {#if $errors.email}
      <span class="text-error flex items-center gap-2 text-xs">{$errors.email[0]}</span>
    {/if}
  </div>
  <!-- password input field with errors store -->
  <div class="flex flex-col gap-1">
    <label class="floating-label">
      <span class="bg-base-300! duration-100!">Password*</span>
      <div class="input w-full bg-transparent" class:input-error={$errors.password}>
        <coreicons-shape-lock class="size-4 shrink-0 opacity-50"></coreicons-shape-lock>
        <input
          type={show_password ? 'text' : 'password'}
          name="password"
          placeholder="Password*"
          aria-invalid={$errors.password ? 'true' : undefined}
          bind:value={$form.password}
        />
      </div>
    </label>
    {#if $errors.password}
      <span class="text-error flex items-center gap-2 text-xs">{$errors.password[0]}</span>
    {/if}
  </div>
  <div class="flex items-center justify-between gap-1">
    <label class="flex items-center gap-2">
      <input
        type="checkbox"
        class="checkbox checkbox-sm"
        onchange={() => (show_password = !show_password)}
      />
      <span class="cursor-pointer text-sm">Show password</span>
    </label>
    <a href="/password" tabindex="-1" class="text-accent text-sm">Forgot password?</a>
  </div>
  <div class="flex flex-col items-center gap-2">
    <button class={cn($submitting && 'btn-active pointer-events-none', 'btn btn-primary w-full')}>
      Log in
      {#if $submitting}
        <span class="loading loading-spinner loading-xs"></span>
      {:else}
        <coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
      {/if}
    </button>
    <a href={href_register} class="btn w-full">New? Sign up now!</a>
  </div>
</form>
