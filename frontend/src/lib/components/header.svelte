<script lang="ts">
  import { page } from '$app/stores';
  import ChartBarsIcon from '$lib/components/icons/chart_bars.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
  import NotificationIcon from '$lib/components/icons/notification.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import { createModalsStore } from '$lib/stores/modals.svelte';

  type Props = {
    on_menu_click?: () => void;
  };

  let { on_menu_click }: Props = $props();

  const show_search_in_quiblet = $derived.by(
    () => $page.url.pathname.includes('/q/') && $page.data.quiblet
  );

  const modalsStore = createModalsStore(),
    authStore = createAuthStore();
</script>

<header
  class="fixed top-0 z-20 flex h-[3.75rem] w-full items-center justify-between border-b border-neutral bg-base-300 px-4"
>
  <div class="flex items-center gap-4">
    <button
      onclick={on_menu_click}
      class="btn border-none !bg-transparent p-0 md:hidden"
      aria-label="open up sidebar"
    >
      <coreicons-shape-list class="size-5"></coreicons-shape-list>
    </button>
    <a href="/" aria-label="Quibble Home" class="flex items-center gap-2">
      <QuibbleLogo class="size-7" />
      <QuibbleTextLogo class="hidden h-7 w-auto md:flex" />
    </a>
  </div>
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
    <label
      class="input input-bordered relative flex h-10 w-96 items-center bg-transparent px-3"
    >
      <coreicons-shape-search class="size-5"></coreicons-shape-search>
      {#if show_search_in_quiblet}
        <div
          class="ml-2 flex items-center gap-2 rounded-lg border border-neutral bg-base-100 p-1 px-1.5"
        >
          <Avatar src={$page.data.quiblet.avatar} class="size-5 rounded-full" />
          <h5 class="whitespace-nowrap text-xs font-medium">q/{$page.data.quiblet.name}</h5>
        </div>
      {/if}
      <input
        type="text"
        class="grow border-none text-sm font-medium focus:ring-0"
        placeholder={show_search_in_quiblet
          ? `Search in q/${$page.params.name}`
          : 'Search...'}
      />
    </label>
  </div>
  <div class="flex items-center gap-2">
    <button aria-label="Expand search" class="btn size-10 p-0 md:hidden">
      <coreicons-shape-search variant="no-border" class="size-5"></coreicons-shape-search>
    </button>
    {#if authStore.state.is_authenticated}
      <div class="tooltip tooltip-bottom" data-tip="Create a Quib">
        <button
          aria-label="Create a Post"
          class="btn h-10 w-10 p-0 md:btn-primary md:w-auto md:px-3"
        >
          <coreicons-shape-plus variant="no-border" class="size-5"></coreicons-shape-plus>
          <span class="hidden text-sm font-medium md:flex">Create</span>
        </button>
      </div>
      <div class="tooltip tooltip-bottom" data-tip="Inbox">
        <button aria-label="Inbox" class="btn btn-neutral size-10 p-0">
          <NotificationIcon class="size-6" />
        </button>
      </div>
      <div class="tooltip tooltip-bottom flex before:left-0" data-tip="Profile menu">
        <Avatar
          class="btn btn-neutral size-10 rounded-btn p-0"
          src={authStore.state.profile?.avatar}
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
