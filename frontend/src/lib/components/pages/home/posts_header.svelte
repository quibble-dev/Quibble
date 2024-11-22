<script lang="ts">
	import CardIcon from '$lib/components/icons/card.svelte';
	import CompactIcon from '$lib/components/icons/compact.svelte';
	import HotIcon from '$lib/components/icons/hot.svelte';
	import NewIcon from '$lib/components/icons/new.svelte';
	import RocketIcon from '$lib/components/icons/rocket.svelte';
	import TopIcon from '$lib/components/icons/top.svelte';

	let active_mapping = $state<{
		filter: keyof typeof mapping.filters;
		view: keyof typeof mapping.view;
	}>({
		filter: 'best',
		view: 'card'
	});

	const mapping = {
		filters: {
			best: { icon: RocketIcon, href: '/' },
			hot: { icon: HotIcon, href: '/hot' },
			new: { icon: NewIcon, href: '/new' },
			top: { icon: TopIcon, href: '/top' }
		},
		view: {
			compact: { icon: CompactIcon, onclick: () => {} },
			card: { icon: CardIcon, onclick: () => {} }
		}
	};
</script>

<div class="flex flex-col sm:flex-row items-center justify-between">
	<div class="flex gap-3 w-full sm:w-auto">
		{#each Object.entries(mapping.filters) as [key, item]}
			{@const is_active = active_mapping.filter === key}

			<div class="flex flex-col items-center flex-1 sm:flex-auto transition-colors hover:bg-base-100 p-1 sm:px-2 rounded-xl">
				<a href={item.href} aria-label={key} class="flex items-center gap-2">
					<item.icon class="size-4" />
					<span class="text-sm font-bold capitalize">{key}</span>
				</a>
				{#if is_active}
					<div class="h-0.5 w-2/3 mt-3 sm:w-5 sm:m-0 rounded-full bg-primary"></div>
				{/if}
			</div>
		{/each}
	</div>
	<div class="hidden sm:flex gap-3">
		<span class="text-sm font-bold">View:</span>
		{#each Object.entries(mapping.view) as [key, item]}
			{@const is_active = active_mapping.view === key}

			<div class="flex flex-col items-center gap-1">
				<button onclick={item.onclick} aria-label="{key} view" class="flex items-center gap-2">
					<item.icon class="size-4" />
					<span class="text-sm font-bold capitalize">{key}</span>
				</button>
				{#if is_active}
					<div class="h-0.5 w-5 rounded-full bg-primary"></div>
				{/if}
			</div>
		{/each}
	</div>
</div>
