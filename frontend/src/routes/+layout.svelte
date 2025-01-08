<script lang="ts">
  import type { components } from '$lib/clients/v1';
  import Header from '$lib/components/header.svelte';
  import Modals from '$lib/components/modals/index.svelte';
  import Sidebar from '$lib/components/sidebar.svelte';
  import { cn } from '$lib/functions/classnames';
  import { debounce } from '$lib/functions/debounce';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import '../styles/app.css';
  import '../styles/smiz.css';
  import { defineCustomElements } from '@coreproject-moe/icons/loader';
  import { onMount, type Snippet } from 'svelte';

  type Profile = components['schemas']['Profile'];

  let { children, data }: { children: Snippet; data: { profile: Profile } } = $props();

  let sidebar_show = $state(false);
  let sidebar_shown = $state(false);

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

  const toggle_show_sidebar = () => {
    if (sidebar_shown) return;
    sidebar_show = !sidebar_show;
  };
</script>

<!-- render available models -->
<Modals />
<main class="flex h-dvh w-dvw flex-col font-sans">
  <Header on_menu_click={toggle_show_sidebar} />
  <section class="mt-[3.75rem] flex">
    <!-- sidebar for medium screens -->
    <div class="hidden w-72 md:flex">
      <Sidebar />
    </div>
    <!-- sidebar for small screens with transition -->
    <div
      class="fixed left-0 top-[3.75rem] z-50 flex h-[calc(100dvh-3.75rem)] w-72 transform transition-transform duration-300 md:hidden"
      class:-translate-x-72={!sidebar_show}
      ontransitionstart={() => (sidebar_shown = true)}
      ontransitionend={() => (sidebar_shown = false)}
    >
      <Sidebar />
    </div>
    <!-- background clicker to toggle show_sidebar state (small screens) -->
    <button
      onclick={toggle_show_sidebar}
      class={cn(
        sidebar_show ? 'opacity-100' : 'pointer-events-none opacity-0',
        'fixed z-40 h-[calc(100dvh-3.75rem)] w-dvw bg-base-300/55 transition-opacity duration-300 md:hidden'
      )}
      aria-label="toggle sidebar"
    ></button>
    <div class="mx-auto flex flex-1 xl:max-w-6xl">
      {@render children()}
    </div>
  </section>
</main>
