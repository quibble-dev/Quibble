<script lang="ts">
  import ChartBarsIcon from '$lib/components/icons/chart_bars.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
  import NotificationIcon from '$lib/components/icons/notification.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import { createAuthStore } from '$lib/stores/auth.svelte';

  const modalsStore = createModalsStore(),
    authStore = createAuthStore();
</script>

<header
  class="fixed top-0 z-20 flex h-[3.75rem] w-full items-center justify-between border-b border-neutral bg-base-300 px-4"
>
  <a href="/" aria-label="Quibble Home" class="flex items-center gap-2">
    <QuibbleLogo class="size-7" />
    <QuibbleTextLogo class="h-7 w-auto" />
  </a>
  <div class="hidden items-center gap-5 md:flex">
    <div class="flex gap-2">
      <a href="/" aria-label="Home" class="flex items-center gap-2">
        <coreicons-shape-home class="size-5 text-primary"></coreicons-shape-home>
        <span class="text-sm font-medium">Home</span>
      </a>
      <a href="/q/popular" aria-label="Popular Quibbles" class="flex items-center gap-2">
        <ChartBarsIcon variant="popular" class="size-5" />
        <span class="text-sm font-medium">Popular</span>
      </a>
      <a href="/q/all" aria-label="All Quibbles" class="flex items-center gap-2">
        <ChartBarsIcon variant="all" class="size-5" />
        <span class="text-sm font-medium">All</span>
      </a>
    </div>
    <label class="input input-bordered flex h-10 w-96 items-center bg-transparent px-3">
      <coreicons-shape-search class="size-5"></coreicons-shape-search>
      <input
        type="text"
        class="grow border-none text-sm font-medium focus:ring-0"
        placeholder="Search..."
      />
    </label>
  </div>
  <div class="flex items-center gap-2">
    {#if authStore.state.is_authenticated}
      <div class="tooltip tooltip-bottom" data-tip="Create a Quib">
        <button aria-label="Create a Post" class="btn btn-primary h-10 px-3">
          <coreicons-shape-plus variant="no-border" class="size-5"></coreicons-shape-plus>
          <span class="text-sm font-medium">Create</span>
        </button>
      </div>
      <div class="tooltip tooltip-bottom" data-tip="Inbox">
        <button aria-label="Inbox" class="btn btn-neutral size-10 p-0">
          <NotificationIcon class="size-6" />
        </button>
      </div>
      <div class="tooltip tooltip-bottom flex before:left-0" data-tip="Profile menu">
        <Avatar
          class="btn !size-10 rounded-btn p-0"
          src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
        />
      </div>
    {:else}
      <button
        class="btn btn-primary h-10 px-3 text-sm font-bold"
        onclick={() => modalsStore.open('auth')}
      >
        Join In!
        <coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
      </button>
    {/if}
  </div>
</header>
