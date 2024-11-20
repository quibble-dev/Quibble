<script>
	import AboutIcon from '$lib/components/icons/AboutIcon.svelte';
	import Filter from '$lib/components/icons/FilterIcon.svelte';
	import HelpIcon from '$lib/components/icons/HelpIcon.svelte';
	import PlusCircle from '$lib/components/icons/PlusCircle.svelte';
	import { femaleUsers, maleUsers } from '$lib/data/moks/user';
	import UserListItem from '../User/UserListItem.svelte';
	import User from '../User/UserListItem.svelte';

	const YEAR = new Date().getFullYear();
</script>

<div class="bg-base-300 fixed bottom-0 left-0 top-16 h-screen w-64 px-5 pb-16 max-h-screen scrollbar-thin scrollbar-thumb-transparent scrollbar-track-sky-300/0 overflow-y-auto ">
	<div class=" py-1">
		<!-- Filter and Create -->
		<div class="mb-3 py-2">
			<h1 class="text-base-content mb-3 text-xl font-semibold">Communities</h1>
			<div class="">
				<label class="input bg-base-300 input-bordered flex h-10 items-center pl-0">
					<input
						type="text"
						class="input-sm w-ful grow border-none placeholder:text-base placeholder:font-bold focus:border-none focus:ring-0"
						placeholder="Filter"
					/>
					<Filter />
				</label>
			</div>

			<span class="text-base-content mt-3 flex cursor-pointer space-x-2 text-xs font-medium">
				<coreicons-shape-plus variant="circle" class="size-4"></coreicons-shape-plus>
				<span>Create Communities</span>
			</span>
		</div>
		<!-- Favourite -->
		<div class="w-full">
			<h1 class="text-base-content/50 font-medium">Favourites</h1>
			<div class="py-3">
				{#each femaleUsers as user}
					<UserListItem img={user.img} name={user.name} stared={user.stared} />
				{/each}
			</div>
		</div>
		<!-- Your Communities -->
		<div class="w-full">
			<h1 class="text-base-content/50 font-medium">Your Communities</h1>
			<div class="py-3">
				{#each maleUsers as user}
					<UserListItem img={user.img} name={user.name} stared={user.stared} />
				{/each}
			</div>
		</div>
		<!-- Resources -->
		<div class="">
			<h1 class="text-base-content/50 font-mdeium">Resources</h1>
			<div class="flex flex-col gap-2 py-3">
				<span class="flex cursor-pointer items-center space-x-2">
					<AboutIcon />
					<span class="text-base font-semibold">About Quibble</span>
				</span>
				<span class="flex cursor-pointer items-center space-x-2">
					<coreicons-shape-help-circle class="size-6"></coreicons-shape-help-circle>
					<span class="text-base font-bold">Help</span>
				</span>
			</div>
		</div>

		<p class="mt-5 text-[10px] font-normal">Quibble © {YEAR}. All rights reserved.</p>
	</div>
</div>
