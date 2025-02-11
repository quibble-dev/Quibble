<script lang="ts">
  import QuibbleIcon from '$lib/components/icons/logos/quibble.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { toast } from '$lib/components/ui/toast/toast.svelte';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import { createSidebarStore } from '$lib/stores/sidebar.svelte';
  import { fly } from 'svelte/transition';

  const sidebarStore = createSidebarStore(),
    modalsStore = createModalsStore(),
    authStore = createAuthStore();

  function handle_create_a_communiy_btn_click() {
    if (authStore.state.is_authenticated) {
      modalsStore.open('create_community');
    } else {
      modalsStore.open('auth');
      toast.push('Please login to do this action!', { inside_modal: true });
    }
  }
</script>

<div
  class="fixed flex h-[calc(100dvh-3.75rem)] w-72 flex-col gap-4 overflow-y-scroll border-r border-neutral bg-base-300 p-4 scrollbar-none md:top-[3.75rem] md:z-10"
>
  <div class="flex flex-col gap-2">
    <h2 class="font-medium">Communities</h2>
    <label class="input input-sm input-bordered flex items-center rounded-lg bg-transparent">
      <input
        type="text"
        class="grow border-none pl-0.5 pr-2 text-sm focus:ring-0"
        placeholder="Search filter..."
      />
      <coreicons-shape-filter class="size-3"></coreicons-shape-filter>
    </label>
    <button
      class="btn btn-ghost btn-xs flex w-max items-center gap-2"
      onclick={handle_create_a_communiy_btn_click}
    >
      <coreicons-shape-plus variant="circle" class="size-4"></coreicons-shape-plus>
      <span class="text-xs font-medium">Create a community</span>
    </button>
  </div>
  <div class="collapse gap-2 overflow-visible rounded-none">
    <input type="checkbox" checked={true} class="peer h-max min-h-full w-full" />
    <div
      class="collapse-title flex h-max min-h-max items-center justify-between p-0 text-sm font-medium text-base-content/75 peer-checked:[&>coreicons-shape-chevron]:rotate-180"
    >
      Recent
      <div class="flex items-center gap-2">
        <button
          onclick={sidebarStore.clear_recents}
          class="z-10 rounded-full p-1 px-2 text-xs transition-colors hover:bg-primary/40 hover:text-white"
          >Clear</button
        >
        <coreicons-shape-chevron class="size-4 transition-transform" variant="down"
        ></coreicons-shape-chevron>
      </div>
    </div>
    {#if sidebarStore.state.recent}
      <div class="collapse-content flex flex-col gap-2 !p-0">
        {#each sidebarStore.state.recent as community}
          <div class="flex items-center gap-2" transition:fly={{ y: -15 }}>
            <a href="/q/{community.name}" class="flex">
              <Avatar src={community.avatar} />
            </a>
            <a href="/q/{community.name}" class="text-sm font-medium">q/{community.name}</a>
            <button
              onclick={() => sidebarStore.toggle_star('recent', community.name)}
              class="ml-auto"
              aria-label="Star Community"
            >
              <coreicons-shape-star class="size-4" class:text-primary={community.starred}
              ></coreicons-shape-star>
            </button>
          </div>
        {/each}
      </div>
    {:else}
      <span class="text-sm">Just in—take a peek.</span>
    {/if}
  </div>

  <div class="collapse gap-2 overflow-visible rounded-none">
    <input type="checkbox" checked={true} class="peer h-max min-h-full w-full" />
    <div
      class="collapse-title flex h-max min-h-max items-center justify-between p-0 text-sm font-medium text-base-content/75 peer-checked:[&>coreicons-shape-chevron]:rotate-180"
    >
      Your Communities
      <coreicons-shape-chevron class="size-4 transition-transform" variant="down"
      ></coreicons-shape-chevron>
    </div>
    {#if sidebarStore.state.your}
      <div class="collapse-content flex flex-col gap-2 !p-0">
        {#each sidebarStore.state.your as community}
          <div class="flex items-center gap-2">
            <a href="/q/{community.name}" class="flex">
              <Avatar src={community.avatar} />
            </a>
            <a href="/q/{community.name}" class="text-sm font-medium">q/{community.name}</a>
            <button
              onclick={() => sidebarStore.toggle_star('your', community.name)}
              class="ml-auto"
              aria-label="Star Community"
            >
              <coreicons-shape-star class="size-4" class:text-primary={community.starred}
              ></coreicons-shape-star>
            </button>
          </div>
        {/each}
      </div>
    {:else}
      <span class="text-sm">Ready to quibble? Join in.</span>
    {/if}
  </div>
  <div class="collapse gap-2 overflow-visible rounded-none">
    <input type="checkbox" checked={true} class="peer h-max min-h-full w-full" />
    <div
      class="collapse-title flex h-max min-h-max items-center justify-between p-0 text-sm font-medium text-base-content/75 peer-checked:[&>coreicons-shape-chevron]:rotate-180"
    >
      Resources
      <coreicons-shape-chevron class="size-4 transition-transform" variant="down"
      ></coreicons-shape-chevron>
    </div>
    <div class="collapse-content flex flex-col gap-2 !p-0">
      <a href="/about" class="flex items-center gap-2">
        <QuibbleIcon class="size-4" />
        <span class="text-sm font-medium">About Quibble</span>
      </a>
      <a href="/support/help" class="flex items-center gap-2">
        <coreicons-shape-help-circle class="size-4"></coreicons-shape-help-circle>
        <span class="text-sm font-medium">Help</span>
      </a>
    </div>
  </div>
  <p class="text-xs">Quibble © {new Date().getFullYear()}. All rights reserved.</p>
</div>
