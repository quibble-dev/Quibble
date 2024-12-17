<script lang="ts">
  import QuibbleIcon from '$lib/components/icons/logos/quibble.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import favorite_communities from '$lib/data/mock/favorites.json';
  import your_communities from '$lib/data/mock/your_communities.json';
</script>

<div
  class="fixed top-[3.75rem] z-10 flex h-[calc(100dvh-3.75rem)] w-72 flex-col gap-4 overflow-y-scroll border-r border-neutral bg-base-300 p-4 scrollbar-none"
>
  <div class="flex flex-col gap-2">
    <div class="flex items-center gap-2">
      <h2 class="font-medium">Quiblets</h2>
      <div class="tooltip tooltip-right flex" data-tip="Communities">
        <coreicons-shape-help-circle class="size-[0.85rem]"></coreicons-shape-help-circle>
      </div>
    </div>
    <label
      class="input input-sm input-bordered flex items-center rounded-lg bg-transparent"
    >
      <input
        type="text"
        class="grow border-none pl-0.5 pr-2 text-sm focus:ring-0"
        placeholder="Search filter..."
      />
      <coreicons-shape-filter class="size-3"></coreicons-shape-filter>
    </label>
    <button class="flex items-center gap-2">
      <coreicons-shape-plus variant="circle" class="size-4"></coreicons-shape-plus>
      <span class="text-xs font-medium">Create Quiblet</span>
    </button>
  </div>
  <div class="collapse gap-2 rounded-none">
    <input type="checkbox" checked={true} class="peer h-max min-h-full w-full" />
    <div
      class="collapse-title flex h-max min-h-max items-center justify-between p-0 text-sm font-medium text-base-content/75 peer-checked:[&>coreicons-shape-chevron]:rotate-180"
    >
      Favourites
      <coreicons-shape-chevron class="size-4 transition-transform" variant="down"
      ></coreicons-shape-chevron>
    </div>
    <div class="collapse-content flex flex-col gap-2 !p-0">
      {#each favorite_communities as community}
        <div class="flex items-center gap-2">
          <a href="q/{community.name}" class="flex">
            <Avatar src={community.avatar} />
          </a>
          <a href="q/{community.name}" class="text-sm font-medium">q/{community.name}</a>
          <button class="ml-auto" aria-label="Star Community">
            <coreicons-shape-star class="size-4" class:text-primary={community.starred}
            ></coreicons-shape-star>
          </button>
        </div>
      {/each}
    </div>
  </div>
  <div class="collapse gap-2 rounded-none">
    <input type="checkbox" checked={true} class="peer h-max min-h-full w-full" />
    <div
      class="collapse-title flex h-max min-h-max items-center justify-between p-0 text-sm font-medium text-base-content/75 peer-checked:[&>coreicons-shape-chevron]:rotate-180"
    >
      Your Quiblets
      <coreicons-shape-chevron class="size-4 transition-transform" variant="down"
      ></coreicons-shape-chevron>
    </div>
    <div class="collapse-content flex flex-col gap-2 !p-0">
      {#each your_communities as community}
        <div class="flex items-center gap-2">
          <a href="q/{community.name}" class="flex">
            <Avatar src={community.avatar} />
          </a>
          <a href="q/{community.name}" class="text-sm font-medium">q/{community.name}</a>
          <button class="ml-auto" aria-label="Star Community">
            <coreicons-shape-star class="size-4" class:text-primary={community.starred}
            ></coreicons-shape-star>
          </button>
        </div>
      {/each}
    </div>
  </div>
  <div class="collapse gap-2 rounded-none">
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
