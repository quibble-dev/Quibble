import aspectRatio from '@tailwindcss/aspect-ratio';
import forms from '@tailwindcss/forms';
import typography from '@tailwindcss/typography';
import daisyui from 'daisyui';
import type { Config } from 'tailwindcss';

export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  theme: {
    extend: {
      fontFamily: {
        'riffic': 'Riffic, sans-serif',
      },
    }
  },

  daisyui: {
    themes: ['sunset']
  },

  plugins: [typography, forms, aspectRatio, daisyui]
} satisfies Config;
