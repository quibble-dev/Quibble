import client from '$lib/clients/client';
import type { components } from '$lib/clients/v1';
import type { Handle, HandleFetch } from '@sveltejs/kit';

type Profile = components['schemas']['Profile'];

export const handle: Handle = async ({ event, resolve }) => {
  const auth_token = event.cookies.get('auth_token');
  const auth_user_profile_id = event.cookies.get('auth_user_profile_id');
  // init local
  let profile: Profile | null = null;

  if (auth_token && auth_user_profile_id) {
    try {
      const { data } = await client.GET('/api/v1/users/me/', {
        headers: {
          Authorization: `Bearer ${auth_token}`,
          'Profile-Id': auth_user_profile_id.toString()
        }
      });

      if (data) profile = data;
    } catch (err) {
      console.error(err);
    }
  }

  event.locals.profile = profile;
  const response = await resolve(event);
  return response;
};

export const handleFetch: HandleFetch = async ({ event, request, fetch }) => {
  const auth_token = event.cookies.get('auth_token');
  console.log('AUTH_TOKEN', auth_token);

  return fetch(request);
};
