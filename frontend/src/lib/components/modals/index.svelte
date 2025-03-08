<script lang="ts">
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import AuthModal from './auth/index.svelte';

  const authStore = createAuthStore();
</script>

{#if !authStore.state.is_authenticated}
  <AuthModal />
{/if}
