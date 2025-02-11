import { browser } from '$app/environment';
import type { RecentPost, RecentPostWithTimestamp } from '../types/recent-post.type';

const stored_recent_post = browser ? localStorage.getItem('recent-post-store') : null;
const parsed_recent_post: RecentPostWithTimestamp[] = stored_recent_post
  ? // convert string to Date object
    (JSON.parse(stored_recent_post) as RecentPostWithTimestamp[]).map((q) => ({
      ...q,
      timestamp: new Date(q.timestamp)
    }))
  : [];

let recent_post = $state<RecentPostWithTimestamp[]>(parsed_recent_post);

function sync_to_localstorage() {
  if (browser) {
    // convert Date object to string
    localStorage.setItem(
      'recent-post-store',
      JSON.stringify(
        recent_post.map((q) => ({
          ...q,
          timestamp: q.timestamp.toISOString()
        }))
      )
    );
  }
}

function get_sorted_recent_post(input: RecentPostWithTimestamp) {
  return [...recent_post, input].sort((a, b) => b.timestamp.getTime() - a.timestamp.getTime());
}

export function createRecentPostStore() {
  return {
    get state() {
      return recent_post;
    },
    add_post(post: RecentPost) {
      const exists = recent_post.some((p) => p.id === post.id);
      if (exists) return;

      recent_post = get_sorted_recent_post({
        ...post,
        timestamp: new Date(Date.now())
      });

      sync_to_localstorage();
    },
    clear() {
      recent_post = [];
      sync_to_localstorage();
    }
  };
}
