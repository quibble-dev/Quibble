import { dev } from '$app/environment';
import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';
import { apiFetch } from '$lib/utils/api';
import { isAuthError } from '$lib/errors/auth';

export const actions = {
	login: async ({ request, cookies }) => {
		const form_data = await request.formData();

		try {
			const { token } = await apiFetch<{ token: string }>('v1/user/auth/login/', {
				body: JSON.stringify({
					email: form_data.get('email'),
					password: form_data.get('password')
				})
			});

			cookies.set('auth_token', token, {
				httpOnly: true,
				secure: !dev,
				path: '/',
				sameSite: 'lax'
			});

			return { token: token };
		} catch (err) {
			let message = 'Oops! something went wrong.';
			let code = 500;

			if (isAuthError(err)) {
				message = err.message;
				code = err.code;
			} else {
				console.error(err);
			}
			return fail(code, { detail: message });
		}
	}
} satisfies Actions;
