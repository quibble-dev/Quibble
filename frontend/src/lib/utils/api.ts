import { PUBLIC_API_URL } from '$env/static/public';

/**
 * A utility function to make API requests.
 *
 * @template T - The type of the response data.
 * @param endpoint - The API endpoint to call.
 * @param init_options - Optional request configuration, eg: body, method, etc.
 *
 * @returns A promise that resolves to the parsed data of type T.
 *
 * @throws { Error } Throws an error if the response if not ok.
 *
 * @example
 * ```ts
 * // Example of getting a token with type.
 * const { token } = await apiFetch<{ token: string }>('v1/user/auth/login/', {
 *   body: JSON.stringify({ email, password })
 * });
 * ```
 */
export async function apiFetch<T>(
	endpoint: string,
	{ body, ...init_options }: RequestInit = {}
): Promise<T> {
	const config: RequestInit = {
		method: body ? 'POST' : 'GET',
		...init_options,
		headers: {
			'Content-Type': 'application/json',
			...init_options?.headers
		},
		// attach body if body is provided (for POST)
		...(body && { body })
	};

	const response = await fetch(`${PUBLIC_API_URL}${endpoint}`, config);

	if (!response.ok) {
		const data = await response.json();
		throw new Error(data.errors[0].detail || 'Oops! something went wrong.');
	}

	return response.json() as Promise<T>;
}
