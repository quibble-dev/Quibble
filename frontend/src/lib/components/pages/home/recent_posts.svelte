<script lang="ts">
	import readable from 'readable-numbers';
	import Avatar from '$lib/components/ui/avatar.svelte';
	import recent_posts from '$lib/data/mock/recent_posts.json';
</script>

<div
	class="fixed top-[3.75rem] flex  h-[calc(100dvh-3.75rem)] w-72 flex-col gap-4 overflow-y-scroll p-4 scrollbar-none"
>
	<h2 class="font-semibold">Recent Posts</h2>
	<div class="flex flex-col gap-4">
		{#each recent_posts as post}
			<div class="flex justify-between gap-2">
				<div class="flex flex-col gap-1">
					<div class="flex items-center gap-2">
						<Avatar src={post.community.avatar} alt={post.community.name} />
						<a href="/q/{post.community.name}" class="text-xs font-bold">q/{post.community.name}</a>
					</div>
					<a
						href="/q/{post.community.name}/posts/{post.slug}"
						class="font-extrabold text-info hover:underline"
					>
						{post.title}
					</a>
					<div class="flex items-center gap-2">
						<p class="text-xs font-medium">{readable(post.likes)} likes</p>
						<coreicons-shape-circle variant="filled" class="size-0.5"></coreicons-shape-circle>
						<p class="text-xs font-medium">{readable(post.comments)} quibble(s)</p>
					</div>
				</div>
				{#if post.cover}
					<img
						class="aspect-square size-20 flex-shrink-0 rounded-xl object-cover"
						src={post.cover}
						alt=""
					/>
				{/if}
			</div>
		{/each}
	</div>
</div>
