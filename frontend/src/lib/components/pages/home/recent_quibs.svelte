<script lang="ts">
  import readable from 'readable-numbers';
  import Avatar from '$lib/components/ui/avatar.svelte';
  import recent_posts from '$lib/data/mock/recent_posts.json';
</script>

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
            <Avatar src={post.community.avatar} alt={post.community.name} />
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
        <coreicons-shape-circle variant="filled" class="size-0.5"></coreicons-shape-circle>
        <p class="text-xs font-medium">{readable(post.comments)} comments</p>
      </div>
    </div>
  {/each}
</div>
