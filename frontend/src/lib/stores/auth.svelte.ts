import type { Nullable } from '$lib/types/shared';
import type { Profile } from '$lib/types/user';

let auth_state = $state<{
	is_authenticated: boolean;
	profile: Nullable<Profile>;
}>({
	is_authenticated: false,
	profile: null
});

export function get_auth_state() {
	return auth_state;
}

export function set_auth_state(new_state: Partial<typeof auth_state>) {
	// auth_state = { ...auth_state, ...new_state }
	Object.assign(auth_state, new_state);
}
