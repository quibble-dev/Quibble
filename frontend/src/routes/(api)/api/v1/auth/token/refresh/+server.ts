import { handle_refresh_access_token } from '$lib/server/utils/auth';
import { set_cookies_from_header } from '$lib/server/utils/cookie';
import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ cookies, request }) => {
  const refresh_token = cookies.get('jwt-refresh');
  if (!refresh_token) return json({ success: false }, { status: 401 });

  try {
    const res = await handle_refresh_access_token(refresh_token, request.headers.get('Cookie'));
    if (res && res.headers.getSetCookie()) {
      set_cookies_from_header(res.headers.getSetCookie(), cookies);
    }

    return json({ success: true });
  } catch (err) {
    console.error('token refresh failed: ', err);
    return json({ success: false }, { status: 401 });
  }
};
