// See https://svelte.dev/docs/kit/types#app.d.ts
import type { components } from '$lib/api';

type Profile = components['schemas']['Profile'];

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
