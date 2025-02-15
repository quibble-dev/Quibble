<script lang="ts">
  import Toaster from '$lib/components/ui/toast';
  import Modals from '$lib/modals/index.svelte';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import '../styles/app.css';
  import '../styles/smiz.css';
  import { defineCustomElements } from '@coreproject-moe/icons/loader';
  import { onMount, type Snippet } from 'svelte';

  // eslint-disable-next-line no-undef
  let { children, data }: { children: Snippet; data: App.Locals } = $props();

  const authStore = createAuthStore();

  $effect(() => {
    authStore.update({
      is_authenticated: !!data.profile,
      profile: data.profile
    });
  });

  onMount(() => {
    defineCustomElements();
  });
</script>

<!-- render toasts -->
<!-- https://stackoverflow.com/questions/77099074/layering-toast-alerts-above-dialog-modal -->
<Toaster />
<!-- render available models -->
<Modals />

<!-- main ui layout -->
<main class="flex h-dvh flex-col font-sans">
  {@render children()}
</main>
