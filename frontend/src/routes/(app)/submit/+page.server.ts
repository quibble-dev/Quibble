import client from '$lib/clients/v1/client';
import { PostSubmitSchema } from '$lib/schemas/post-submit';
import { fail, redirect, type Actions } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load = async () => {
  const form = await superValidate(zod(PostSubmitSchema));

  return { form };
};

export const actions: Actions = {
  default: async ({ request, cookies }) => {
    const form = await superValidate(request, zod(PostSubmitSchema));
    const auth_user_profile_id = cookies.get('auth_user_profile_id');

    if (!form.valid) {
      return fail(400, { form });
    }

    const { data, response } = await client.POST('/posts/', {
      headers: {
        Authorization: `Bearer ${cookies.get('auth_token')}`,
        'Profile-Id': auth_user_profile_id
      },
      body: {
        ...form.data,
        poster: Number(auth_user_profile_id)
      }
    });

    if (response.ok && data)
      redirect(307, `/q/${data.community.name}/posts/${data.id}/${data.slug}`);
    return { form };
  }
};
