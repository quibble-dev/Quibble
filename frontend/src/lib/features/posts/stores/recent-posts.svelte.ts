import { browser } from '$app/environment';
import type { Post, RecentPost } from '../types/recent-post.type';

const stored_recent_posts = browser ? localStorage.getItem('recent_posts') : null;
const parsed_recent_posts: RecentPost[] = stored_recent_posts
  ? // convert string to Date object
    (JSON.parse(stored_recent_posts) as RecentPost[]).map((q) => ({
      ...q,
      timestamp: new Date(q.timestamp)
    }))
  : [];

let recent_posts = $state<RecentPost[]>(parsed_recent_posts);

function sync_to_localstorage() {
  if (browser) {
    // convert Date object to string
    localStorage.setItem(
      'recent_posts',
      JSON.stringify(
        recent_posts.map((q) => ({
          ...q,
          timestamp: q.timestamp.toISOString()
        }))
      )
    );
  }
}

function get_sorted_recent_posts(input: RecentPost) {
  return [...recent_posts, input].sort((a, b) => b.timestamp.getTime() - a.timestamp.getTime());
}

export function createRecentPostsStore() {
  return {
    get state() {
      return recent_posts;
    },
    add_post(post: Post) {
      const exists = recent_posts.some((p) => p.id === post.id);
      if (exists) return;

      recent_posts = get_sorted_recent_posts({
        ...post,
        timestamp: new Date(Date.now())
      });

      sync_to_localstorage();
    }
  };
}
