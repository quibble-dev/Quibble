import api from '$lib/api';
import { RegisterSchema, VerificationCodeSchema } from '$lib/schemas/auth';
import { set_cookies_from_header } from '$lib/server/utils/cookie';
import type { PageServerLoad } from './$types';
import { fail, type Actions } from '@sveltejs/kit';
import { setError, superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async ({ url }) => {
  const initial_data = { email: url.searchParams.get('email') ?? '' };
  const form = await superValidate(initial_data, zod(RegisterSchema), { errors: false });

  return { form };
};

export const actions: Actions = {
  register: async ({ request, cookies }) => {
    const form = await superValidate(request, zod(RegisterSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    const { data, error, response } = await api.POST('/auth/registration/', {
      body: { ...form.data }
    });

    if (response.ok && data) {
      const set_cookie_header = response.headers.getSetCookie();
      set_cookies_from_header(set_cookie_header, cookies);

      return { form };
    } else if (error) {
      return setError(form, 'email', String(error.errors[0]?.detail));
    }
  },
  code: async ({ request }) => {
    const form = await superValidate(request, zod(VerificationCodeSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    const { response, error } = await api.POST('/auth/registration/verify-email/', {
      headers: { Cookie: request.headers.get('Cookie') },
      body: { key: form.data.code }
    });

    if (response.ok) {
      return { form };
    } else if (error) {
      return setError(form, 'code', String(error.errors[0]?.detail));
    }
  }
};
