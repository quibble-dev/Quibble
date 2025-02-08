import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ params, cookies, url }) => {
  console.log(params, url.search, url.searchParams);
  return json({ success: true });
};
