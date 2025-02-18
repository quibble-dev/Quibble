<script lang="ts">
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import BaseModal from '../_components/base-modal.svelte';

  const modalsStore = createModalsStore();

  function handle_modal_close() {
    modalsStore.close('auth');
  }
</script>

<BaseModal open={modalsStore.state.get('auth') === true} onclose={handle_modal_close}>
  <div class="flex flex-col items-center gap-4">
    <img src="/assets/svgs/quibble-group.svg" alt="Quibble" class="h-24" />
    <div class="flex flex-col gap-2">
      <h3 class="text-xl font-bold text-info">
        Join Quibble to engage with communities, share posts, and more!
      </h3>
      <span class="text-sm">Want to do more? Create an account or log in.</span>
    </div>
    <div class="flex w-full flex-col gap-2">
      <a href="/login" class="btn btn-primary btn-block" onclick={handle_modal_close}>
        Log in
        <coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
      </a>
      <a href="/register" class="btn btn-block" onclick={handle_modal_close}>Sign up</a>
    </div>
    <p class="self-start text-xs">
      By continuing, you agree to the <a
        href="/support/terms-and-conditions"
        class="font-medium text-info underline">Terms of use</a
      >,
      <a href="/support/privary" class="font-medium text-info underline">Privacy</a>
      and <a href="/support/policy" class="font-medium text-info underline">Policy</a> Preplaced.
    </p>
  </div>
  <button
    class="btn btn-square btn-circle btn-ghost btn-sm absolute right-2.5 top-2.5"
    aria-label="Close modal"
    onclick={handle_modal_close}
  >
    <coreicons-shape-x class="size-5" variant="no-border"></coreicons-shape-x>
  </button>
</BaseModal>
