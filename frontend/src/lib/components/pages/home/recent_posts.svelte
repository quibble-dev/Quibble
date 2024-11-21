<script lang="ts">
	import UserListItem from '$lib/components/User/UserListItem.svelte';
	import Recent from '$lib/data/moks/recentPost';
	import readable from 'readable-numbers';
</script>

<div
	class="fixed bottom-0 right-0 top-16 mx-1 max-h-full w-80 overflow-y-auto scrollbar-thin scrollbar-track-sky-300/0 scrollbar-thumb-transparent"
>
	<h2 class="py-4 font-sans font-semibold text-info">Recent Posts</h2>
	<div class="mb-4 flex flex-col gap-7">
		{#each Recent as post}
			<div class="flex justify-between gap-2">
				<div class="flex flex-col">
					<UserListItem name={post.username} img={post.userImg} />
					<div class="cursor-pointer">
						<h2
							class="font-sans text-sm font-extrabold text-info transition-all duration-1000 hover:underline"
						>
							{post.title}
						</h2>
					</div>
					<div class="flex w-full gap-2">
						<p class="text-sm font-medium text-base-content">{readable(post.upvotes)} upvotes</p>
						<span>•</span>
						<p class="text-sm font-medium text-base-content">{readable(post.comments)} comments</p>
					</div>
				</div>
				{#if post.postImg !== undefined}
					<div class="flex flex-col items-center justify-end object-contain">
						<img class="aspect-square h-20 w-20 rounded-xl" src={post.postImg} alt="" />
					</div>
				{/if}
			</div>
		{/each}
	</div>
</div>
