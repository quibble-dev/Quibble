<script lang="ts">
	type postProps = {
		title: string;
		userImg?: string;
		postImg?: string;
		username: string;
		upvotes: number ;
		comments: number;
	};

	import readable from 'readable-numbers';
	import UserListItem from '../User/UserListItem.svelte';
	let { comments, title, upvotes, username, userImg, postImg }: postProps = $props();
</script>

<div class="flex justify-between gap-2">
	<!--others  -->
	<div class="flex flex-col">
		<UserListItem name={username} img={userImg} />
		<div class="cursor-pointer">
			<h2
				class="text-info font-sans text-sm font-extrabold transition-all duration-1000 hover:underline"
			>
				{title}
			</h2>
		</div>
		<div class="flex w-full gap-2">
			<p class="text-base-content text-sm font-medium">{readable(upvotes)} upvotes</p>
			<span>•</span>
			<p class="text-base-content text-sm font-medium">{readable(comments)} comments</p>
		</div>
	</div>
	<!-- image div -->
	{#if postImg !== undefined}
		<div class="flex flex-col items-center justify-end object-contain">
			<img class="rounded-xl w-20 h-20  aspect-square" src={postImg} alt="" />
		</div>
	{/if}
</div>
