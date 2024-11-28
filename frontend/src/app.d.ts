// See https://svelte.dev/docs/kit/types#app.d.ts

import type { Profile } from '$lib/types/user';

// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		interface Locals {
			profile: Profile | null;
		}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

export {};
