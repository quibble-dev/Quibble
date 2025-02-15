import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async () => {
  try {
    return json({ success: true });
  } catch (err) {
    console.error(err);
    return json({ success: false });
  }
};
