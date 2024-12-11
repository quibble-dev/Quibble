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
    <h2 class="font-semibold">Communities</h2>
    <label class="input input-sm input-bordered flex items-center rounded-lg bg-transparent">
      <input
        type="text"
        class="grow border-none pl-0.5 pr-2 text-sm focus:ring-0"
        placeholder="Search"
      />
      <coreicons-shape-filter class="size-3"></coreicons-shape-filter>
    </label>
    <button class="flex items-center gap-2">
      <coreicons-shape-plus variant="circle" class="size-4"></coreicons-shape-plus>
      <span class="text-xs font-medium">Create Community</span>
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
            <Avatar src={community.avatar} alt={community.name} />
          </a>
          <a href="q/{community.name}" class="text-sm font-semibold">q/{community.name}</a>
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
      Your Communities
      <coreicons-shape-chevron class="size-4 transition-transform" variant="down"
      ></coreicons-shape-chevron>
    </div>
    <div class="collapse-content flex flex-col gap-2 !p-0">
      {#each your_communities as community}
        <div class="flex items-center gap-2">
          <a href="q/{community.name}" class="flex">
            <Avatar src={community.avatar} alt={community.name} />
          </a>
          <a href="q/{community.name}" class="text-sm font-semibold">q/{community.name}</a>
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
        <span class="text-sm font-semibold">About Quibble</span>
      </a>
      <a href="/support/help" class="flex items-center gap-2">
        <coreicons-shape-help-circle class="size-4"></coreicons-shape-help-circle>
        <span class="text-sm font-semibold">Help</span>
      </a>
    </div>
  </div>
  <p class="text-xs">Quibble © {new Date().getFullYear()}. All rights reserved.</p>
</div>
