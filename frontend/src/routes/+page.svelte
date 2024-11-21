<script lang="ts">
	import mockPosts from '$lib/data/moks/post';
	import Post from '$lib/components/pages/home/post.svelte';
	import PostsHeader from '$lib/components/pages/home/posts_header.svelte';
</script>

<svelte:head>
	<title>Quibble - Delve into real conversations.</title>
</svelte:head>

<div class="ml-64 mr-80 mt-20 min-h-screen flex-1 overflow-auto pr-8">
	<PostsHeader />
	<div class="hidden flex w-full flex-col justify-center">
		{#each mockPosts as post}
			<Post {...post} />
		{/each}
	</div>
</div>
