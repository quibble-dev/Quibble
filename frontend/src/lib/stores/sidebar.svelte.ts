import { browser } from '$app/environment';

type ISidebarStore = Record<string, IQuiblets>;

type IQuiblets = {
  avatar?: string | null | undefined;
  name: string;
  starred?: boolean;
}[];

const stored_sidebar_store = browser ? localStorage.getItem('sidebar_store') : null;

const parsed_stored_sidebar_store: ISidebarStore = stored_sidebar_store
  ? JSON.parse(stored_sidebar_store)
  : {};

const sidebar_state = $state<ISidebarStore>(
  // sort initial data
  Object.fromEntries(
    Object.entries(parsed_stored_sidebar_store).map(([key, quiblets]) => [
      key,
      get_sorted_quiblets(quiblets)
    ])
  )
);

function sync_to_localstorage() {
  if (browser) {
    localStorage.setItem('sidebar_store', JSON.stringify(sidebar_state));
  }
}

function get_sorted_quiblets(quiblets: IQuiblets) {
  return [...quiblets].sort((a, b) => {
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
    add_quiblet(type: string, quiblet: IQuiblets[number]) {
      // initialize empty array for new type type
      if (!sidebar_state[type]) {
        sidebar_state[type] = [];
      }

      const exists = sidebar_state[type].some((q) => q.name === quiblet.name);
      if (exists) return;

      sidebar_state[type] = get_sorted_quiblets([
        ...sidebar_state[type],
        { ...quiblet, starred: false }
      ]);
      sync_to_localstorage();
    },
    toggle_star(type: string, name: string) {
      if (!sidebar_state[type]) return;

      sidebar_state[type] = get_sorted_quiblets(
        sidebar_state[type].map((q) =>
          q.name === name ? { ...q, starred: !q.starred } : q
        )
      );
      sync_to_localstorage();
    }
  };
}
