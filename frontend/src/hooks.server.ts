import client from '$lib/clients';
import type { Handle } from '@sveltejs/kit';

const auth_routes = ['/login', '/register', '/password'];
const protected_routes = ['/submit'];

export const handle: Handle = async ({ event, resolve }) => {
  console.log('called');
  const auth_token = event.cookies.get('auth_token');
  const auth_user_profile_id = event.cookies.get('auth_user_profile_id');

  if (auth_token && auth_user_profile_id) {
    if (!event.locals.profile) {
      const { data, error, response } = await client.GET('/u/me/', {
        headers: {
          Authorization: `Bearer ${auth_token}`,
          'Profile-Id': auth_user_profile_id
        }
      });

      if (response.ok && data) {
        event.locals.profile = data;
      } else if (error) {
        console.error(error);
        event.locals.profile = null;

        // on auth error
        if (response.status === 401) {
          event.cookies.delete('auth_token', { path: '/' });
          event.cookies.delete('auth_user_profile_id', { path: '/' });
        }
      }
    }
  }

  // authenticated user cant access auth routes
  if (event.locals.profile && auth_routes.some((route) => event.url.pathname.startsWith(route))) {
    return new Response(null, {
      status: 302,
      headers: { location: '/' }
    });
  }

  // unauthenticated user cant access protected routes
  if (
    !event.locals.profile &&
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
