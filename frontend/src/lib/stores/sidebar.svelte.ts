import { browser } from '$app/environment';

type SidebarStore = Record<string, Community>;

type Community = {
  avatar?: string | null | undefined;
  name: string;
  starred?: boolean;
}[];

const stored_sidebar_store = browser ? localStorage.getItem('sidebar_store') : null;

const parsed_stored_sidebar_store: SidebarStore = stored_sidebar_store
  ? JSON.parse(stored_sidebar_store)
  : {};

const sidebar_state = $state<SidebarStore>(
  // sort initial data
  Object.fromEntries(
    Object.entries(parsed_stored_sidebar_store).map(([key, community]) => [
      key,
      get_sorted_communities(community)
    ])
  )
);

function sync_to_localstorage() {
  if (browser) {
    localStorage.setItem('sidebar_store', JSON.stringify(sidebar_state));
  }
}

function get_sorted_communities(community: Community) {
  return [...community].sort((a, b) => {
    if (a.starred !== b.starred) {
      return b.starred ? 1 : -1;
    }
    return a.name.localeCompare(b.name);
  });
}

export function createSidebarStore() {
  return {
    get state() {
      return sidebar_state;
    },
    add_community(type: string, community: Community[number]) {
      // initialize empty array for new type type
      if (!sidebar_state[type]) {
        sidebar_state[type] = [];
      }

      const exists = sidebar_state[type].some((c) => c.name === community.name);
      if (exists) return;

      sidebar_state[type] = get_sorted_communities([
        ...sidebar_state[type],
        { ...community, starred: false }
      ]);
      sync_to_localstorage();
    },
    toggle_star(type: string, name: string) {
      if (!sidebar_state[type]) return;

      sidebar_state[type] = get_sorted_communities(
        sidebar_state[type].map((c) =>
          c.name === name ? { ...c, starred: !c.starred } : c
        )
      );
      sync_to_localstorage();
    }
  };
}
