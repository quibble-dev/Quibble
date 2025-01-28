import innerBorder from '@quibble-dev/tailwindcss-inner-border';
import aspectRatio from '@tailwindcss/aspect-ratio';
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

  plugins: [aspectRatio, daisyui, tailwindScroll, innerBorder]
} satisfies Config;
