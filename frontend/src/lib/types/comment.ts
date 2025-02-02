import type { components } from '$lib/clients/v1/schema';

export type Comment = components['schemas']['CommentDetail'];
export type CommentTree = Comment & { children: CommentTree[]; collapsed: boolean };
