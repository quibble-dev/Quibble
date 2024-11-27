import { PUBLIC_API_URL } from '$env/static/public';

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
		...(body && { body })
	};

	const response = await fetch(`${PUBLIC_API_URL}${endpoint}`, config);

	if (!response.ok) {
		const data = await response.json();
		throw new Error(data.errors[0].detail || 'Oops! something went wrong.');
	}

	return response.json() as Promise<T>;
}
