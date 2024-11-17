<script lang="ts">
	import Header from '$lib/components/header.svelte';

	import '../app.css';
	let { children } = $props();
</script>

<main>
	<Header />
	{@render children()}
</main>
