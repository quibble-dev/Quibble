<script lang="ts">
  import Quibbles from '$lib/components/icons/logos/quibbles.svelte';
  import BaseModal from '$lib/components/ui/base-modal.svelte';
  import { createModalsStore } from '$lib/stores/modals.svelte';

  const modalsStore = createModalsStore();

  function handle_modal_close() {
    modalsStore.close('auth');
  }
</script>

<BaseModal open={modalsStore.state.get('auth') === true} onclose={handle_modal_close}>
  <div class="flex flex-col items-center gap-4">
    <Quibbles class="h-20 w-auto" />
    <div class="flex flex-col items-center gap-2">
      <h3 class="text-center text-xl font-bold text-info">
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
    <div class="divider my-0 text-xs font-bold">NOTE</div>
    <div class="flex items-center gap-2 self-start text-sm">
      <coreicons-shape-info class="shrink-0"></coreicons-shape-info>
      <span
        >Project is in development, if you see any issues- please <a
          href="https://github.com/quibble-dev/Quibble/issues/new?template=bug_report.yml"
          target="_blank"
          class="font-medium text-info underline">raise a ticket</a
        >.</span
      >
    </div>
  </div>
  <button
    class="btn btn-square btn-circle btn-ghost btn-sm absolute right-2.5 top-2.5"
    aria-label="Close modal"
    onclick={handle_modal_close}
  >
    <coreicons-shape-x class="size-5" variant="no-border"></coreicons-shape-x>
  </button>
</BaseModal>
