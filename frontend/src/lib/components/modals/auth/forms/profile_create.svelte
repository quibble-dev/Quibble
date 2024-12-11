<script lang="ts">
  import { deserialize } from '$app/forms';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
  import { cn } from '$lib/functions/classnames';
  import type { ActionResult } from '@sveltejs/kit';
  import type { FormProps } from '../types';

  let { goto_form }: FormProps = $props();

  let errors = $state<Record<string, string> | undefined>();
  let pending = $state(false);

  async function handle_submit(e: SubmitEvent) {
    e.preventDefault();
    pending = true;

    try {
      const form = e.currentTarget as HTMLFormElement;
      const form_data = new FormData(form);

      const response = await fetch(form.action, {
        method: form.method,
        body: form_data
      });

      const result: ActionResult = deserialize(await response.text());

      if (result.type === 'success') {
        errors = undefined;
        goto_form('profile_select');
      } else if (result.type === 'failure') {
        errors = result.data;
      }
    } catch (err) {
      console.error(err);
    } finally {
      pending = false;
    }
  }
</script>

<div class="flex flex-col gap-4">
  <div class="flex flex-col items-center justify-center gap-4">
    <div class="flex items-center gap-2">
      <QuibbleLogo class="size-7" />
      <QuibbleTextLogo class="h-7 w-auto" />
    </div>
    <p class="text-center font-medium">Let's create new one!</p>
  </div>
  <form
    method="POST"
    action="/settings/profile?/create"
    onsubmit={handle_submit}
    class="flex flex-col gap-3"
  >
    <label class="input input-bordered flex items-center gap-2">
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
    {#if errors?.detail}
      <div class="flex items-center gap-2">
        <coreicons-shape-alert-triangle class="size-3 text-error"></coreicons-shape-alert-triangle>
        <span class="text-xs text-error first-letter:uppercase">{errors.detail}</span>
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
        <coreicons-shape-chevron variant="right" class="size-4"></coreicons-shape-chevron>
      {/if}
    </button>
  </form>
  <p class="text-center text-xs">You can do more things from settings page later.</p>
</div>
