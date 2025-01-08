import { browser } from '$app/environment';

type Quib = {
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
};

interface IRecentQuib extends Quib {
  timestamp: Date;
}

const stored_recent_quibs = browser ? localStorage.getItem('recent_posts_store') : null;
const parsed_stored_recent_quibs: IRecentQuib[] = stored_recent_quibs
  ? // convert string to Date object
    (JSON.parse(stored_recent_quibs) as IRecentQuib[]).map((q) => ({
      ...q,
      timestamp: new Date(q.timestamp)
    }))
  : [];

let recent_quibs_state = $state<IRecentQuib[]>(parsed_stored_recent_quibs);

function sync_to_localstorage() {
  if (browser) {
    // convert Date object to string
    localStorage.setItem(
      'recent_posts_store',
      JSON.stringify(
        recent_quibs_state.map((q) => ({
          ...q,
          timestamp: q.timestamp.toISOString()
        }))
      )
    );
  }
}

function get_sorted_recent_quibs_state(input: IRecentQuib) {
  return [...recent_quibs_state, input].sort(
    (a, b) => b.timestamp.getTime() - a.timestamp.getTime()
  );
}

export function createRecentQuibsStore() {
  return {
    get state() {
      return recent_quibs_state;
    },
    add_quib(quib: Quib) {
      const exists = recent_quibs_state.some((q) => q.id === quib.id);
      if (exists) return;

      recent_quibs_state = get_sorted_recent_quibs_state({
        ...quib,
        timestamp: new Date(Date.now())
      });

      sync_to_localstorage();
    }
  };
}
