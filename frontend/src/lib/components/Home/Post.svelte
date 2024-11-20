<script lang="ts" >
	import readable from 'readable-numbers';
	import Dots from '../icons/dots.svelte';
	import Downvote from '../icons/downvote.svelte';
	import Upvote from '../icons/upvote.svelte';
	import UserListItem from '../User/UserListItem.svelte';
  type PostProps = {
    title: string,
    time: string,
    content: string,
    image?: string,
    upvotes: number,
    downvotes: number,
    comments: number,
    username:string;
    userimage?: string;


  }
 let {comments,content,downvotes,title,time,upvotes,userimage,username,image}:PostProps = $props()

</script>

<div class="bg-base-200 my-4 flex w-full flex-col gap-3 rounded-2xl p-4">
	<UserListItem name={username} img={userimage} {time} />
	<div class="flex flex-col  gap-1">
		<h2 class="font-extrabold text-white">{title}</h2>
		<p class="text-base-content  text-base font-normal">
		{content}
		</p>
	</div>
	{#if image !== undefined}
  <div class="w-full ">
    <img class="rounded-lg w-full" src={image ? image : ""} alt="">
  </div>
	{/if}
	<div class="mt-2 flex gap-5">
		<a href="/" class="flex items-center gap-1">
			<Upvote />
			<span class="text-sm font-semibold">{readable(upvotes)}</span>
		</a>
		<a href="/" class="flex items-center gap-1">
			<Downvote />
			<span class="text-sm font-semibold">{readable(downvotes)}</span>
		</a>
		<a href="/" class="flex items-center gap-2">
			<coreicons-shape-forum></coreicons-shape-forum>
			<span class="text-sm font-semibold">{readable(comments)} Comments</span>
		</a>
		<a href="/" class="flex items-center gap-2">
			<coreicons-shape-share></coreicons-shape-share>
			<span class="text-sm font-semibold">Share</span>
		</a>
		<a href="/" class="flex items-center gap-2">
			<Dots />
		</a>
	</div>
</div>
