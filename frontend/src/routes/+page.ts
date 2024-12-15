import client from '$lib/clients/client';
import type { PageLoad } from './$types';

export const load: PageLoad = async () => {
  const { data: quibs } = await client.GET('/api/v1/quibs/');

  return { quibs };
};
