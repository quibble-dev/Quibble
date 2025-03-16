import api from '$lib/api';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
  const { data, error, response } = await api.GET('/u/profiles/{username}/', {
    params: { path: { username: params.username } }
  });

  console.log('data', data);

  console.log('response', response);

  if (response.ok && data) {
    return { profile: data };
  } else {
    console.log('error', error);
  }
};
