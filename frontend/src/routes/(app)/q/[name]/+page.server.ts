import client from '$lib/clients/client';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
  const {
    data: quibs_data,
    error: quibs_error,
    response: quibs_response
  } = await client.GET('/api/v1/quiblets/{name}/quibs/', {
    params: {
      path: { name: params.name }
    }
  });

  const {
    data: highlighted_quibs_data,
    error: highlighted_quibs_error,
    response: highlighted_quibs_response
  } = await client.GET('/api/v1/quiblets/{name}/highlighted_quibs/', {
    params: {
      path: { name: params.name }
    }
  });

  if (
    quibs_response.ok &&
    quibs_data &&
    highlighted_quibs_response &&
    highlighted_quibs_data
  ) {
    return { quibs: quibs_data, highlighted_quibs: highlighted_quibs_data };
  } else if (quibs_error || highlighted_quibs_error) {
    console.error(quibs_error, highlighted_quibs_error);
  }
};
