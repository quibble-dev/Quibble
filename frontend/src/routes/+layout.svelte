<script lang="ts">
	import { onMount } from 'svelte';
	import { defineCustomElements } from '@coreproject-moe/icons/loader';
	import Header from '$lib/components/header.svelte';

	import '../app.css';
	import LeftPanel from '$lib/components/LeftPanel/LeftPanel.svelte';
	import RightPanel from '$lib/components/RightPanel/rightPanel.svelte';

	let { children } = $props();

	onMount(() => {
		defineCustomElements();
	});
</script>

<main class="font-sans">
	<Header />
	<LeftPanel />
	<RightPanel />

	{@render children()}
</main>
