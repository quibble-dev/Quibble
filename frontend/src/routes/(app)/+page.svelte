<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';
  import { emoticons } from '$lib/constants/emoticons';
  import { PostCard, PostsHeader } from '$lib/features/posts';
  import { createRecentPostStore } from '$lib/features/posts/stores/recent-post.svelte';
  import type { PageData } from './$types';
  import readable from 'readable-numbers';

  const { data }: { data: PageData } = $props();

  const recentPostStore = createRecentPostStore();
</script>

<!-- site head and seo -->
<svelte:head>
  <title>Quibble - Delve into real conversations.</title>
</svelte:head>

<div class="flex h-max flex-1 flex-col gap-4 p-4">
  <!-- posts header: filter and change layout type -->
  <PostsHeader />
  <!-- list posts section -->
  <div class="flex flex-1 flex-col gap-4">
    <!-- if posts available -->
    {#if data.posts && data.posts.length}
      {#each data.posts as post (post.id)}
        <PostCard {...post} />
      {/each}
    {:else}
      <!-- if not available: render fallback -->
      <div class="flex flex-col">
        <span class="text-lg font-medium">{emoticons.DISTRESSED}</span>
        <span class="text-sm">The silence is deafening—why not break it?</span>
      </div>
    {/if}
  </div>
</div>
<!-- fixed shared sidebar for recent posts -->
<div class="hidden w-80 lg:flex">
  <div
    class="fixed top-[3.75rem] flex h-[calc(100dvh-3.75rem)] w-72 flex-col gap-4 overflow-y-scroll p-4 scrollbar-none"
  >
    <div class="flex items-center justify-between">
      <h2 class="font-medium">Recent Posts</h2>
      <button
        class="btn btn-ghost btn-xs z-10"
        disabled={recentPostStore.state.length === 0}
        onclick={recentPostStore.clear}>Clear</button
      >
    </div>
    <!-- render recent posts from localstorage -->
    <div class="flex flex-col gap-4">
      {#if recentPostStore.state.length}
        {#each recentPostStore.state as post (post.id)}
          <!-- recent post component -->
          <div class="flex flex-col gap-2">
            <div class="flex justify-between gap-2">
              <div class="flex flex-col gap-1">
                <a
                  href="/q/{post.community.name}"
                  class="flex items-center gap-2 hover:text-accent hover:underline"
                >
                  <Avatar src={post.community.avatar} class="size-6 rounded-full" />
                  <h3 class="text-xs font-semibold">q/{post.community.name}</h3>
                </a>
                <a
                  href="/q/{post.community.name}/posts/{post.id}/{post.slug}"
                  class="font-semibold text-info hover:underline"
                >
                  {post.title}
                </a>
              </div>
              {#if post.cover}
                <img
                  class="aspect-square size-20 flex-shrink-0 rounded-xl object-cover"
                  src={post.cover}
                  alt=""
                />
              {/if}
            </div>
            <div class="flex items-center gap-2">
              <p class="text-xs font-medium">
                {readable(post.upvotes?.length ?? 0)} upvotes
              </p>
              <coreicons-shape-circle variant="filled" class="size-0.5"></coreicons-shape-circle>
              <p class="text-xs font-medium">
                {readable(post.comments?.length ?? 0)} comments
              </p>
            </div>
          </div>
        {/each}
      {:else}
        <!-- fallback content if there are no recent posts -->
        <div class="flex flex-col">
          <span class="text-lg font-medium">{emoticons.ANGRY}</span>
          <span class="text-sm">Nothing here yet—go find a Post!</span>
        </div>
      {/if}
    </div>
  </div>
</div>
