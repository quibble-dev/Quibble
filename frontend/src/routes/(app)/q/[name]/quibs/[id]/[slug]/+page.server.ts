import client from '$lib/clients/client';
import type { PageServerLoad } from './$types';
import { error as raise_error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params }) => {
  const { data, error, response } = await client.GET('/api/v1/quibs/{id}/', {
    params: {
      path: { id: params.id }
    }
  });

  if (response.ok && data) {
    if (data.slug !== params.slug) {
      redirect(307, `/q/${params.name}/quibs/${data.id}/${data.slug}/`);
    }
    return { quib: data };
  } else {
    raise_error(response.status, error?.errors[0]?.detail);
  }
};
