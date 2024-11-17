<script lang="ts">
	import ChartBarsIcon from '$lib/components/icons/chart_bars.svelte';
	import HomeIcon from '$lib/components/icons/home.svelte';
	import SearchIcon from '$lib/components/icons/search.svelte';
	import PlusIcon from '$lib/components/icons/plus.svelte';
	import NotificationIcon from '$lib/components/icons/notification.svelte';
	import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';

	let is_authenticated = $state(true);
</script>

<header class="flex items-center justify-between bg-base-100 p-4">
	<!-- quibble icon -->
	<div class="flex items-center gap-2">
		<QuibbleLogo class="size-6" />
		<h1 class="font-riffic text-xl text-primary">Quibble</h1>
	</div>
	<!-- search bar and navigates -->
	<div class="flex h-[50px] w-[1000px] flex-row items-center justify-center gap-5">
		<div class="flex flex-row justify-center gap-5">
			<span class="flex cursor-pointer space-x-2">
				<HomeIcon />
				<span class="text-lg font-bold">Home</span>
			</span>
			<span class="flex cursor-pointer space-x-2">
				<ChartBarsIcon variant="popular" />
				<span class="text-lg font-bold">Popular</span>
			</span>
			<span class="flex cursor-pointer space-x-2">
				<ChartBarsIcon variant="all" />
				<span class="text-lg font-bold">All</span>
			</span>
		</div>
		<div class="w-[600px]">
			<label class="input input-bordered flex items-center">
				<SearchIcon />
				<input
					type="text"
					class="input w-full grow placeholder:text-base placeholder:font-bold focus:border-none"
					placeholder="Seek. Find. Quibble"
				/>
			</label>
		</div>
	</div>
	<!-- create account details & join in -->
	<div class="flex h-[40px] items-center gap-5">
		{#if is_authenticated}
			<button class="btn btn-primary btn-md font-bold">
				<PlusIcon /> <span>Create New</span>
			</button>
			<NotificationIcon />
			<div draggable="false" class="avatar cursor-pointer select-none">
				<div class="w-[50px] rounded-[15px]">
					<img
						draggable="false"
						alt="avatar"
						src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
					/>
				</div>
			</div>
		{:else}
			<button class="btn btn-primary btn-md font-bold">Join In!</button>
		{/if}
	</div>
</header>
