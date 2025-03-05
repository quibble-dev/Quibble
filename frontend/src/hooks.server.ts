import api from '$lib/api';
import { set_cookies_from_header } from '$lib/server/utils/cookie';
import type { Nullable } from '$lib/types/shared';
import type { Handle } from '@sveltejs/kit';

const auth_routes = ['/login', '/register', '/password'];
const protected_routes = ['/submit', '/q/create'];

export const handle: Handle = async ({ event, resolve }) => {
  const auth_token = event.cookies.get('jwt-auth');
  const refresh_token = event.cookies.get('jwt-refresh');
  const has_profile_selected = Boolean(event.cookies.get('profile-id'));

  let valid_token = auth_token ? await handle_verify_access_token(auth_token) : false;

  if (!valid_token && refresh_token && has_profile_selected) {
    const res = await handle_refresh_access_token(
      refresh_token,
      event.request.headers.get('Cookie')
    );
    if (res) {
      set_cookies_from_header(res.headers.getSetCookie(), event.cookies);
      valid_token = true;
    }
  }

  if (valid_token && has_profile_selected) {
    const { data, error, response } = await api.GET('/auth/user/', {
      headers: { Cookie: event.request.headers.get('Cookie') }
    });

    if (response.ok && data) {
      event.locals.user = data;
    } else if (error) {
      console.error(error);
      event.locals.user = null;

      // on auth error
      if (response.status === 401) {
        // ...
      }
    }
  }

  // authenticated user cant access auth routes
  if (event.locals.user && auth_routes.some((route) => event.url.pathname.startsWith(route))) {
    return new Response(null, {
      status: 302,
      headers: { location: '/' }
    });
  }

  // unauthenticated user cant access protected routes
  if (
    !event.locals.user &&
    protected_routes.some((route) => event.url.pathname.startsWith(route))
  ) {
    const encoded_dest = encodeURIComponent(event.url.href);
    return new Response(null, {
      status: 302,
      headers: { location: `/login?dest=${encoded_dest}` }
    });
  }

  return await resolve(event);
};

/**
 * A utility function to check if access token if valid or not.
 * @param access_token - Access token to check.
 * @returns Promise<boolean>
 */
async function handle_verify_access_token(access_token: string) {
  const { response } = await api.POST('/auth/token/verify/', {
    body: { token: access_token }
  });

  return response.ok;
}

/**
 * A utility function to make API requests.
 * @param refresh_token - Refresh token to send along with request.
 * @param cookie_header - Cookies to send
 * @returns Promise<Nullable<Response>>
 */
async function handle_refresh_access_token(
  refresh_token: string,
  cookie_header: Nullable<string>
): Promise<Nullable<Response>> {
  const { response, error } = await api.POST('/auth/token/refresh/', {
    headers: { Cookie: cookie_header },
    // @ts-expect-error: only refresh token required
    body: { refresh: refresh_token }
  });

  if (response.ok) {
    return response;
  } else {
    console.log('refresh_access_token failed with err: ', error);
    return null;
  }
}
