<script lang="ts">
  import Quib from '$lib/components/quib.svelte';
  import QuibsHeader from '$lib/components/quibs_header.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { cn } from '$lib/functions/classnames';
  import { FormatDate } from '$lib/functions/date';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import { createSidebarStore } from '$lib/stores/sidebar.svelte';
  import type { PageData } from './$types';
  import { onMount } from 'svelte';

  const { data }: { data: PageData } = $props();
  const { quiblet, quibs, highlighted_quibs } = data;

  const authStore = createAuthStore(),
    sidebarStore = createSidebarStore();

  const is_joined = $derived.by(() => {
    if (!authStore.state.is_authenticated) return false;
    if (authStore.state.profile && quiblet) {
      return quiblet.members?.includes(authStore.state.profile.id);
    }
  });

  function add_to_sidebar_store(key: string) {
    sidebarStore.add_quiblet(key, {
      avatar: quiblet.avatar,
      name: quiblet.name
    });
  }

  onMount(() => {
    add_to_sidebar_store('recent');
    if (is_joined) add_to_sidebar_store('your');
  });
</script>

<svelte:head>
  <title>q/{quiblet?.name}</title>
</svelte:head>

<div class="relative">
  <!-- show quiblet cover if not null or solid bg -->
  <div
    class={cn(
      !quiblet?.banner ? 'h-24 bg-neutral' : 'h-40 bg-cover bg-center',
      'w-full rounded-2xl'
    )}
    style="background-image: url({quiblet?.banner});"
  ></div>
  <div class="absolute inset-x-0 -bottom-12 flex items-end justify-between px-4">
    <div class="flex items-end gap-2">
      <Avatar
        class="size-20 rounded-full outline outline-8 outline-base-300"
        src={quiblet?.avatar}
      />
      <h3 class="text-2xl font-bold text-info">q/{quiblet?.name}</h3>
    </div>
    <!-- quiblet basic operations -->
    <div class="flex items-center gap-2">
      <button class="btn btn-primary h-10 px-3" aria-label="Create a Post">
        <coreicons-shape-plus variant="no-border" class="size-5"></coreicons-shape-plus>
        <span class="text-sm font-medium">Create Quib</span>
      </button>
      <button class="btn btn-secondary h-10 px-3" aria-label="Join quiblet">
        <span class="text-sm font-medium">{is_joined ? 'Joined' : 'Join'}</span>
      </button>
      <button class="btn btn-neutral size-10 p-0" aria-label="More options">
        <coreicons-shape-more class="size-5 rotate-90"></coreicons-shape-more>
      </button>
    </div>
  </div>
</div>
<div class="h-12"></div>
<QuibsHeader />
<!-- list highlighted quibs if exists -->
{#if highlighted_quibs?.length}
  <div class="flex flex-col gap-4">
    <div class="flex items-center gap-2">
      <coreicons-shape-hash class="size-5"></coreicons-shape-hash>
      <h4 class="font-medium">Highlights</h4>
    </div>
    <div class="grid grid-cols-3 gap-4">
      {#each highlighted_quibs as quib}
        <div
          class="relative flex h-40 flex-col gap-2 overflow-hidden rounded-2xl border border-neutral p-2 transition-colors hover:bg-base-200"
        >
          <div
            class="flex-1 rounded-xl bg-cover bg-center inner-border
            inner-border-base-content/15"
            class:bg-base-100={!quib.cover}
            style="background-image: url({quib.cover});"
          ></div>
          <div class="flex flex-col p-2 pt-0.5">
            <h4 class="line-clamp-1 font-medium">{quib.title}</h4>
            <span class="text-xs font-medium text-base-content/75"
              >{new FormatDate(quib.created_at).format()}</span
            >
          </div>
          <a
            href="./{quiblet?.name}/quibs/{quib.id}/{quib.slug}"
            class="absolute inset-0"
            aria-label={quib.title}
          ></a>
        </div>
      {/each}
    </div>
  </div>
{/if}
<!-- list quibs -->
{#if quibs}
  {#each quibs as quib}
    <Quib {...quib} />
  {/each}
{/if}
