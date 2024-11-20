<script lang="ts" >
	type postProps = {
		title: string;
		userImg?: string;
		postImg?: string;
		username: string;
		upvotes: number;
		comments: number;
	};
	import { formatNumber } from '$lib/utils/formatNumber';
	import UserListItem from '../User/UserListItem.svelte';
	let {comments,title,upvotes,username,userImg,postImg}: postProps = $props();
  let votes = formatNumber(upvotes)
  let cmnts = formatNumber(comments)
</script>

<div class="flex gap-2">
	<!--others  -->
	<div class="">
		<UserListItem
			name={username}
			img={userImg}
		/>
		<div class="cursor-pointer">
			<h2
				class="text-info font-sans text-xl font-extrabold transition-all duration-1000 hover:underline"
			>
			{title}
			</h2>
		</div>
		<div class="flex gap-2">
			<p class="text-base-content text-sm font-medium">{votes} upvotes</p>
			<span>•</span>
			<p class="text-base-content text-sm font-medium">{cmnts} comments</p>
		</div>
	</div>
	<!-- image div -->
	<div class="flex w-24 object-contain flex-col items-center justify-center">
		<img class="rounded-xl" src={postImg} alt="" />
	</div>
</div>
