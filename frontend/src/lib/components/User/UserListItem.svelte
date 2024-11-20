<script lang="ts">
	type User = {
		name: string;
		stared?: boolean;
		img?: string;
		time?: string;
	};
	import Star from '$lib/components/icons/StarIcon.svelte';
	import StarFill from '$lib/components/icons/StarFill.svelte';

	let { name, stared, img, time }: User = $props();
</script>

<div class="mb-3 flex w-full cursor-pointer items-center justify-between gap-2">
	<div class="flex items-center gap-2">
		{#if !img}
			<div class="avatar placeholder">
				<div class="text-neutral-content w-7 rounded-full bg-lime-500">
					<span class=" font-bold capitalize text-black">{name.slice(0, 1)}</span>
				</div>
			</div>
		{:else}
			<div class="avatar">
				<div class="w-8 rounded-full">
					<img alt="" src={img} />
				</div>
			</div>
		{/if}

		<a href="/" aria-label="Home" class="flex items-center gap-2">
			<h1 class="text-base-content text-xs font-semibold">q/{name}</h1>
			{#if time !== undefined}
			<div class="flex items-center gap-2" >
				<span>•</span>
				<span class="text-base-content/50 text-xs">2hr ago</span>
			</div>
			{/if}
		</a>
	</div>
	{#if stared !== undefined}
		<div>
			{#if stared}
				<StarFill />
			{:else}
				<Star />
			{/if}
		</div>
	{/if}
</div>
