<script lang="ts">
	type User = {
		name: string;
		stared: boolean;
		img: string;
	};
	import Star from '$lib/components/icons/StarIcon.svelte';
	import StarFill from '$lib/components/icons/StarFill.svelte';

	let { name, stared, img }: User = $props();
</script>

<div class="mb-3 flex w-full cursor-pointer items-center justify-between gap-2">
	<div class="flex gap-2">
		{#if img?.length == 0}
			<div class="avatar placeholder">
				<div class="text-neutral-content w-[30px] rounded-full bg-lime-500">
					<span class="text-[16px] font-bold capitalize text-black">{name.slice(0, 1)}</span>
				</div>
			</div>
		{:else}
			<div class="avatar">
				<div class="w-[30px] rounded-full">
					<img
						alt=""
						src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
					/>
				</div>
			</div>
		{/if}

		<h1>q/{name}</h1>
	</div>
	{#if stared}
		<StarFill />
	{:else}
		<Star />
	{/if}
</div>
