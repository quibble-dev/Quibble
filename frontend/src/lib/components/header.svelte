<script lang="ts">
	import ChartBars from '$lib/icons/chart_bars.svelte';
	import Home from '$lib/icons/Home.svelte';
	import Notification from '$lib/icons/Notification.svelte';
	import Plus from '$lib/icons/Plus.svelte';
	import Popular from '$lib/icons/Popular.svelte';
	import Search from '$lib/icons/Search.svelte';

	let is_authenticated = $state(true);
</script>

<header class="flex h-[75px] w-full flex-row items-center justify-between bg-neutral">
	<!-- quibble icon -->
	<div class="flex h-full items-center pl-5">
		<h1 class="text-center text-3xl font-black text-primary">Quibble</h1>
	</div>
	<!-- search bar and navigates -->
	<div class="flex h-[50px] w-[1000px] flex-row items-center justify-center gap-5">
		<div class="flex flex-row justify-center gap-5">
			<span class="flex cursor-pointer space-x-2">
				<Home />
				<span class="text-lg font-bold">Home</span>
			</span>
			<span class="flex cursor-pointer space-x-2">
				<ChartBars variant="popular" />
				<span class="text-lg font-bold">Popular</span>
			</span>
			<span class="flex cursor-pointer space-x-2">
				<ChartBars variant="all" />
				<span class="text-lg font-bold">All</span>
			</span>
		</div>
		<div class="w-[600px]">
			<label class="input input-bordered flex items-center">
				<Search />
				<input
					type="text"
					class="input w-full grow placeholder:text-base placeholder:font-bold focus:border-none"
					placeholder="Seek. Find. Quibble"
				/>
			</label>
		</div>
	</div>
	<!-- create account details & join in -->
	<div class="flex h-[40px] items-center gap-5 pr-4">
		{#if is_authenticated}
			<button class="btn btn-primary btn-md font-bold">
				<Plus /> <span>Create New</span>
			</button>
			<Notification />
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
