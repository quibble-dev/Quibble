<script lang="ts">
	import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
	import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';

	let { modal = $bindable() } = $props();

	let username = $state('anime');
	let tab = $state('login');
</script>

<dialog class="modal modal-bottom sm:modal-middle" bind:this={modal}>
	<div class="modal-box flex  sm:w-[480px]  select-none flex-col sm:p-10">
		<span class="flex w-full items-center justify-center gap-2">
			<QuibbleLogo class="size-7" />
			<QuibbleTextLogo class="h-7 w-auto" />
		</span>

		{#if tab == 'login'}
			<div class="flex flex-col">
				<p class="py-8 text-center text-xl font-bold">
					Join in, share your take, and<br /> make some waves!
				</p>
				<button class="btn btn-neutral w-full gap-2">
					<coreicons-logo-github class="size-5"></coreicons-logo-github>
					Continue with Google
				</button>

				<div class="divider text-xs">OR</div>

				<label for="email" class="text-bold py-3">Email</label>
				<input type="email" name="email" class="input bg-neutral w-full text-sm" />
				<label for="password" class="text-bold py-3">Password</label>
				<input type="password" name="password" class="input bg-neutral w-full text-sm" />

				<button type="submit" class="btn btn-primary my-4" onclick={()=> tab = "profile"}>Continue</button>

				<p class="text-center text-sm">
					By continuing, you agree to the <span class="text-cyan-400">Terms of use</span>,
					<span class="text-cyan-400">Privacy</span>
					and <span class="text-cyan-400">Policy</span> Preplaced.
				</p>
			</div>
		{:else}
			<div class="flex flex-col">
				
				<p class="py-4 text-center text-xl font-bold">Create new Profile</p>

				<div class="flex">
					<!-- svelte-ignore a11y_img_redundant_alt -->
					<img
						src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
						alt="Profile Picture"
						class="aspect-1 bg-neutral w-40 h-40 rounded-lg"
					/>
					<div class="ml-5 flex flex-col">
						<h6 class="font-bold">Picture</h6>
						<p class="mb-4 text-sm text-neutral-400">Click or drag and drop to see preview</p>
						<h6 class="mb-2 font-bold">Profile preview</h6>
						<div class="flex items-center">
							<!-- svelte-ignore a11y_img_redundant_alt -->
							<img
								src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
								alt="Profile Picture"
								class=" aspect-1 bg-neutral w-12 rounded-xl"
							/>
							<h6 class="ml-4 font-bold">u/{username}</h6>
						</div>
					</div>
				</div>

				<label for="username" class="text-bold py-3">Username</label>
				<input
					type="text"
					name="username"
					class="input bg-neutral w-full text-sm"
					bind:value={username}
				/>

				<button type="submit" class="btn btn-primary my-4" onclick={()=> tab = "login"}>Continue</button>
			</div>
		{/if}
	</div>
	<form method="dialog" class="modal-backdrop bg-black/20">
		<button>close</button>
	</form>
</dialog>
