import { browser } from '$app/environment';

type Sidebar = Record<string, Community[]>;
type Community = {
  avatar?: string | null | undefined;
  name: string;
  starred?: boolean;
};

const MAX_ITEMS_SHOWN = 4;

const stored_sidebar = browser ? localStorage.getItem('sidebar') : null;
const parsed_sidebar: Sidebar = stored_sidebar ? JSON.parse(stored_sidebar) : {};

const sidebar = $state<Sidebar>(
  // sort initial data
  Object.fromEntries(
    Object.entries(parsed_sidebar).map(([key, community]) => [
      key,
      key === 'recents'
        ? get_sorted_communities(community, true)
        : get_sorted_communities(community)
    ])
  )
);

function sync_to_localstorage() {
  if (browser) {
    localStorage.setItem('sidebar', JSON.stringify(sidebar));
  }
}

function get_sorted_communities(
  communities: Community[],
  sortByName: boolean = true,
  starred_only: boolean = false
) {
  const filteredCommunities = starred_only
    ? communities.filter((community) => community.starred)
    : communities;

  return [...filteredCommunities].sort((a, b) => {
    if (a.starred !== b.starred) {
      return b.starred ? 1 : -1;
    }
    return sortByName ? a.name.localeCompare(b.name) : 1;
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

      // Recent items should not be sorted by name.
      if (type == 'recent') {
        sidebar[type] = get_sorted_communities(
          [{ ...community, starred: false }, ...sidebar[type]],
          false
        ).slice(0, MAX_ITEMS_SHOWN);
      } else {
        sidebar[type] = get_sorted_communities([
          ...sidebar[type],
          { ...community, starred: false }
        ]).slice(0, MAX_ITEMS_SHOWN);
      }

      sync_to_localstorage();
    },
    toggle_star(type: string, name: string) {
      if (!sidebar[type]) return;

      sidebar[type] = get_sorted_communities(
        sidebar[type].map((c) => (c.name === name ? { ...c, starred: !c.starred } : c))
      );
      sync_to_localstorage();
    },
    clear_recents() {
      sidebar['recent'] = get_sorted_communities(sidebar['recent'] as Community[], false, true);
      sync_to_localstorage();
    }
  };
}
