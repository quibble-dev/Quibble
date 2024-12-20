<script lang="ts">
  import '../app.css';
  import { onMount, type Snippet } from 'svelte';
  import { defineCustomElements } from '@coreproject-moe/icons/loader';
  import Header from '$lib/components/header.svelte';
  import Sidebar from '$lib/components/sidebar.svelte';
  import Modals from '$lib/components/modals/index.svelte';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import type { components } from '$lib/clients/v1';

  type Profile = components['schemas']['Profile'];

  let { children, data }: { children: Snippet; data: { profile: Profile } } = $props();

  const authStore = createAuthStore();

  $effect.pre(() => {
    authStore.update({
      profile: data.profile,
      is_authenticated: !!data.profile
    });
  });

  onMount(() => {
    defineCustomElements();
  });
</script>

<Modals />
<main class="flex h-dvh w-dvw flex-col font-sans">
  <Header />
  <section class="mt-[3.75rem] flex">
    <div class="w-72">
      <Sidebar />
    </div>
    <div class="mx-auto flex flex-1 xl:max-w-6xl">
      {@render children()}
    </div>
  </section>
</main>
