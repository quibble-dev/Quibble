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
				sans: 'DM Sans, sans-serif'
			}
		}
	},

	daisyui: {
		themes: ['sunset']
	},

	plugins: [typography, forms, aspectRatio, daisyui, tailwindScroll]
} satisfies Config;
