<script lang="ts">
  import { goto } from '$app/navigation';
  import { cn } from '$lib/functions/classnames';
  import { VerificationCodeSchema } from '$lib/schemas/auth';
  import { defaults, superForm } from 'sveltekit-superforms';
  import { zod } from 'sveltekit-superforms/adapters';

  interface Props {
    email?: string;
    onback: () => void;
  }

  let { onback, email }: Props = $props();

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
</script>

<div class="tooltip tooltip-right absolute left-2.5 top-2.5 flex before:capitalize" data-tip="Back">
  <button class="btn btn-square btn-circle btn-ghost btn-sm" aria-label="Back" onclick={onback}>
    <coreicons-shape-arrow class="size-5" variant="left"></coreicons-shape-arrow>
  </button>
</div>

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
    <div class="flex items-center gap-2 self-center text-xs">
      Didn't get an email?
      <button type="button" class="btn btn-ghost btn-xs">Resend</button>
    </div>
    <button class={cn($delayed && 'btn-active pointer-events-none', 'btn btn-primary')}>
      Continue
      {#if $delayed}
        <span class="loading loading-spinner loading-xs"></span>
      {:else}
        <coreicons-shape-arrow variant="right" class="size-4"></coreicons-shape-arrow>
      {/if}
    </button>
  </div>
</form>
