import { PUBLIC_API_URL } from '$env/static/public';
import type { paths } from './v1';
import createClient from 'openapi-fetch';

/**
 * V1 Fetch API wrapper for generating types based on OpenAPI specs
 *
 * @example
 * ```ts
 * const { data, error } = await client.GET('/endpoint/{id}', {
 *    params: { id: 69 }
 * })
 * ```
 */
const client = createClient<paths>({
  baseUrl: PUBLIC_API_URL,
  credentials: 'include'
});

export default client;
export * from './v1';
