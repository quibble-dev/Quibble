import type { SidebarCommunity } from '$lib/types/sidebar';

export const sidebar_communities: {
	[key: string]: SidebarCommunity[];
} = {
	favorites: [
		{
			name: 'AskQuibble',
			avatar: 'https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp',
			starred: true
		},
		{
			name: 'sveltejs',
			starred: false
		}
	],
	your_communities: [
		{
			name: 'developers',
			avatar: 'https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp',
			starred: true
		},
		{
			name: 'anime',
			starred: false
		}
	]
};
