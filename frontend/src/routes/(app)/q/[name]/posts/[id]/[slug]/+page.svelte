<script lang="ts">
  import { browser } from '$app/environment';
  import type { components } from '$lib/api';
  import NewIcon from '$lib/components/icons/new.svelte';
  import RocketIcon from '$lib/components/icons/rocket.svelte';
  import TopIcon from '$lib/components/icons/top.svelte';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import BackdropImage from '$lib/components/ui/backdrop-image.svelte';
  import Zoom from '$lib/components/ui/zoom.svelte';
  import { CommentBlock } from '$lib/features/comments';
  import CommentBox from '$lib/features/comments/components/comment-box.svelte';
  import { createRecentPostStore } from '$lib/features/posts/stores/recent-post.svelte';
  import { cn } from '$lib/functions/classnames';
  import { FormatDate } from '$lib/functions/date';
  import { is_valid } from '$lib/functions/is-valid';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import type { CommentTree } from '$lib/types/comment';
  import type { PageData } from './$types';
  import readable from 'readable-numbers';
  import { onMount } from 'svelte';

  type Comment = components['schemas']['CommentDetail'];

  const { data }: { data: PageData } = $props();
  const { post, comments } = $state(data);

  const authStore = createAuthStore();
  const recentPostStore = createRecentPostStore();

  let ratio = $state(post.ratio);
  let reaction = $state<ReturnType<typeof get_reaction>>(get_reaction());

  $inspect(reaction);

  const is_upvoted = $derived.by(check_if_upvoted);
  function check_if_upvoted() {
    if (authStore.state.user && post.upvotes) {
      return post.upvotes.includes(authStore.state.user.profile.id);
    } else {
      return false;
    }
  }

  $effect(() => {
    reaction = get_reaction();
  });

  function get_reaction(): 'upvoted' | 'downvoted' | null {
    if (authStore.state.user) {
      if (post.upvotes?.includes(authStore.state.user.profile.id)) return 'upvoted';
      else if (post.downvotes?.includes(authStore.state.user.profile.id)) return 'downvoted';
      else return null;
    } else {
      return null;
    }
  }

  let active_mapping = $state<{
    filter: keyof typeof mapping.filters;
  }>({
    filter: 'best'
  });

  const mapping = {
    filters: {
      best: { icon: RocketIcon, onclick: () => (active_mapping.filter = 'best') },
      new: { icon: NewIcon, onclick: () => (active_mapping.filter = 'new') },
      top: { icon: TopIcon, onclick: () => (active_mapping.filter = 'top') }
    }
  };

  let active_filter = $derived(mapping.filters[active_mapping.filter]);
  let show_comment_box = $state(false);

  function handle_back() {
    if (browser) window.history.back();
  }

  async function handle_comment(data: { comment: Comment }) {
    show_comment_box = false;

    const new_comment: CommentTree = { ...data.comment, children: [], collapsed: false };
    comments.unshift(new_comment);
  }

  onMount(() => {
    recentPostStore.add_post({
      id: post.id,
      community: post.community,
      title: post.title,
      slug: post.slug,
      cover: post.cover,
      upvotes: post.upvotes,
      comments: post.comments
    });
  });
</script>

<svelte:head>
  <title>{post.title} : q/{post.community.name}</title>
</svelte:head>

<!-- poster and community details and more -->
<div class="flex items-center gap-2">
  <button onclick={handle_back} class="btn btn-neutral size-8 rounded-full p-0" aria-label="back">
    <coreicons-shape-arrow variant="left" class="size-5"></coreicons-shape-arrow>
  </button>
  <div class="flex items-center gap-2">
    <a href="/q/{post.community.name}">
      <Avatar src={post.community.avatar} class="size-8 rounded-full" />
    </a>
    <div class="flex flex-col">
      <div class="flex items-center gap-2">
        <a href="/q/{post.community.name}" class="hover:text-accent hover:underline">
          <h3 class="text-xs font-semibold">q/{post.community.name}</h3>
        </a>
        <coreicons-shape-circle variant="filled" class="text-base-content/75 size-0.5"
        ></coreicons-shape-circle>
        <span class="text-base-content/75 text-xs font-medium"
          >{new FormatDate(post.created_at).timeAgo()}</span
        >
      </div>
      <a href="/u/{post.poster.username}" class="w-max hover:underline">
        <h3 class="text-xs">{post.poster.username}</h3>
      </a>
    </div>
  </div>
  <button class="btn btn-sm btn-square btn-ghost ml-auto" aria-label="more">
    <coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
  </button>
