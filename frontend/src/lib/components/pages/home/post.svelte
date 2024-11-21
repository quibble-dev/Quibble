<script lang="ts">
	import readable from 'readable-numbers';

	type Props = {
		title: string;
		time: string;
		content: string;
		image?: string;
		upvotes: number;
		downvotes: number;
		comments: number;
		username: string;
		userimage: string;
	};

	let props: Props = $props();
</script>

<div class="my-4 flex w-full flex-col gap-3 rounded-2xl bg-base-200 p-4">
	<!-- <UserListItem name={props.username} img={props.userimage} time={props.time} /> -->
	<div class="flex flex-col gap-1">
		<h2 class="font-extrabold text-white">{props.title}</h2>
		<p class="text-base font-normal text-base-content">
			{props.content}
		</p>
	</div>
	{#if props.image !== undefined}
		<div class="w-full">
			<img class="w-full rounded-lg" src={props.image} alt="" />
		</div>
	{/if}
	<div class="mt-2 flex gap-5">
		<a href="/" class="flex items-center gap-1">
			<coreicons-shape-thumbs variant="up"></coreicons-shape-thumbs>
			<span class="text-sm font-semibold">{readable(props.upvotes)}</span>
		</a>
		<a href="/" class="flex items-center gap-1">
			<coreicons-shape-thumbs variant="down"></coreicons-shape-thumbs>
			<span class="text-sm font-semibold">{readable(props.downvotes)}</span>
		</a>
		<a href="/" class="flex items-center gap-2">
			<coreicons-shape-forum></coreicons-shape-forum>
			<span class="text-sm font-semibold">{readable(props.comments)} Comments</span>
		</a>
		<a href="/" class="flex items-center gap-2">
			<coreicons-shape-share></coreicons-shape-share>
			<span class="text-sm font-semibold">Share</span>
		</a>
		<a href="/" class="flex items-center gap-2">
			<coreicons-shape-circle variant='filled'></coreicons-shape-circle>
		</a>
	</div>
</div>
