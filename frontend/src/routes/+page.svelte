<script lang="ts">
	import Post from '$lib/components/pages/home/post.svelte';
	import PostsHeader from '$lib/components/pages/home/posts_header.svelte';
	import RecentPosts from '$lib/components/pages/home/recent_posts.svelte';
	import { posts } from '$lib/data/mock/posts';
</script>

<svelte:head>
	<title>Quibble - Delve into real conversations.</title>
</svelte:head>

<div class="flex flex-col sm:flex-row flex-1 gap-2 overflow-y-scroll scrollbar-thin">
	<div class="flex h-max flex-1 flex-col gap-4 p-4">
		<PostsHeader />
		<div class="flex flex-1 flex-col gap-4">
			{#each posts as post}
				<Post {...post} />
			{/each}
		</div>
	</div>
	<RecentPosts />
</div>
