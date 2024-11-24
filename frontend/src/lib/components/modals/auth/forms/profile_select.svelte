<script lang="ts">
	import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
	import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
	import type { FormProps } from '../types';
	import my_profiles from '$lib/data/mock/my_profiles.json';
	import Avatar from '$lib/components/ui/avatar.svelte';

	let { forms_state, goto_form }: FormProps = $props();

	console.log((forms_state.login as { email: string }).email);
</script>

<div class="flex flex-col gap-4">
	<div class="flex flex-col items-center justify-center gap-4">
		<div class="flex items-center gap-2">
			<QuibbleLogo class="size-7" />
			<QuibbleTextLogo class="h-7 w-auto" />
		</div>
		<p class="text-center font-medium">Who's quibbling?</p>
	</div>
	<div class="flex flex-wrap items-center justify-center gap-x-8 gap-y-4 self-center">
		{#each my_profiles as profile}
			<button class="flex flex-col justify-center gap-2.5">
				<Avatar
					class="!size-20 !rounded-2xl"
					parent_class="outline outline-accent/75 hover:outline-accent transition-[outline] duration-300 rounded-2xl outline-offset-4"
					src={profile.avatar}
					alt={profile.username}
				/>
				<span class="text-xs font-medium">q/{profile.username}</span>
			</button>
		{/each}
		<button
			onclick={() => goto_form('profile_create')}
			class="flex flex-col justify-center gap-2.5"
		>
			<div
				class="grid size-20 place-items-center rounded-2xl bg-neutral outline outline-offset-4 outline-neutral transition-[outline] hover:outline-neutral-content/25"
			>
				<coreicons-shape-plus variant="no-border" class="size-8"></coreicons-shape-plus>
			</div>
			<span class="text-xs font-medium">Create new</span>
		</button>
	</div>
</div>
