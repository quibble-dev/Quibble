import type { components } from '$lib/clients/v1';

export type Comment = components['schemas']['Comment'];
export type CommentTree = Comment & { children: CommentTree[] };
