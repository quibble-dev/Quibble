import type { Nullable } from './shared';

export type User = {
	id: number;
	email: string;
	date_joined: string;
};

export type Profile = {
	id: number;
	user: User;
	username: string;
	avatar: Nullable<string>;
	first_name: Nullable<string>;
	last_name: Nullable<string>;
	date_created: string;
};
