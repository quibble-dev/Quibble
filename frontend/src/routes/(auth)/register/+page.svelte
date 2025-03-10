<script lang="ts">
  import { page } from '$app/state';
  import { toast } from '$lib/components/ui/toast';
  import { cn } from '$lib/functions/classnames';
  import type { Data } from '../+layout.svelte';
  import { getContext, untrack } from 'svelte';
  import { superForm } from 'sveltekit-superforms';

  let { data } = $props();

  const dest_param = page.url.searchParams.get('dest');
  const href_login = dest_param ? `/login?dest=${encodeURIComponent(dest_param)}` : '/login';

  const handle_success: (data: Data) => void = getContext('handle_success');

  const { form, enhance, delayed, errors, message } = superForm(data.form, {
    resetForm: false,
    onResult({ result }) {
      if (result.type === 'success' && result.data) {
        handle_success({ type: 'code', email: result.data.form.data.email });
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
  <title>Register on Quibble</title>
</svelte:head>

<!-- form element: email and password -->
<form method="POST" action="?/register" class="flex flex-col gap-2" use:enhance novalidate>
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
      <span class="text-error flex items-center gap-2">
        <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
        <span class="text-xs">{$errors.email}</span>
      </span>
    {/if}
  </div>
  <div class="flex flex-col gap-1">
    <label class="floating-label">
      <span class="bg-base-300! duration-100!">Password*</span>
      <div class="input w-full bg-transparent" class:input-error={$errors.password1}>
        <coreicons-shape-lock class="size-4 shrink-0 opacity-50"></coreicons-shape-lock>
        <input
          type="password"
          name="password1"
          placeholder="Password*"
          aria-invalid={$errors.password1 ? 'true' : undefined}
          bind:value={$form.password1}
        />
      </div>
    </label>
    {#if $errors.password1}
      <span class="text-error flex items-center gap-2">
        <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
        <span class="text-xs">{$errors.password1}</span>
      </span>
    {/if}
  </div>
  <div class="flex flex-col gap-1">
    <label class="floating-label">
      <span class="bg-base-300! duration-100!">Confirm password*</span>
      <div class="input w-full bg-transparent" class:input-error={$errors.password2}>
        <coreicons-shape-lock class="size-4 shrink-0 opacity-50"></coreicons-shape-lock>
        <input
          type="password"
          name="password2"
          placeholder="Confirm password*"
          aria-invalid={$errors.password2 ? 'true' : undefined}
          bind:value={$form.password2}
        />
      </div>
    </label>
    {#if $errors.password2}
      <span class="text-error flex items-center gap-2">
        <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
        <span class="text-xs">{$errors.password2}</span>
      </span>
    {/if}
  </div>
  <div class="flex flex-col items-center gap-2">
    <button class={cn($delayed && 'btn-active pointer-events-none', 'btn btn-primary w-full')}>
      Register
      {#if $delayed}
        <span class="loading loading-spinner loading-xs"></span>
      {:else}
        <coreicons-shape-arrow class="size-4" variant="right"></coreicons-shape-arrow>
      {/if}
    </button>
    <a href="/login?ref=auth-page" class="btn w-full">Already? Log in now!</a>
  </div>
</form>
