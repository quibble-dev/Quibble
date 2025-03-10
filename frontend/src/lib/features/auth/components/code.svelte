<script lang="ts">
  import { cn } from '$lib/functions/classnames';
  import { VerificationCodeSchema } from '$lib/schemas/auth';
  import { onMount } from 'svelte';
  import { defaults, superForm } from 'sveltekit-superforms';
  import { zod } from 'sveltekit-superforms/adapters';

  interface Props {
    email?: string;
    onback: () => void;
  }

  let { onback, email }: Props = $props();

  let countdown = $state(30);
  let is_resend_disabled = $state(true);
  // eslint-disable-next-line no-undef
  let countdown_interval = $state<NodeJS.Timeout>();

  const { form, enhance, errors, delayed } = superForm(defaults(zod(VerificationCodeSchema)), {
    resetForm: false,
    onResult({ result }) {
      if (result.type === 'success') {
        const new_href = email ? `/login?email=${encodeURIComponent(email)}` : `/login`;
        // hard redirect to login page
        window.location.href = new_href;
      }
    }
  });

  function handle_resend_click() {
    start_countdown();
  }

  function start_countdown() {
    is_resend_disabled = true;
    countdown = 30;
    // clear interval (if any)
    clearInterval(countdown_interval);

    countdown_interval = setInterval(() => {
      if (countdown > 0) {
        countdown--;
      } else {
        is_resend_disabled = false;
        clearInterval(countdown_interval);
      }
    }, 1000);
  }

  onMount(() => {
    start_countdown();
    return () => clearInterval(countdown_interval);
  });
</script>

<form class="flex flex-col gap-2" method="POST" action="?/code" use:enhance>
  <div class="flex flex-col gap-1">
    <label class="input input-bordered flex items-center gap-2 bg-transparent pr-2">
      <coreicons-shape-key class="size-4"></coreicons-shape-key>
      <input
        name="code"
        class="grow border-none p-2 text-sm font-medium focus:ring-0"
        placeholder="Verification code*"
        aria-invalid={$errors.code ? 'true' : undefined}
        bind:value={$form.code}
      />
    </label>
    <span class="flex items-center gap-2" class:text-error={$errors.code}>
      {#if $errors.code}
        <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
      {:else}
        <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
      {/if}
      <span class="text-xs">{$errors.code ?? 'You only got 3 attempts!'}</span>
    </span>
  </div>
  <div class="flex flex-col gap-1">
    <div class="flex items-center gap-2 text-xs">
      Didn't get an email?
      <button
        type="button"
        class="btn btn-ghost btn-xs"
        disabled={is_resend_disabled}
        onclick={handle_resend_click}
        >{is_resend_disabled ? `Resend in ${countdown}s` : `Resend`}</button
      >
    </div>
    <div class="flex items-center gap-4">
      <button type="button" class="btn flex-1" aria-label="Back" onclick={onback}>
        <coreicons-shape-arrow variant="left" class="size-4"></coreicons-shape-arrow>
        Back
      </button>
      <button class={cn($delayed && 'btn-active pointer-events-none', 'btn btn-primary flex-1')}>
        Continue
        {#if $delayed}
          <span class="loading loading-spinner loading-xs"></span>
        {:else}
          <coreicons-shape-arrow variant="right" class="size-4"></coreicons-shape-arrow>
        {/if}
      </button>
    </div>
  </div>
</form>
