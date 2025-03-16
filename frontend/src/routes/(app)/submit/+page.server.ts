import api from '$lib/api';
import { PostSubmitSchema } from '$lib/schemas/post-submit';
import type { PageServerLoad } from '../$types';
import { fail, redirect, type Actions } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async () => {
  const form = await superValidate(zod(PostSubmitSchema));

  return { form };
};

export const actions: Actions = {
  default: async ({ request, cookies }) => {
    const form = await superValidate(request, zod(PostSubmitSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    const { data, response } = await api.POST('/posts/', {
      headers: { Cookie: request.headers.get('Cookie') },
      body: {
        ...form.data,
        poster: Number(cookies.get('profile-id'))
      }
    });

    if (response.ok && data)
      redirect(307, `/q/${data.community.name}/posts/${data.id}/${data.slug}`);
    return { form };
  }
};
