<script lang="ts">
	import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
	import QuibbleTextLogo from '$lib/components/icons/logos/quibble_text.svelte';
	import type { FormProps } from '../types';
	import Avatar from '$lib/components/ui/avatar.svelte';
	import { onMount } from 'svelte';
	import { apiFetch } from '$lib/utils/api';
	import type { Profile } from '$lib/types/user';
	import { enhance } from '$app/forms';
	import type { SubmitFunction } from '@sveltejs/kit';

	let { forms_state, goto_form }: FormProps = $props();

	let pending = $state(false);
	let status_text = $state<string | null>(null);

	let profiles = $state<Profile[]>([]);

	const handle_submit: SubmitFunction = async () => {
		pending = true;
		status_text = 'Setting up profile...';
		return async ({ update }) => {
			try {
				await update();
			} finally {
				pending = false;
				status_text = null;
			}
		};
	};

	onMount(async () => {
		try {
			pending = true;
			status_text = 'Fetching profiles...';
			profiles = await apiFetch<Profile[]>('v1/user/me/profiles/', {
				headers: {
					Authorization: `Bearer ${(forms_state.login as { token: string }).token}`
				}
			});
		} catch (err) {
			console.error(err);
		} finally {
			pending = false;
			status_text = null;
		}
	});
</script>

{#if pending}
	<span class="loading loading-spinner loading-md absolute right-2.5 top-2.5"></span>
{/if}
<div class="flex flex-col gap-4">
	<div class="flex flex-col items-center justify-center gap-4">
		<div class="flex items-center gap-2">
			<QuibbleLogo class="size-7" />
			<QuibbleTextLogo class="h-7 w-auto" />
		</div>
		<p class="text-center font-medium">
			{status_text ?? "Who's quibbling?"}
		</p>
	</div>
	<div
		class="flex flex-wrap items-center justify-center gap-x-6 gap-y-4 self-center"
		class:pointer-events-none={pending}
	>
		{#each profiles as profile}
			<form
				method="POST"
				action="/settings/profile?/select"
				use:enhance={handle_submit}
			>
				<input type="hidden" name="profile_id" value={profile.id} />
				<button type="submit" class="flex flex-col items-center justify-center gap-2.5">
					<Avatar
						class="!size-20 !rounded-2xl"
						parent_class="grid size-20 place-items-center rounded-2xl bg-neutral outline outline-offset-4 outline-neutral transition-[outline] hover:outline-neutral-content"
						fallback_text_class="text-4xl"
						src={profile.avatar}
						alt={profile.username}
					/>
					<span class="text-xs font-medium">u/{profile.username}</span>
				</button>
			</form>
		{/each}
		{#if !(profiles.length >= 3)}
			<button
				onclick={() => goto_form('profile_create')}
				class="flex flex-col items-center gap-2.5"
			>
				<div
					class="grid size-20 place-items-center rounded-2xl bg-neutral outline outline-dashed outline-offset-4 outline-neutral transition-[outline] hover:outline-neutral-content/25"
				>
					<coreicons-shape-plus variant="no-border" class="size-8"></coreicons-shape-plus>
				</div>
				<span class="text-xs font-medium">Create new</span>
			</button>
		{/if}
	</div>
</div>
