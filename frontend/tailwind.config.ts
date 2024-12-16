import aspectRatio from '@tailwindcss/aspect-ratio';
import forms from '@tailwindcss/forms';
import typography from '@tailwindcss/typography';
import daisyui from 'daisyui';
import tailwindScroll from 'tailwind-scrollbar';

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

  plugins: [typography, forms, aspectRatio, daisyui, tailwindScroll]
} satisfies Config;
