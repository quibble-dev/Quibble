import client from '$lib/clients/client';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
  const { data, error, response } = await client.GET('/api/v1/quiblets/{name}/quibs/', {
    params: {
      path: { name: params.name }
    }
  });

  if (response.ok && data) {
    return { quibs: data };
  } else if (error) {
    console.error(error);
  }
};
