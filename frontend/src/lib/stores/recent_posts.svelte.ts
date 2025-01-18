import { browser } from '$app/environment';

type Post = {
  id: string;
  community: {
    avatar?: string | null | undefined;
    name: string;
  };
  title: string;
  slug?: string | undefined;
  cover?: string | null | undefined;
  upvotes?: number[] | undefined;
  comments?: number[] | undefined;
};

interface IRecentPost extends Post {
  timestamp: Date;
}

const stored_recent_posts = browser ? localStorage.getItem('recent_posts_store') : null;
const parsed_stored_recent_posts: IRecentPost[] = stored_recent_posts
  ? // convert string to Date object
    (JSON.parse(stored_recent_posts) as IRecentPost[]).map((q) => ({
      ...q,
      timestamp: new Date(q.timestamp)
    }))
  : [];

let recent_posts_state = $state<IRecentPost[]>(parsed_stored_recent_posts);

function sync_to_localstorage() {
  if (browser) {
    // convert Date object to string
    localStorage.setItem(
      'recent_posts_store',
      JSON.stringify(
        recent_posts_state.map((q) => ({
          ...q,
          timestamp: q.timestamp.toISOString()
        }))
      )
    );
  }
}

function get_sorted_recent_posts_state(input: IRecentPost) {
  return [...recent_posts_state, input].sort(
    (a, b) => b.timestamp.getTime() - a.timestamp.getTime()
  );
}

export function createRecentPostsStore() {
  return {
    get state() {
      return recent_posts_state;
    },
    add_post(post: Post) {
      const exists = recent_posts_state.some((q) => q.id === post.id);
      if (exists) return;

      recent_posts_state = get_sorted_recent_posts_state({
        ...post,
        timestamp: new Date(Date.now())
      });

      sync_to_localstorage();
    }
  };
}
