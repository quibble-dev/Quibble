<script lang="ts">
	import CardIcon from '$lib/components/icons/card.svelte';
	import CompactIcon from '$lib/components/icons/compact.svelte';
	import HotIcon from '$lib/components/icons/hot.svelte';
	import NewIcon from '$lib/components/icons/new.svelte';
	import RocketIcon from '$lib/components/icons/rocket.svelte';
	import TopIcon from '$lib/components/icons/top.svelte';
	import { cn } from '$lib/functions/classnames';

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
			compact: {
				icon: CompactIcon,
				onclick: () => {
					active_mapping.view = 'compact';
				}
			},
			card: {
				icon: CardIcon,
				onclick: () => {
					active_mapping.view = 'card';
				}
			}
		}
	};

	let active_view_icon = $derived(mapping.view[active_mapping.view]);

	console.log(mapping);
	console.log(mapping.view[active_mapping.view].icon);
</script>

<div class="flex items-center justify-between">
	<div class="flex gap-3">
		{#each Object.entries(mapping.filters) as [key, item]}
			{@const is_active = active_mapping.filter === key}

			<div class="flex flex-col items-center gap-1">
				<a href={item.href} aria-label={key} class="flex items-center gap-2">
					<item.icon class="size-4" />
					<span class="text-sm font-bold capitalize">{key}</span>
				</a>
				{#if is_active}
					<div class="bg-primary h-0.5 w-5 rounded-full"></div>
				{/if}
			</div>
		{/each}
	</div>
	<div class="flex gap-3">
		<div class="dropdown">
			<div tabindex="0" role="button" class="btn btn-sm hover:bg-neutral m-1 bg-transparent">
				<active_view_icon.icon class="stroke-primary"/>
				<span class="text-sm font-bold capitalize">{active_mapping.view}</span>
			</div>
			<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
			<ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-[1] w-32 p-2 shadow gap-1">
				{#each Object.entries(mapping.view) as [key, item]}
					{@const is_active = active_mapping.view === key}
					<li>
						<button
							onclick={item.onclick}
							aria-label="{key} view"
							class="flex items-center gap-2 p-2"
						>
							<item.icon class={cn(is_active ? 'stroke-primary' : 'stroke-neutral-content', 'size-4')} />
							<span class={cn(is_active && 'text-primary',"text-sm font-bold capitalize")}>{key}</span>
						</button>
					</li>
				{/each}
			</ul>
		</div>
	</div>
</div>
