import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
  client: '@hey-api/client-fetch',
  input: `${process.env.PUBLIC_API_URL as string}/api/v1/schema/`,
  output: './src/lib/clients/v1/'
});
