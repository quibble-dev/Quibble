import client from '$lib/clients/client';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
  const { data: posts_data } = await client.GET('/api/v1/posts/');

  return { posts: posts_data };
};
