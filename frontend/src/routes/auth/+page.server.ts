import { dev } from '$app/environment';
import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';
import { apiFetch } from '$lib/utils/api';

export const actions = {
	login: async ({ cookies, request }) => {
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

			return { success: true };
		} catch (err) {
			let message = err;
			if (err instanceof Error) message = err.message;
			return fail(401, { detail: message });
		}
	}
} satisfies Actions;
