import { browser } from '$app/environment';
import { SIDEBAR_MAX_ITEMS_LIMIT } from '$lib/constants/limits';

// internal types
type SidebarStore = Record<string, Community[]>;
type Community = {
  id: number;
  avatar?: string | null | undefined;
  name: string;
  starred?: boolean;
  timestamp?: number;
};

// constants
const SIDEBAR_LOCALSTORAGE_KEY = 'sidebar-store';

// helper functions
function get_stored_sidebar_store(): SidebarStore {
  if (!browser) return {};

  const stored = localStorage.getItem(SIDEBAR_LOCALSTORAGE_KEY);
  return stored ? JSON.parse(stored) : {};
}

function get_sorted_communities(communities: Community[]) {
  return [...communities].sort((a, b) => {
    if (a.starred !== b.starred) {
      return b.starred ? 1 : -1;
    }
    // newset first even if both are starred
    return (b.timestamp ?? 0) - (a.timestamp ?? 0);
  });
}

function create_sidebar_store() {
  const sidebar_store = $state<SidebarStore>(
    // sort initial data
    Object.fromEntries(
      Object.entries(get_stored_sidebar_store()).map(([key, community]) => [
        key,
        get_sorted_communities(community)
      ])
    )
  );

  $effect.root(() => {
    $effect(() => {
      if (!browser) return;
      localStorage.setItem(SIDEBAR_LOCALSTORAGE_KEY, JSON.stringify(sidebar_store));
    });
  });

  return {
    get value() {
      return sidebar_store;
    },
    add_community(type: string, community: Community) {
      // initialize empty array for new type type
      if (!sidebar_store[type]) sidebar_store[type] = [];
      // if community already exists in store
      if (sidebar_store[type].some((c) => c.name === community.name)) return;

      const community_with_timestamp: Community = {
        ...community,
        starred: false,
        timestamp: Date.now()
      };

      sidebar_store[type] = get_sorted_communities([
        community_with_timestamp,
        ...sidebar_store[type]
      ]).slice(0, SIDEBAR_MAX_ITEMS_LIMIT);
    },
    toggle_star(type: string, name: string) {
      // guard clause
      if (!sidebar_store[type]) return;
      sidebar_store[type] = get_sorted_communities(
        sidebar_store[type].map((c) => (c.name === name ? { ...c, starred: !c.starred } : c))
      );
    },
    clear(type: string) {
      // guard clause
      if (!sidebar_store[type]) return;
      sidebar_store[type] = get_sorted_communities(
        sidebar_store[type].filter((c) => c.starred === true)
      );
    }
  };
}

// initialize store
export const sidebar_store = create_sidebar_store();
