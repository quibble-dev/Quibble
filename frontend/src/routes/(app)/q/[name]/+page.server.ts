import client from '$lib/clients/client';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
  const [quibs, highlighted_quibs] = await Promise.all([
    client.GET('/api/v1/quiblets/{name}/quibs/', {
      params: {
        path: { name: params.name }
      }
    }),
    client.GET('/api/v1/quiblets/{name}/highlighted_quibs/', {
      params: {
        path: { name: params.name }
      }
    })
  ]);

  if (
    quibs.response.ok &&
    quibs.data &&
    highlighted_quibs.response &&
    highlighted_quibs.data
  ) {
    return { quibs: quibs.data, highlighted_quibs: highlighted_quibs.data };
  } else {
    const errors = [quibs.error, highlighted_quibs.error].filter((error) => error);
    console.error(errors);
  }
};
