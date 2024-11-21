<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	import { defineCustomElements } from '@coreproject-moe/icons/loader';
	import Header from '$lib/components/header.svelte';
	import Sidebar from '$lib/components/sidebar.svelte';

	let { children } = $props();

	onMount(() => {
		defineCustomElements();
	});
</script>

<main class="font-sans">
	<Header />
	<section class="flex w-full gap-5">
		<Sidebar />
		{@render children()}
	</section>
</main>
