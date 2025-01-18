import type { components } from '$lib/clients/v1/schema';
import type { Nullable } from '$lib/types/shared';

type Profile = components['schemas']['Profile'];

type AuthState = {
  is_authenticated: boolean;
  profile: Nullable<Profile>;
};

const auth_state = $state<AuthState>({
  is_authenticated: false,
  profile: null
});

export function createAuthStore() {
  return {
    get state() {
      return auth_state;
    },
    update(new_state: Partial<AuthState>) {
      // spreading doesnt work because it creates a new reference
      // which leads to infinite loop of effects
      // auth_state = { ...auth_state, ...new_state }
      Object.assign(auth_state, new_state);
    }
  };
}
