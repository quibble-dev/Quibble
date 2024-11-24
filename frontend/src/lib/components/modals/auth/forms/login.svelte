<script lang="ts">
	import GoogleLogo from '$lib/components/icons/logos/google.svelte';
	import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
	import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
	import { cn } from '$lib/functions/classnames';
	import type { FormProps } from '../types';

	let { on_submit, goto_form }: FormProps = $props();

	let pending = $state(false);

	async function handle_submit(e: SubmitEvent) {
		e.preventDefault();
		pending = true;
		try {
			const form_data = new FormData(e.target as HTMLFormElement);
			// handle login logic here then call on_submit
			await new Promise((resolve) => setTimeout(resolve, 2000));

			on_submit({
				email: form_data.get('email') as string,
				password: form_data.get('password') as string
			});
			// next form
			goto_form('profile_select');
		} finally {
			pending = false;
		}
	}
</script>

<div class="flex flex-col gap-4">
	<div class="flex flex-col items-center justify-center gap-4">
		<div class="flex items-center gap-2">
			<QuibbleLogo class="size-7" />
			<QuibbleTextLogo class="h-7 w-auto" />
		</div>
		<p class="text-center font-medium">
			Join in, share your take, and<br /> make some waves!
		</p>
	</div>
	<button class="btn btn-neutral hover:btn-ghost">
		<GoogleLogo class="size-5" />
		Continue with Google
	</button>
	<div class="divider my-0 text-xs font-bold">OR</div>
	<form class="flex flex-col gap-3" onsubmit={handle_submit}>
		<label class="input input-bordered flex items-center gap-2">
			<coreicons-shape-mail class="size-4"></coreicons-shape-mail>
			<input
				type="email"
				name="email"
				required
				class="grow border-none p-2 text-sm font-medium focus:ring-0"
				placeholder="Email address*"
			/>
		</label>
		<label class="input input-bordered flex items-center gap-2">
			<coreicons-shape-lock class="size-4"></coreicons-shape-lock>
			<input
				type="password"
				name="password"
				required
				minlength="8"
				class="grow border-none p-2 text-sm font-medium focus:ring-0"
				placeholder="Password*"
			/>
		</label>
		<button
			type="submit"
			class={cn(pending && 'btn-active pointer-events-none', 'btn btn-primary')}
		>
			{#if pending}
				Logging in
				<span class="loading loading-spinner loading-xs"></span>
			{:else}
				Log in
				<coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
			{/if}
		</button>
	</form>
	<p class="text-center text-xs">
		By continuing, you agree to the <a
			href="/support/terms-and-conditions"
			class="font-semibold text-info">Terms of use</a
		>,
		<a href="/support/privary" class="font-semibold text-info">Privacy</a>
		and <a href="/support/policy" class="font-semibold text-info">Policy</a> Preplaced.
	</p>
</div>
