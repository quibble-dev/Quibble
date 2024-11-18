<script lang="ts">
	import ChartBarsIcon from '$lib/components/icons/chart_bars.svelte';
	import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
	import NotificationIcon from '$lib/components/icons/notification.svelte';

	let is_authenticated = $state(true);
</script>

<header class="flex items-center justify-between bg-base-200 p-2.5 px-4">
	<!-- quibble logo -->
	<a href="/" class="flex items-center gap-2">
		<QuibbleLogo class="size-7" />
		<h1 class="font-riffic text-2xl text-white">Quibble</h1>
	</a>
	<!-- search bar and navigates -->
	<div class="flex items-center gap-5">
		<div class="flex gap-2">
			<span class="flex items-center gap-2">
				<coreproject-shape-home class="size-5 text-primary"></coreproject-shape-home>
				<span class="font-bold">Home</span>
			</span>
			<span class="flex items-center gap-2">
				<ChartBarsIcon variant="popular" class="size-5" />
				<span class="font-bold">Popular</span>
			</span>
			<span class="flex items-center gap-2">
				<ChartBarsIcon variant="all" class="size-5" />
				<span class="font-bold">All</span>
			</span>
		</div>
		<label class="input input-bordered flex h-10 w-96 items-center bg-transparent px-3">
			<coreproject-shape-search class="size-5"></coreproject-shape-search>
			<input
				type="text"
				class="grow border-none font-medium focus:ring-0"
				placeholder="Search..."
			/>
		</label>
	</div>
	<!-- create, account details & join in -->
	<div class="flex items-center gap-2">
		{#if is_authenticated}
			<button class="btn btn-primary h-10 px-3">
				<coreproject-shape-plus variant="no-border" class="size-5"></coreproject-shape-plus>
				<span class="font-semibold">Create</span>
			</button>
			<button aria-label="Notifications" class="btn btn-neutral size-10 p-0">
				<NotificationIcon class="size-6" />
			</button>
			<div class="avatar btn size-10 overflow-hidden p-0">
				<img draggable="false" alt="moonlitgrace" src="https://github.com/moonlitgrace.png" />
			</div>
		{:else}
			<button class="btn btn-primary h-10 px-3 font-bold">Join In!</button>
		{/if}
	</div>
</header>
