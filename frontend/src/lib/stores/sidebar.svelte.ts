import { browser } from '$app/environment';

type ISidebarStore = Record<string, IQuiblets>;

type IQuiblets = {
  avatar?: string | null | undefined;
  name: string;
  starred: boolean;
}[];

const stored_sidebar_store = browser ? localStorage.getItem('sidebar_store') : null;

const parsed_stored_quiblets: ISidebarStore = stored_sidebar_store
  ? JSON.parse(stored_sidebar_store)
  : {};

const sidebar_state = $state<ISidebarStore>(
  // sort initial data
  Object.fromEntries(
    Object.entries(parsed_stored_quiblets).map(([key, quiblets]) => [
      key,
      sort_quiblets(quiblets)
    ])
  )
);

function sync_localstorage() {
  if (browser) {
    localStorage.setItem('sidebar_store', JSON.stringify(sidebar_state));
  }
}

function sort_quiblets(quiblets: IQuiblets) {
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
    add_quiblet(quiblet: IQuiblets[number], type: string) {
      // initialize empty array for type
      if (!sidebar_state[type]) {
        sidebar_state[type] = [];
      }

      const state = sidebar_state[type];
      if (!state) return;

      const exists = state.some((q) => q.name === quiblet.name);
      if (exists) return;

      sidebar_state[type] = sort_quiblets([...state, quiblet]);
      // sidebar_state = {
      //   ...sidebar_state,
      //   [type]: sort_quiblets([...state, quiblet])
      // }
      sync_localstorage();
    },
    toggle_star(name: string, type: string) {
      if (!sidebar_state[type]) return;

      sidebar_state[type] = sort_quiblets(
        sidebar_state[type].map((q) =>
          q.name === name ? { ...q, starred: !q.starred } : q
        )
      );
    }
  };
}
