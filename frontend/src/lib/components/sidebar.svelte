<script lang="ts">
  import QuibbleIcon from '$lib/components/icons/logos/quibble.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { emoticons } from '$lib/constants/emoticons';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import { createSidebarStore } from '$lib/stores/sidebar.svelte';

  const sidebarStore = createSidebarStore(),
    modalsStore = createModalsStore(),
    authStore = createAuthStore();

  function handle_create_a_communiy_btn_click(e: MouseEvent) {
    if (!authStore.state.is_authenticated) {
      e.preventDefault();
      modalsStore.open('auth');
    }
  }
</script>

<div
  class="border-neutral bg-base-300 scrollbar-none fixed flex h-[calc(100dvh-3.75rem)] w-72 flex-col gap-4 overflow-y-scroll border-r p-4 md:top-[3.75rem] md:z-10"
>
  <div class="flex flex-col gap-2">
    <h2 class="font-medium">Communities</h2>
    <label class="input input-sm input-bordered flex items-center rounded-lg bg-transparent">
      <input
        type="text"
        class="grow border-none pr-2 pl-0.5 text-sm focus:ring-0"
        placeholder="Search filter..."
      />
      <coreicons-shape-filter class="size-3"></coreicons-shape-filter>
    </label>
    <a
      href="/q/create"
      class="btn btn-ghost btn-xs flex w-max items-center gap-2"
      onclick={handle_create_a_communiy_btn_click}
    >
      <coreicons-shape-plus variant="circle" class="size-4"></coreicons-shape-plus>
      <span class="text-xs font-medium">Create a community</span>
    </a>
  </div>
  <div class="collapse gap-2 overflow-visible rounded-none">
    <input type="checkbox" checked={true} class="peer h-max min-h-full w-full" />
    <div
      class="collapse-title text-base-content/75 flex h-max min-h-max items-center justify-between p-0 text-sm font-medium [&>div>coreicons-shape-chevron]:peer-checked:rotate-180"
    >
      Recent
      <div class="flex items-center gap-2">
        <button
          class="btn btn-ghost btn-xs z-10"
          disabled={sidebarStore.state.recent?.length === 0}
          onclick={() => sidebarStore.clear('recent')}>Clear</button
        >
        <coreicons-shape-chevron class="size-4 transition-transform" variant="down"
        ></coreicons-shape-chevron>
      </div>
    </div>
    {#if sidebarStore.state.recent?.length}
      <div class="collapse-content flex flex-col gap-2 p-0!">
        {#each sidebarStore.state.recent as community (community.id)}
          <div class="flex items-center gap-2">
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
      <span class="text-sm">{emoticons.SUSPICIOUS} Just in—take a peek.</span>
    {/if}
  </div>

  <div class="collapse gap-2 overflow-visible rounded-none">
    <input type="checkbox" checked={true} class="peer h-max min-h-full w-full" />
    <div
      class="collapse-title text-base-content/75 flex h-max min-h-max items-center justify-between p-0 text-sm font-medium [&>div>coreicons-shape-chevron]:peer-checked:rotate-180"
    >
      Your Communities
      <div class="flex items-center gap-2">
        <button
          class="btn btn-ghost btn-xs z-10"
          disabled={sidebarStore.state.your?.length === 0}
          onclick={() => sidebarStore.clear('your')}>Clear</button
        >
        <coreicons-shape-chevron class="size-4 transition-transform" variant="down"
        ></coreicons-shape-chevron>
      </div>
    </div>
    {#if sidebarStore.state.your?.length}
      <div class="collapse-content flex flex-col gap-2 p-0!">
        {#each sidebarStore.state.your as community (community.id)}
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
      <span class="text-sm">{emoticons.SHY} Ready to quibble? Join in.</span>
    {/if}
  </div>
  <div class="collapse gap-2 overflow-visible rounded-none">
    <input type="checkbox" checked={true} class="peer h-max min-h-full w-full" />
    <div
      class="collapse-title text-base-content/75 flex h-max min-h-max items-center justify-between p-0 text-sm font-medium [&>coreicons-shape-chevron]:peer-checked:rotate-180"
    >
      Resources
      <coreicons-shape-chevron class="size-4 transition-transform" variant="down"
      ></coreicons-shape-chevron>
    </div>
    <div class="collapse-content flex flex-col gap-2 p-0!">
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
