import client from '$lib/clients';
import { CommentTreeBuilder } from '$lib/functions/comment';
import type { PageServerLoad } from './$types';
import { error as raise_error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params }) => {
  const [post, comments] = await Promise.all([
    await client.GET('/api/v1/posts/{id}/', {
      params: {
        path: { id: params.id }
      }
    }),
    await client.GET('/api/v1/posts/{id}/comments/', {
      params: {
        path: { id: params.id }
      }
    })
  ]);

  if (post.response.ok && post.data) {
    if (post.data.slug !== params.slug) {
      redirect(307, `/q/${params.name}/posts/${post.data.id}/${post.data.slug}/`);
    }

    // build comment free before sending to frontend
    const comment_tree_builder = new CommentTreeBuilder(comments.data);
    const comment_tree = comment_tree_builder.build();

    return { post: post.data, comments: comment_tree };
  } else {
    raise_error(post.response.status, post.error?.errors[0]?.detail);
  }
};
