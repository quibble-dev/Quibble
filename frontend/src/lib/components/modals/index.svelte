<script lang="ts">
  import { authStore } from '$lib/stores/auth.svelte';
  import AuthModal from './auth/index.svelte';
</script>

{#if !authStore.value.is_authenticated}
  <AuthModal />
{/if}
