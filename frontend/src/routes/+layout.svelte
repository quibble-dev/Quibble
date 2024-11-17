<script lang="ts">
	import Header from '$lib/components/header.svelte';

	import '../app.css';
	let { children } = $props();
</script>

<main class="font-sans">
	<Header />
	{@render children()}
</main>
