import type { paths } from '$lib/types/schema_v1';
import createClient from 'openapi-fetch';
import { PUBLIC_API_URL } from '$env/static/public';

export const client = createClient<paths>({
	baseUrl: PUBLIC_API_URL
});
