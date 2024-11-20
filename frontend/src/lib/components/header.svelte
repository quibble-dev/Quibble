<script lang="ts">
	import ChartBarsIcon from '$lib/components/icons/chart_bars.svelte';
	import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
	import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
	import NotificationIcon from '$lib/components/icons/notification.svelte';

	let is_authenticated = $state(true);
</script>

<header class="flex items-center fixed top-0 z-50 w-full justify-between border-b border-neutral bg-base-200 p-2.5 px-4">
	<!-- quibble logo -->
	<a href="/" aria-label="Quibble Home" class="flex items-center gap-2">
		<QuibbleLogo class="size-7" />
		<QuibbleTextLogo class="h-7 w-auto" />
	</a>
	<!-- search bar and navigates -->
	<div class="flex items-center gap-5">
		<div class="flex gap-2">
			<a href="/" aria-label="Home" class="flex items-center gap-2">
				<coreicons-shape-home class="size-5 text-primary"></coreicons-shape-home>
				<span class="text-sm font-bold">Home</span>
			</a>
			<a href="/q/popular" aria-label="Popular Quibbles" class="flex items-center gap-2">
				<ChartBarsIcon variant="popular" class="size-5" />
				<span class="text-sm font-bold">Popular</span>
			</a>
			<a href="/q/all" aria-label="All Quibbles" class="flex items-center gap-2">
				<ChartBarsIcon variant="all" class="size-5" />
				<span class="text-sm font-bold">All</span>
			</a>
		</div>
		<label
			class="input input-bordered flex h-10 w-96 items-center bg-transparent px-3 transition-colors focus-within:bg-base-100"
		>
			<coreicons-shape-search class="size-5"></coreicons-shape-search>
			<input
				type="text"
				class="grow border-none text-sm font-semibold focus:ring-0"
				placeholder="Search..."
			/>
		</label>
	</div>
	<!-- create, account details & join in -->
	<div class="flex items-center gap-2">
		{#if is_authenticated}
			<button aria-label="Create Quibble" class="btn btn-primary h-10 px-3">
				<coreicons-shape-plus variant="no-border" class="size-5"></coreicons-shape-plus>
				<span class="text-sm font-semibold">Create</span>
			</button>
			<button aria-label="Notifications" class="btn btn-neutral size-10 p-0">
				<NotificationIcon class="size-6" />
			</button>
			<button aria-label="Profile" class="avatar btn size-10 overflow-hidden p-0">
				<img draggable="false" alt="moonlitgrace" src="https://i.pinimg.com/736x/c2/9b/68/c29b68c2d7c8d3a4cd6b607e478ff9cf.jpg" />
			</button>
		{:else}
			<button class="btn btn-primary h-10 px-3 text-sm font-bold">
				Join In!
				<coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
			</button>
		{/if}
	</div>
</header>
