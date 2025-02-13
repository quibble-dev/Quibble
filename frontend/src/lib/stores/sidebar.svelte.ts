import { browser } from '$app/environment';
import { SIDEBAR_MAX_ITEMS_LIMIT } from '$lib/constants/limits';

type Sidebar = Record<string, Community[]>;
type Community = {
  id: number;
  avatar?: string | null | undefined;
  name: string;
  starred?: boolean;
  timestamp?: number;
};

const stored_sidebar = browser ? localStorage.getItem('sidebar') : null;
const parsed_sidebar: Sidebar = stored_sidebar ? JSON.parse(stored_sidebar) : {};

const sidebar = $state<Sidebar>(
  // sort initial data
  Object.fromEntries(
    Object.entries(parsed_sidebar).map(([key, community]) => [
      key,
      get_sorted_communities(community)
    ])
  )
);

function sync_to_localstorage() {
  if (browser) {
    localStorage.setItem('sidebar', JSON.stringify(sidebar));
  }
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

export function createSidebarStore() {
  return {
    get state() {
      return sidebar;
    },
    add_community(type: string, community: Community) {
      // initialize empty array for new type type
      if (!sidebar[type]) {
        sidebar[type] = [];
      }

      const exists = sidebar[type].some((c) => c.name === community.name);
      if (exists) return;

      const community_with_timestamp: Community = {
        ...community,
        starred: false,
        timestamp: Date.now()
      };
      sidebar[type] = get_sorted_communities([community_with_timestamp, ...sidebar[type]]).slice(
        0,
        SIDEBAR_MAX_ITEMS_LIMIT
      );
      sync_to_localstorage();
    },
    toggle_star(type: string, name: string) {
      if (!sidebar[type]) return;

      sidebar[type] = get_sorted_communities(
        sidebar[type].map((c) => (c.name === name ? { ...c, starred: !c.starred } : c))
      );
      sync_to_localstorage();
    },
    clear(type: string) {
      if (!sidebar[type]) return;

      sidebar[type] = get_sorted_communities(sidebar[type].filter((c) => c.starred === true));
      sync_to_localstorage();
    }
  };
}
