<script lang="ts">
	import CardIcon from '$lib/components/icons/card.svelte';
	import CompactIcon from '$lib/components/icons/compact.svelte';
	import HotIcon from '$lib/components/icons/hot.svelte';
	import NewIcon from '$lib/components/icons/new.svelte';
	import RocketIcon from '$lib/components/icons/rocket.svelte';
	import TopIcon from '$lib/components/icons/top.svelte';
</script>

<div class="flex h-7 w-full justify-between">
	<div class="flex gap-4">
		<a href="/" aria-label="Home" class="flex items-center gap-2">
			<RocketIcon />
			<span class="text-sm font-bold">Best</span>
		</a>
		<a href="/" aria-label="Home" class="flex items-center gap-2">
			<HotIcon />
			<span class="text-sm font-bold">Hot</span>
		</a>
		<a href="/" aria-label="Home" class="flex items-center gap-2">
			<NewIcon />
			<span class="text-sm font-bold">New</span>
		</a>
		<a href="/" aria-label="Home" class="flex items-center gap-2">
			<TopIcon />
			<span class="text-sm font-bold">Top</span>
		</a>
	</div>
	<div class="flex gap-4">
		<a href="/" aria-label="Home" class="flex items-center gap-2">
			<CompactIcon />
			<span class="text-sm font-bold">Compact view</span>
		</a>
		<a href="/" aria-label="Home" class="flex items-center gap-2">
			<CardIcon />
			<span class="text-sm font-bold">Card view</span>
		</a>
	</div>
</div>
