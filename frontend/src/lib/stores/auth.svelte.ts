import type { components } from '$lib/api';
import type { Nullable } from '$lib/types/shared';

type UserDetails = components['schemas']['UserDetails'];

type AuthState = {
  is_authenticated: boolean;
  user: Nullable<UserDetails>;
};

const auth_state = $state<AuthState>({
  is_authenticated: false,
  user: null
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
