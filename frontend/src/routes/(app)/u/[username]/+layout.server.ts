import api from '$lib/api';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ params }) => {
  const { data, error, response } = await api.GET('/u/profiles/{username}/', {
    params: { path: { username: params.username } }
  });

  if (response.ok && data) {
    return { profile: data };
  } else {
    console.log(error);
  }
};
