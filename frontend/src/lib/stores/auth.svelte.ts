import type { Nullable } from '$lib/types/shared';
import type { Profile, User } from '$lib/types/user';

let auth_state = $state<{
	is_authenticated: boolean;
	user: Nullable<User>;
	profile: Nullable<Profile>;
}>({
	is_authenticated: false,
	user: null,
	profile: null
});

export function get_auth_state() {
	return auth_state;
}
