<script lang="ts">
	import { onMount } from 'svelte';
	import { defineCustomElements } from '@coreproject-moe/icons/loader';
	import Header from '$lib/components/header.svelte';

	import '../app.css';
	let { children } = $props();

	onMount(() => {
		defineCustomElements();
	});
</script>

<main class="font-sans">
	<Header />
	{@render children()}
</main>
