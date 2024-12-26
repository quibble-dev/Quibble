import client from '$lib/clients/client';
import { CommentTreeBuilder } from '$lib/functions/comment';
import type { PageServerLoad } from './$types';
import { error as raise_error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params }) => {
  const [quib, comments] = await Promise.all([
    await client.GET('/api/v1/quibs/{id}/', {
      params: {
        path: { id: params.id }
      }
    }),
    await client.GET('/api/v1/quibs/{id}/comments/', {
      params: {
        path: { id: params.id }
      }
    })
  ]);

  if (quib.response.ok && quib.data) {
    if (quib.data.slug !== params.slug) {
      redirect(307, `/q/${params.name}/quibs/${quib.data.id}/${quib.data.slug}/`);
    }

    // build comment free before sending to frontend
    const comment_tree_builder = new CommentTreeBuilder(comments.data);
    const comment_tree = comment_tree_builder.build();

    return { quib: quib.data, comments: comment_tree };
  } else {
    raise_error(quib.response.status, quib.error?.errors[0]?.detail);
  }
};
