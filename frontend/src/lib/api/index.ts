import { PUBLIC_API_URL } from '$env/static/public';
import type { paths } from './v1';
import createClient from 'openapi-fetch';

const client = createClient<paths>({
  baseUrl: PUBLIC_API_URL,
  credentials: 'include'
});

export default client;
export * from './v1';