</div>
<!-- title -->
<h1 class="text-info text-xl font-bold md:text-2xl">{post.title}</h1>
<!-- content or cover -->
{#if is_valid(post.content)}
  <p class="text-sm font-normal">
    {post.content}
  </p>
{:else}
  <BackdropImage src={post.cover} class="z-10">
    <Zoom>
      <img src={post.cover} alt="" class="max-h-[25rem] object-contain" />
    </Zoom>
  </BackdropImage>
{/if}
<!-- post options like vote share -->
<div class="flex items-center gap-4">
  <div class="flex items-center gap-2">
    <button class="flex items-center gap-2" aria-label="upvote">
      <coreicons-shape-thumbs variant="up" class="size-4" class:text-primary={is_upvoted}
      ></coreicons-shape-thumbs>
    </button>
    <span class="text-sm font-medium">{readable(ratio)}</span>
    <button class="flex items-center gap-2" aria-label="downvote">
      <coreicons-shape-thumbs variant="down" class="size-4"></coreicons-shape-thumbs>
    </button>
  </div>
  <button class="flex items-center gap-2">
    <coreicons-shape-forum class="size-4"></coreicons-shape-forum>
    <span class="text-sm font-medium">{readable(post.comments?.length ?? 0)} comments</span>
  </button>
  <button class="flex items-center gap-2">
    <coreicons-shape-share class="size-4"></coreicons-shape-share>
    <span class="text-sm font-medium">Share</span>
  </button>
</div>

{#if show_comment_box}
  <!-- root comment -->
  <CommentBox
    oncancel={() => (show_comment_box = false)}
    oncomment={(comment) => handle_comment(comment)}
  />
{:else}
  <button
    class="border-base-content/20 rounded-box flex cursor-text items-center gap-2 border p-2.5 text-sm"
    onclick={() => (show_comment_box = true)}
  >
    <coreicons-shape-message-circle class="size-5"></coreicons-shape-message-circle>
    Add a comment...
  </button>
{/if}

<!-- comment sort and add comment -->
<div class="flex items-center gap-2">
  <div class="flex items-center gap-2">
    <span class="text-sm">Sort by:</span>
    <div class="dropdown-start dropdown">
      <div tabindex="0" role="button" class="flex cursor-pointer items-center gap-2 select-none">
        <active_filter.icon class="text-primary size-4" />
        <span class="text-sm font-medium capitalize">{active_mapping.filter}</span>
        <coreicons-shape-chevron variant="down" class="text-base-content/75 size-4"
        ></coreicons-shape-chevron>
      </div>
      <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
      <ul tabindex="0" class="menu dropdown-content bg-base-100 z-10 mt-2 gap-1 rounded-2xl p-1.5">
        {#each Object.entries(mapping.filters) as [key, item]}
          {@const is_active = active_mapping.filter === key}
          <li>
            <button
              onclick={item.onclick}
              aria-label="{key} filter"
              class="flex items-center gap-2 rounded-xl p-2"
            >
              <item.icon class={cn(is_active && 'text-primary', 'size-4')} />
              <span class="text-sm font-medium capitalize" class:text-primary={is_active}
                >{key}</span
              >
            </button>
          </li>
        {/each}
      </ul>
    </div>
  </div>
</div>
<!-- render comments -->
{#if comments}
  {#each comments as comment (comment.id)}
    <CommentBlock {...comment} />
  {/each}
{/if}
