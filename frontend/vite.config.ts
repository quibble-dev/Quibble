import { defineConfig } from 'vitest/config';
import { sveltekit } from '@sveltejs/kit/vite';

export default defineConfig({
	plugins: [sveltekit()],
	resolve: {
    alias: {
      $lib: '/src/lib',
      
    }
  },
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
});
