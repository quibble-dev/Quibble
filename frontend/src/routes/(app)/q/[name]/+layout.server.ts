import client from '$lib/clients';
import type { LayoutServerLoad } from './$types';
import { error as raise_error, redirect } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ params }) => {
  const { data, error, response } = await client.GET('/q/communities/{name}/', {
    params: {
      path: { name: params.name }
    }
  });

  if (response.ok && data) {
    if (data.name !== params.name) {
      redirect(307, `/q/${data.name}`);
    }
    return { community: data };
  } else {
    raise_error(response.status, error?.errors[0]?.detail);
  }
};
