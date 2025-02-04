<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { PostCard, PostsHeader } from '$lib/features/posts';
  import { cn } from '$lib/functions/classnames';
  import { FormatDate } from '$lib/functions/date';
  import { pluralize } from '$lib/functions/pluralize';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import { createSidebarStore } from '$lib/stores/sidebar.svelte';
  import type { PageData } from './$types';
  import { onMount } from 'svelte';

  const { data }: { data: PageData } = $props();
  const { community, posts, highlighted_posts } = $derived(data);

  const authStore = createAuthStore(),
    sidebarStore = createSidebarStore();

  const is_joined = $derived.by(() => {
    if (!authStore.state.is_authenticated) return false;
    if (authStore.state.profile && community) {
      return community.members?.includes(authStore.state.profile.id);
    }
  });

  function add_to_sidebar_store(key: string) {
    sidebarStore.add_community(key, {
      avatar: community.avatar,
      name: community.name
    });
  }

  onMount(() => {
    add_to_sidebar_store('recent');
    if (is_joined) add_to_sidebar_store('your');
  });
</script>

<svelte:head>
  <title>q/{community?.name}</title>
</svelte:head>

<div class="relative">
  <!-- show community cover if not null or solid bg -->
  <div
    class={cn(
      !community?.banner ? 'h-24 bg-neutral' : 'h-24 bg-cover bg-center md:h-40',
      'w-full rounded-2xl'
    )}
    style="background-image: url({community?.banner});"
  ></div>
  <div
    class="inset-x-0 -bottom-12 flex flex-col justify-between gap-4 md:absolute md:flex-row md:items-end md:px-4"
  >
    <div class="mt-4 flex items-center gap-2 md:mt-0 md:items-end">
      <Avatar
        class="size-14 flex-shrink-0 rounded-full outline-8 outline-base-300 md:size-20 md:outline"
        src={community?.avatar}
      />
      <div class="flex flex-col">
        <h3 class="text-xl font-bold text-info md:text-2xl">q/{community?.name}</h3>
        <div class="flex items-center gap-2 md:hidden">
          <div class="flex items-center gap-1">
            <span class="text-sm text-info">{community?.members?.length}</span>
            <span class="text-xs text-base-content/75"
              >{pluralize('Member', community?.members?.length ?? 0)}</span
            >
          </div>
          <div class="flex items-center gap-1">
            <span class="text-sm text-info">{community?.posts_count}</span>
            <span class="text-xs text-base-content/75"
              >{pluralize('Post', community?.posts_count)}</span
            >
          </div>
        </div>
      </div>
    </div>
    <!-- community basic operations -->
    <div class="flex items-center gap-2">
      <button class="btn btn-primary h-10 px-3" aria-label="Create a Post">
        <coreicons-shape-plus variant="no-border" class="size-5"></coreicons-shape-plus>
        <span class="text-sm font-medium">Create Post</span>
      </button>
      <button class="btn btn-secondary h-10 px-3" aria-label="Join Community">
        <span class="text-sm font-medium">{is_joined ? 'Joined' : 'Join'}</span>
      </button>
      <button class="btn btn-neutral ml-auto size-10 p-0 md:ml-0" aria-label="More options">
        <coreicons-shape-more class="size-5 rotate-90"></coreicons-shape-more>
      </button>
    </div>
  </div>
</div>
<div class="hidden h-12 md:flex"></div>
<PostsHeader />
<!-- list highlighted posts if exists -->
{#if highlighted_posts?.length}
  <div class="flex flex-col gap-4">
    <div class="flex items-center gap-2">
      <coreicons-shape-hash class="size-5"></coreicons-shape-hash>
      <h4 class="font-medium">Highlights</h4>
    </div>
    <div class="grid grid-cols-2 gap-4 md:grid-cols-3">
      {#each highlighted_posts as post}
        <div
          class="relative flex h-40 flex-col gap-2 overflow-hidden rounded-2xl border border-neutral p-2 transition-colors hover:bg-base-200"
        >
          <div
            class="flex-1 rounded-xl bg-cover bg-center inner-border
            inner-border-base-content/15"
            class:bg-base-100={!post.cover}
            style="background-image: url({post.cover});"
          ></div>
          <div class="flex flex-col p-2 pt-0.5">
            <h4 class="line-clamp-1 font-medium">{post.title}</h4>
            <span class="text-xs font-medium text-base-content/75"
              >{new FormatDate(post.created_at).format()}</span
            >
          </div>
          <a
            href="./{community?.name}/posts/{post.id}/{post.slug}"
            class="absolute inset-0"
            aria-label={post.title}
          ></a>
        </div>
      {/each}
    </div>
  </div>
{/if}
<!-- list posts -->
{#if posts}
  {#each posts as post}
    <PostCard {...post} />
  {/each}
{/if}
