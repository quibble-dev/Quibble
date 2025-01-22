import client from '$lib/clients/v1/client';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params, parent }) => {
  await parent();

  const [posts, highlighted_posts] = await Promise.all([
    client.GET('/api/v1/communities/{name}/posts/', {
      params: {
        path: { name: params.name }
      }
    }),
    client.GET('/api/v1/communities/{name}/highlighted_posts/', {
      params: {
        path: { name: params.name }
      }
    })
  ]);

  if (posts.response.ok && posts.data && highlighted_posts.response && highlighted_posts.data) {
    return { posts: posts.data, highlighted_posts: highlighted_posts.data };
  } else {
    const errors = [posts.error, highlighted_posts.error].filter((error) => error);
    console.error(errors);
  }
};
