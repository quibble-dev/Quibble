<script lang="ts">
	import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
	import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
	import { cn } from '$lib/functions/classnames';
	import type { FormProps } from '../types';

	let { forms_state }: FormProps = $props();

	let pending = $state(false);

	console.log((forms_state.login as { email: string }).email);
</script>

<div class="flex flex-col gap-4">
	<div class="flex flex-col items-center justify-center gap-4">
		<div class="flex items-center gap-2">
			<QuibbleLogo class="size-7" />
			<QuibbleTextLogo class="h-7 w-auto" />
		</div>
		<p class="text-center font-medium">Create new Profile</p>
	</div>
	<form class="flex flex-col gap-3">
		<!-- hack to prevent file input getting autofocused -->
		<input type="text" class="absolute -z-10 opacity-0" />
		<label class="form-control">
			<div class="label">
				<span class="label-text">Avatar (optional):</span>
			</div>
			<input type="file" class="file-input" />
		</label>
		<label class="input input-bordered flex items-center gap-2">
			<coreicons-shape-at-sign class="size-4"></coreicons-shape-at-sign>
			<input
				type="text"
				name="username"
				required
				class="grow border-none p-2 text-sm font-medium focus:ring-0"
				placeholder="Username*"
			/>
		</label>
		<div class="form-control w-max">
			<label class="label flex cursor-pointer items-center gap-2 p-0">
				<input type="checkbox" class="checkbox checkbox-xs bg-transparent" checked />
				<span class="label-text">Use this profile</span>
			</label>
		</div>
		<button
			type="submit"
			class={cn(pending && 'btn-active pointer-events-none', 'btn btn-primary')}
		>
			{#if pending}
				Logging in
				<span class="loading loading-spinner loading-xs"></span>
			{:else}
				Create profile
				<coreicons-shape-chevron variant="right" class="size-4"></coreicons-shape-chevron>
			{/if}
		</button>
	</form>
	<p class="text-center text-xs">You can edit your profile on settings page later.</p>
</div>
