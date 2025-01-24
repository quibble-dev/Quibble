<script lang="ts">
  import { enhance } from '$app/forms';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
  import ZodErrors from '$lib/components/shared/zod-errors.svelte';
  import { cn } from '$lib/functions/classnames';
  import type { FormProps } from '../../types';
  import forms from '../forms';
  import type { SubmitFunction } from '@sveltejs/kit';
  import type { ZodIssue } from 'zod';

  let { forms_state, update_forms_state, goto_form }: FormProps<typeof forms> = $props();

  let errors = $state<ZodIssue[]>();
  // for single errors
  let error = $state<string>();
  let pending = $state(false);

  let invalid_username = $derived(
    Boolean(error || errors?.some((err) => err.path.includes('username')))
  );

  const handle_submit: SubmitFunction = async () => {
    pending = true;

    return async ({ result }) => {
      if (result.type === 'success') {
        errors = undefined;
        // append to existing profiles on forms_state
        update_forms_state('profile_select', {
          profiles: [
            ...(forms_state.profile_select as { profiles: object[] }).profiles,
            result.data
          ]
        });
        goto_form('profile_select');
      } else if (result.type === 'failure') {
        // cleanup errors for fresh assigning
        errors = undefined;
        error = undefined;
        // authentication error
        if (result.status === 401) {
          error = result.data?.error;
        } else {
          // zod errors
          errors = result.data?.errors;
        }
      }
      pending = false;
    };
  };
</script>

<div class="flex flex-col gap-4">
  <div class="flex flex-col items-center justify-center gap-1">
    <div class="mb-3 flex items-center gap-2">
      <QuibbleLogo class="size-7" />
      <QuibbleTextLogo class="h-7 w-auto" />
    </div>
    <p class="text-center font-medium">Let's create new one!</p>
    <p class="text-center text-xs">You can edit this profile from settings page later.</p>
  </div>
  <form
    method="POST"
    action="/settings/profile?/create"
    use:enhance={handle_submit}
    class="flex flex-col gap-3"
    novalidate
  >
    <label
      class="input input-bordered flex items-center gap-2"
      class:input-error={invalid_username}
    >
      <coreicons-shape-at-sign class="size-4"></coreicons-shape-at-sign>
      <input
        type="text"
        name="username"
        required
        minlength="3"
        class="grow border-none p-2 text-sm font-medium focus:ring-0"
        placeholder="Username*"
      />
    </label>
    {#if errors}
      <ZodErrors {errors} />
    {:else}
      <div class="flex items-center gap-2" class:text-error={error !== undefined}>
        <coreicons-shape-info class="size-3"></coreicons-shape-info>
        <span class="text-xs">
          {error ?? 'Hint: Make it epic—you only get 3!'}
        </span>
      </div>
    {/if}
    <button
      type="submit"
      class={cn(pending && 'btn-active pointer-events-none', 'btn btn-primary')}
    >
      {#if pending}
        Creating
        <span class="loading loading-spinner loading-xs"></span>
      {:else}
        Create profile
        <coreicons-shape-arrow variant="right" class="size-4"></coreicons-shape-arrow>
      {/if}
    </button>
  </form>
</div>
