import client from '$lib/clients/client';
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
    return { quib: quib.data, comments: comments.data };
  } else {
    raise_error(quib.response.status, quib.error?.errors[0]?.detail);
  }
};
