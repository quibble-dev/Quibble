import type { paths } from './v1';
import createClient from 'openapi-fetch';
import { PUBLIC_API_URL } from '$env/static/public';

/**
 * A Fetch API wrapper for generating types based on OpenAPI specs
 *
 * @example
 * ```ts
 * const { data, error } = await client.GET('/api/v1/endpoint/{id}', {
 *    params: { id: 69 }
 * })
 * ```
 */
const client = createClient<paths>({
	baseUrl: PUBLIC_API_URL,
	headers: {
		'Content-Type': 'application/json'
	}
});

export default client;
