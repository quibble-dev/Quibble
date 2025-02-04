<script lang="ts">
  import Header from '$lib/components/header.svelte';
  import Sidebar from '$lib/components/sidebar.svelte';
  import Toaster from '$lib/components/ui/toast';
  import { cn } from '$lib/functions/classnames';
  import Modals from '$lib/modals/index.svelte';
  import { createAuthStore } from '$lib/stores/auth.svelte';
  import '../styles/app.css';
  import '../styles/smiz.css';
  import { defineCustomElements } from '@coreproject-moe/icons/loader';
  import { onMount, type Snippet } from 'svelte';

  // eslint-disable-next-line no-undef
  let { children, data }: { children: Snippet; data: App.Locals } = $props();

  let sidebar_show = $state(false);
  let sidebar_shown = $state(false);

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

  const toggle_show_sidebar = () => {
    if (sidebar_shown) return;
    sidebar_show = !sidebar_show;
  };
</script>

<!-- render toasts -->
<!-- https://stackoverflow.com/questions/77099074/layering-toast-alerts-above-dialog-modal -->
<Toaster />
<!-- render available models -->
<Modals />

<!-- main ui layout -->
<main class="flex h-dvh w-dvw flex-col font-sans">
  <!-- header section -->
  <Header on_menu_click={toggle_show_sidebar} />

  <!-- main body section -->
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

    <!-- render children content -->
    <div class="mx-auto flex flex-1 xl:max-w-6xl">
      {@render children()}
    </div>
  </section>
</main>
