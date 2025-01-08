import { browser } from '$app/environment';

type RecentQuibs = {
  id: string;
  quiblet: {
    avatar?: string | null | undefined;
    name: string;
  };
  title: string;
  slug?: string | undefined;
  cover?: string | null | undefined;
  upvotes?: number[] | undefined;
  comments?: number[] | undefined;
}[];

const stored_recent_quibs = browser ? localStorage.getItem('recent_posts_store') : null;
const parsed_stored_recent_quibs: RecentQuibs = stored_recent_quibs
  ? JSON.parse(stored_recent_quibs)
  : [];

let recent_quibs_state = $state<RecentQuibs>(parsed_stored_recent_quibs);

function sync_to_localstorage() {
  if (browser) {
    localStorage.setItem('recent_posts_store', JSON.stringify(recent_quibs_state));
  }
}

export function createRecentQuibsStore() {
  return {
    get state() {
      return recent_quibs_state;
    },
    add_quib(quib: RecentQuibs[number]) {
      const exists = recent_quibs_state.some((q) => q.id === quib.id);
      if (exists) return;

      recent_quibs_state.push(quib);
      sync_to_localstorage();
    }
  };
}
