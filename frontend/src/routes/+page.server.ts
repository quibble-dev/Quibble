import client from '$lib/clients/client';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
  const { data: quibs } = await client.GET('/api/v1/quibs/');

  return { quibs };
};
