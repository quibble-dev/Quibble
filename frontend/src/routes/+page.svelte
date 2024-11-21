<script>
	import HomeHeader from '$lib/components/Home/HomeHeader.svelte';
	import Post from '$lib/components/Home/Post.svelte';
	import mockPosts from '$lib/data/moks/post';
</script>

<svelte:head>
	<title>Quibble - Delve into real conversations.</title>
</svelte:head>

<div class="ml-64 mr-80 mt-20 min-h-screen flex-1 overflow-auto pr-8">
	<HomeHeader />
	<div class="flex w-full flex-col justify-center">
		{#each mockPosts as post}
			<Post
				comments={post.comments}
				time={post.time}
				content={post.content}
				title={post.title}
				downvotes={post.downvotes}
				upvotes={post.upvotes}
				username={post.username}
				image={post.image}
				userimage={post.userimage}
			/>
		{/each}
	</div>
</div>
