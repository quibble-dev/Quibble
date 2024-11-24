<script lang="ts">
	import { close_modal, get_modals_state } from '$lib/stores/modals.svelte';
	import type { FormsState, FormSubmitData } from './types';

	const login_form = import('./login_form.svelte');

	let forms = { login: login_form };
	let _form = $state<keyof typeof forms>('login');

	let current_form = $derived(forms[_form]);

	const initial_forms_state = Object.fromEntries(
		Object.keys(forms).map((key) => [key, {}])
	) as FormsState;

	let forms_state = $state<FormsState>(initial_forms_state);

  $inspect(forms_state);

	function on_submit(data: FormSubmitData) {
		forms_state[_form] = data;
	}

	let dialog_element: HTMLDialogElement | undefined = undefined;

	$effect(() => {
		if (get_modals_state().get('auth')) {
			dialog_element?.showModal();
		}
	});
</script>

<dialog
	class="modal modal-bottom sm:modal-middle"
	bind:this={dialog_element}
	onclose={() => close_modal('auth')}
>
	<div class="modal-box !w-[25rem]">
		{#await current_form then Form}
			<Form.default {forms_state} {on_submit} />
		{/await}
	</div>
	<form method="dialog" class="modal-backdrop bg-base-300/25">
		<button>close</button>
	</form>
</dialog>
