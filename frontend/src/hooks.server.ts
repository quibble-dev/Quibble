import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	console.log(event.cookies.get('auth_token'));

	const response = await resolve(event);
	return response;
};
