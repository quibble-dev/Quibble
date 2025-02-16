import client from '$lib/clients';
import type { Handle, HandleFetch } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
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

        event.cookies.delete('auth_token', { path: '/' });
        event.cookies.delete('auth_user_profile_id', { path: '/' });
      }
    }
  }

  if (event.locals.profile && ['/login', '/register', '/password'].includes(event.url.pathname)) {
    return new Response(null, {
      status: 302,
      headers: { location: '/' }
    });
  }

  return await resolve(event);
};

export const handleFetch: HandleFetch = async ({ event, request, fetch }) => {
  const auth_token = event.cookies.get('auth_token');
  console.log('AUTH_TOKEN', auth_token);

  return fetch(request);
};
