<script lang="ts">
	import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
	import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
	import type { FormProps } from './types';

	let { forms_state }: FormProps = $props();

	console.log(forms_state);
</script>

<span class="flex w-full items-center justify-center gap-2">
	<QuibbleLogo class="size-7" />
	<QuibbleTextLogo class="h-7 w-auto" />
</span>

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
	<input type="email" name="email" class="input w-full bg-neutral text-sm" />
	<label for="password" class="text-bold py-3">Password</label>
	<input type="password" name="password" class="input w-full bg-neutral text-sm" />

	<button type="submit" class="btn btn-primary my-4">Continue</button>

	<p class="text-center text-sm">
		By continuing, you agree to the <span class="text-cyan-400">Terms of use</span>,
		<span class="text-cyan-400">Privacy</span>
		and <span class="text-cyan-400">Policy</span> Preplaced.
	</p>
</div>
