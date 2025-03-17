import type { components } from '$lib/api';
import type { Nullable } from './shared';

export type Comment = components['schemas']['Comment'];
export type CommentTree = Comment & { children: CommentTree[]; collapsed: boolean };

export type CommentOverview = {
  id: number;
  commenter: string;
  reply_to: Nullable<string>;
  ratio: number;
  post: {
    title: string;
    slug: string;
    community: {
      name: string;
      avatar: Nullable<string>;
    };
  };
  created_at: string;
  content: string;
  deleted: boolean;
};
