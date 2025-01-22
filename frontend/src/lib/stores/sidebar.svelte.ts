import { browser } from '$app/environment';

type Sidebar = Record<string, Community[]>;
type Community = {
  avatar?: string | null | undefined;
  name: string;
  starred?: boolean;
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
    return a.name.localeCompare(b.name);
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

      sidebar[type] = get_sorted_communities([...sidebar[type], { ...community, starred: false }]);
      sync_to_localstorage();
    },
    toggle_star(type: string, name: string) {
      if (!sidebar[type]) return;

      sidebar[type] = get_sorted_communities(
        sidebar[type].map((c) => (c.name === name ? { ...c, starred: !c.starred } : c))
      );
      sync_to_localstorage();
    }
  };
}
