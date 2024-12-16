import client from '$lib/clients/client';
import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
  const {
    data: quiblet,
    error,
    response
  } = await client.GET('/api/v1/quiblets/{name}/', {
    params: {
      path: { name: params.name }
    }
  });

  if (response.ok && quiblet) {
    if (quiblet.name !== params.name) {
      redirect(307, `/q/${quiblet.name}`);
    }
    return { quiblet };
  } else if (error) {
    redirect(309, '/');
  }
};
