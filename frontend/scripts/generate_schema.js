import { createClient } from '@hey-api/openapi-ts';
import path from 'path';
import { fileURLToPath } from 'url';

const api_url = process.env.PUBLIC_API_URL;

if (!api_url) {
  console.error('error: PUBLIC_API_URL is not defined in your .env file.');
  process.exit(0);
}

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const output_path = path.resolve(__dirname, '../src/lib/clients/v1/');

createClient({
  client: '@hey-api/client-fetch',
  input: `${api_url}/api/v1/schema/`,
  output: output_path
});
