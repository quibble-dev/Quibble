<script lang="ts">
  import { page } from '$app/state';
  import CardIcon from '$lib/components/icons/card.svelte';
  import CompactIcon from '$lib/components/icons/compact.svelte';
  import HotIcon from '$lib/components/icons/hot.svelte';
  import NewIcon from '$lib/components/icons/new.svelte';
  import RocketIcon from '$lib/components/icons/rocket.svelte';
  import TopIcon from '$lib/components/icons/top.svelte';
  import { cn } from '$lib/functions/classnames';
  import { createLayoutTypeStore } from '$lib/stores/layout-type.svelte';

  type FilterType = keyof typeof mapping.filters;

  const layoutTypeStore = createLayoutTypeStore();

  let active_view = $derived<keyof typeof mapping.view>(layoutTypeStore.state);
  let active_filter = $derived.by<FilterType>(() => {
    const sort_param = page.url.searchParams.get('sort');
    if (sort_param && ['best', 'hot', 'new'].includes(sort_param)) return sort_param as FilterType;
    return 'best';
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

  // active view icon for rendering
  let ActiveViewIcon = $derived(mapping.view[active_view].icon);
</script>

<div class="flex items-start justify-between">
  <div class="flex gap-3">
    {#each Object.entries(mapping.filters) as [key, item]}
      {@const is_active = active_filter === key}
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
        <ActiveViewIcon class="stroke-primary" />
        <span class="text-sm font-medium capitalize">{active_view}</span>
        <coreicons-shape-chevron variant="down" class="size-4"></coreicons-shape-chevron>
      </div>
      <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
      <ul tabindex="0" class="menu dropdown-content z-10 mt-2 gap-1 rounded-2xl bg-base-100 p-1.5">
        {#each Object.entries(mapping.view) as [key, item]}
          {@const is_active = active_view === key}
          <li>
            <button
              onclick={item.onclick}
              aria-label="{key} view"
              class="flex items-center gap-2 rounded-xl p-2"
            >
              <item.icon
                class={cn(is_active ? 'stroke-primary' : 'stroke-neutral-content', 'size-4')}
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
