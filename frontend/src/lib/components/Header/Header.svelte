<script>
	import All from '../Icons/All.svelte';
	import Home from '../Icons/Home.svelte';
	import Popular from '../Icons/Popular.svelte';
	import Search from '../Icons/Search.svelte';
	import HeaderAuth from './HeaderAuth.svelte';
	import HeaderNoAuth from './HeaderNoAuth.svelte';

	let auth = $state(false);
</script>

<div class="bg-neutral flex h-[75px] w-full flex-row items-center justify-between">
	<!-- quibble icon -->
	<div class="flex h-full items-center pl-5">
		<h1 class="text-primary text-center text-3xl font-black">Quibble</h1>
	</div>
	<!-- search bar and navigates -->
	<div class="flex h-[50px] w-[1000px] flex-row items-center justify-center gap-5">
		<div class="flex flex-row justify-center gap-5">
			<span class="flex cursor-pointer space-x-2">
				<Home />
				<span class="text-lg font-bold">Home</span>
			</span>
			<span class="flex cursor-pointer space-x-2">
				<Popular />
				<span class="text-lg font-bold">Popular</span>
			</span>
			<span class="flex cursor-pointer space-x-2">
				<All />
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
		{#if auth}
			<HeaderAuth />
		{:else}
			<HeaderNoAuth />
		{/if}
	</div>
</div>
