<script lang="ts">
	import Post from '$lib/components/pages/home/post.svelte';
	import PostsHeader from '$lib/components/pages/home/posts_header.svelte';
	import RecentPosts from '$lib/components/pages/home/recent_posts.svelte';
	import posts from '$lib/data/mock/posts.json';
</script>

<svelte:head>
	<title>Quibble - Delve into real conversations.</title>
</svelte:head>

<div class="mx-auto flex flex-1 xl:max-w-5xl">
	<div class="flex h-max flex-1 flex-col gap-4 p-4">
		<PostsHeader />
		<div class="flex flex-1 flex-col gap-4">
			{#each posts as post}
				<Post {...post} />
			{/each}
		</div>
	</div>
	<div class="w-80">
		<RecentPosts />
	</div>
</div>
