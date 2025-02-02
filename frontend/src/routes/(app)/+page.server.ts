import client from '$lib/clients';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
  const { data: posts_data } = await client.GET('/posts/');

  return { posts: posts_data };
};
