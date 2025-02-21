import inner_border from '@quibble-dev/tailwindcss-inner-border';
import daisyui from 'daisyui';
import tailwind_scrollbar from 'tailwind-scrollbar';
import type { Config } from 'tailwindcss';

export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  theme: {
    extend: {
      fontFamily: {
        sans: 'Roboto, sans-serif'
      }
    }
  },

  daisyui: {
    themes: ['sunset'],
    logs: false
  },

  plugins: [daisyui, tailwind_scrollbar, inner_border]
} satisfies Config;
