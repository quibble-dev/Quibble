<script lang="ts">
  import CardIcon from '$lib/components/icons/card.svelte';
  import CompactIcon from '$lib/components/icons/compact.svelte';
  import HotIcon from '$lib/components/icons/hot.svelte';
  import NewIcon from '$lib/components/icons/new.svelte';
  import RocketIcon from '$lib/components/icons/rocket.svelte';
  import TopIcon from '$lib/components/icons/top.svelte';
  import { cn } from '$lib/functions/classnames';
  import { createLayoutTypeStore } from '$lib/stores/layout_type.svelte';

  const layoutTypeStore = createLayoutTypeStore();

  let active_mapping = $derived<{
    filter: keyof typeof mapping.filters;
    view: keyof typeof mapping.view;
  }>({
    filter: 'best',
    view: layoutTypeStore.state
  });

  const mapping = {
    filters: {
      best: { icon: RocketIcon, href: '/' },
      hot: { icon: HotIcon, href: '/hot' },
      new: { icon: NewIcon, href: '/new' },
      top: { icon: TopIcon, href: '/top' }
    },
    view: {
      card: {
        icon: CardIcon,
        onclick: () => layoutTypeStore.update('card')
      },
      compact: {
        icon: CompactIcon,
        onclick: () => layoutTypeStore.update('compact')
      }
    }
  };

  let active_view_icon = $derived(mapping.view[active_mapping.view]);
</script>

<div class="flex items-start justify-between">
  <div class="flex gap-3">
    {#each Object.entries(mapping.filters) as [key, item]}
      {@const is_active = active_mapping.filter === key}
      {@const hide_on_mobile = key === 'top'}

      <div class={cn(hide_on_mobile ? 'hidden' : 'flex', 'flex-col items-center gap-1')}>
        <a href={item.href} aria-label={key} class="flex items-center gap-2">
          <item.icon class={cn(is_active && 'text-primary', 'size-4')} />
          <span class="text-sm font-medium capitalize">{key}</span>
        </a>
        {#if is_active}
          <div class="h-0.5 w-5 rounded-full bg-primary"></div>
        {/if}
      </div>
    {/each}
  </div>
  <div class="flex gap-3">
    <div class="dropdown dropdown-end">
      <div tabindex="0" role="button" class="flex items-center gap-2">
        <active_view_icon.icon class="stroke-primary" />
        <span class="text-sm font-medium capitalize">{active_mapping.view}</span>
        <coreicons-shape-chevron variant="down" class="size-4"></coreicons-shape-chevron>
      </div>
      <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
      <ul
        tabindex="0"
        class="menu dropdown-content z-10 mt-2 gap-1 rounded-2xl bg-base-100 p-1.5"
      >
        {#each Object.entries(mapping.view) as [key, item]}
          {@const is_active = active_mapping.view === key}
          <li>
            <button
              onclick={item.onclick}
              aria-label="{key} view"
              class="flex items-center gap-2 rounded-xl p-2"
            >
              <item.icon
                class={cn(
                  is_active ? 'stroke-primary' : 'stroke-neutral-content',
                  'size-4'
                )}
              />
              <span class="text-sm font-medium capitalize" class:text-primary={is_active}
                >{key}</span
              >
            </button>
          </li>
        {/each}
      </ul>
    </div>
  </div>
</div>
