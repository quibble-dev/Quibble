<script lang="ts">
  import { page } from '$app/state';
  import { cn } from '$lib/functions/classnames';
  import { superForm } from 'sveltekit-superforms';

  let { data } = $props();

  const dest_param = page.url.searchParams.get('dest');
  const href_login = dest_param ? `/login?dest=${encodeURIComponent(dest_param)}` : '/login';

  const { form, enhance, delayed, errors, message } = superForm(data.form, {
    resetForm: false
  });
</script>

<!-- site head and seo -->
<svelte:head>
  <title>Register on Quibble</title>
</svelte:head>

<!-- form element: email and password -->
<form method="POST" class="flex flex-col gap-3" use:enhance novalidate>
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
  <span class="text-sm">
    Already a quibbler?
    <a href={href_login} class="font-medium text-accent">Log in</a>
  </span>
  {#if $message}
    <div class="flex items-center gap-2 text-error" class:text-error={$message}>
      <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
      <span class="text-xs">{$message}</span>
    </div>
  {/if}
  <button class={cn($delayed && 'btn-active pointer-events-none', 'btn btn-primary')}>
    Register
    {#if $delayed}
      <span class="loading loading-spinner loading-xs"></span>
    {:else}
      <coreicons-shape-arrow class="size-4" variant="right"></coreicons-shape-arrow>
    {/if}
  </button>
</form>
