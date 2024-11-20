<script>
	import AboutIcon from '$lib/components/icons/AboutIcon.svelte';
	import Filter from '$lib/components/icons/FilterIcon.svelte';
	import HelpIcon from '$lib/components/icons/HelpIcon.svelte';
	import PlusCircle from '$lib/components/icons/PlusCircle.svelte';
	import UserListItem from '../User/UserListItem.svelte';
	import User from '../User/UserListItem.svelte';

	const YEAR = new Date().getFullYear();
</script>

<div class="bg-base-300 fixed h-screen w-64  px-5">
	<div class=" py-1">
		<!-- Filter and Create -->
		<div class="mb-3 py-2">
			<h1 class="text-base-content mb-3 text-xl font-semibold">Communities</h1>
			<div class="">
				<label class="input bg-base-300 input-bordered flex h-10 items-center pl-0 ">
					<input
						type="text"
						class="input-sm w-ful grow placeholder:text-base placeholder:font-bold border-none focus:ring-0 focus:border-none"
						placeholder="Filter"
					/>
					<Filter />
				</label>
			</div>

			<span class="text-base-content mt-3 flex cursor-pointer space-x-2 text-xs font-medium">
				<PlusCircle />
				<span>Create Communities</span>
			</span>
		</div>
		<!-- Favourite -->
		<div class="w-full">
			<h1 class="text-base-content/50 font-medium">Favourites</h1>
			<div class="py-3">
				<UserListItem img="https://i.pinimg.com/736x/40/d4/71/40d47153ab90765038b9b1f4116abd99.jpg" name="megan fox" stared={true} />
				<UserListItem
					img="https://avatars.githubusercontent.com/u/114811070?v=4"
					name="suneeth"
					stared={true}
				/>
			</div>
		</div>
		<!-- Your Communities -->
		<div class="w-full">
			<h1 class="text-base-content/50 font-medium">Your Communities</h1>
			<div class="py-3">
				<User img="https://i.pinimg.com/736x/ea/14/85/ea14855f10b6afeb4573145a6dffafe6.jpg" name="ortega" stared={true} />
				<User
					img="https://avatars.githubusercontent.com/u/102005928?v=4"
					name="danish"
					stared={false}
				/>
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
					<HelpIcon />
					<span class="text-base font-bold">Help</span>
				</span>
			</div>
		</div>

		<p class="mt-5 text-[10px] font-normal">Quibble © {YEAR}. All rights reserved.</p>
	</div>
</div>
