<script lang="ts">
  import Quib from '$lib/components/quib.svelte';
  import QuibsHeader from '$lib/components/quibs_header.svelte';
  import recent_posts from '$lib/data/mock/recent_posts.json';
  import readable from 'readable-numbers';
  import Image from '$lib/components/ui/image.svelte';
  import type { PageData } from './$types';

  const { data }: { data: PageData } = $props();
</script>

<svelte:head>
  <title>Quibble - Delve into real conversations.</title>
</svelte:head>

<div class="flex h-max flex-1 flex-col gap-4 p-4">
  <QuibsHeader />
  <div class="flex flex-1 flex-col gap-4">
    {#if data.quibs}
      {#each data.quibs as quib}
        <Quib {...quib} />
      {/each}
    {/if}
  </div>
</div>
<div class="w-80">
  <div
    class="fixed top-[3.75rem] flex h-[calc(100dvh-3.75rem)] w-72 flex-col gap-4 overflow-y-scroll p-4 scrollbar-none"
  >
    <h2 class="font-medium">Recent Quibs</h2>
    <div class="flex flex-col gap-4">
      {#each recent_posts as post}
        <div class="flex flex-col gap-2">
          <div class="flex justify-between gap-2">
            <div class="flex flex-col gap-1">
              <a
                href="/q/{post.community.name}"
                class="flex items-center gap-2 hover:text-accent hover:underline"
              >
                <Image src={post.community.avatar} class="size-6 rounded-full" />
                <h3 class="text-xs font-semibold">q/{post.community.name}</h3>
              </a>
              <a
                href="/q/{post.community.name}/posts/{post.slug}"
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
            <p class="text-xs font-medium">{readable(post.likes)} upvotes</p>
            <coreicons-shape-circle variant="filled" class="size-0.5"
            ></coreicons-shape-circle>
            <p class="text-xs font-medium">{readable(post.comments)} comments</p>
          </div>
        </div>
      {/each}
    </div>
  </div>
</div>
