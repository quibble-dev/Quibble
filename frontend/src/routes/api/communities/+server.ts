import client from '$lib/clients/v1/client';
import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ cookies, request }) => {
  try {
    const { name, description } = await request.json();

    const { data, error, response } = await client.POST('/communities/', {
      headers: {
        Authorization: `Bearer ${cookies.get('auth_token')}`,
        'Profile-Id': cookies.get('auth_user_profile_id')
      },
      // @ts-expect-error: no id required for creation
      body: {
        name,
        description
      }
    });

    if (data && response.ok) {
      return json({ success: true, data });
    } else if (error) {
      console.error(error);
      return json({ success: false, error: error.errors[0]?.detail });
    }

    return json({ success: false, error: 'Unexpected response from server' });
  } catch (err) {
    console.error('unexected error: ', err);
    return json({ success: false, error: 'Internal server error' }, { status: 500 });
  }
};
