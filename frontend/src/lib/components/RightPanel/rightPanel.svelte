<script>
	import Recent from '$lib/data/moks/recentPost';
import Post from './RightPost.svelte';
</script>

<div class="fixed bottom-0 right-0 top-16  w-80  mx-1 max-h-full  scrollbar-thin scrollbar-thumb-transparent scrollbar-track-sky-300/0 overflow-y-auto" >
	<h2 class="text-info py-4 font-sans font-semibold">Recent Posts</h2>
	<!-- recent posts -->
	<div class="flex flex-col gap-7 mb-4">
		<!-- Post -->
  {#each Recent as post }
		<Post
			comments={post.comments}
			upvotes={post.upvotes}
			postImg={post.postImg}
			title={post.title}
			userImg={post.userImg}
			username={post.username}
		/>
	{/each}
		

		
	</div>
</div>

