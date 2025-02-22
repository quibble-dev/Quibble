<script lang="ts">
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import ModalAuth from './modal-auth/index.svelte';
  import ModalCreateCommunity from './modal-create-community/index.svelte';

  const authStore = createAuthStore();
</script>

{#if authStore.state.is_authenticated}
  <ModalCreateCommunity />
{:else}
  <ModalAuth />
{/if}
