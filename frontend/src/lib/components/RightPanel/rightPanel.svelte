<script>
	import Post from './RightPost.svelte';
</script>

<div class="fixed top-16 bottom-0  mx-3 right-0 l  h-screen w-80">
	<h2 class="text-info py-4 font-sans font-semibold">Recent Posts</h2>
	<!-- recent posts -->
	<div class="flex flex-col gap-6">
		<!-- Post -->
		<Post comments={500} upvotes={1000} postImg="https://avatars.githubusercontent.com/u/114811070?v=4" title="I love moonlightgrace, she is mine" userImg="https://i.pinimg.com/736x/53/c2/9d/53c29d1baf7aa6d98206235b4021ee87.jpg" username="gayi" />
		<Post comments={54000} upvotes={22300} title="any one want my beer" postImg="https://i.pinimg.com/736x/e4/3e/1e/e43e1e3db0f2dc79caef437717e01cb5.jpg" userImg="https://i.pinimg.com/736x/70/8e/32/708e32ee69a19b625290653acb582840.jpg"  username="madison beer" />

	</div>
</div>
