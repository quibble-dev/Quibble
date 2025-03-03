import client from '$lib/api';
import type { paths } from '$lib/api/v1/schema';
import type { PageServerLoad } from './$types';

type PostQuery = paths['/posts/']['get']['parameters']['query'];

export const load: PageServerLoad = async ({ url }) => {
  const sort_param = url.searchParams.get('sort');
  const query: PostQuery = { sort: sort_param ?? 'best' } as PostQuery;

  const { data: posts } = await client.GET('/posts/', {
    params: { query }
  });

  return { posts };
};
