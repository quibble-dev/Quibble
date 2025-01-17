import { PUBLIC_API_URL } from '$env/static/public';
import type { paths } from './schema';
import createClient from 'openapi-fetch';

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
  headers: {}
});

export default client;
