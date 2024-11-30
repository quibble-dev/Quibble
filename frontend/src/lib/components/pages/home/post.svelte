<script lang="ts">
	import Avatar from '$lib/components/ui/avatar.svelte';
	import { stopPropagation } from '$lib/functions/event_modifiers';
	import readable from 'readable-numbers';

	type Props = {
		id: number;
		community: {
			avatar?: string;
			name: string;
		};
		title: string;
		slug: string;
		cover?: string;
		content: string;
		created_at: string;
		likes: number;
		dislikes: number;
		comments: number;
	};

	let props: Props = $props();
</script>

<a
	href="/q/{props.community.name}/posts/{props.slug}"
	class="flex flex-col gap-2 rounded-2xl border border-neutral bg-base-300 p-4 transition-colors hover:bg-base-200"
>
	<div class="flex items-center gap-2">
		<Avatar src={props.community.avatar} alt={props.community.name} />
		<h3 class="text-xs font-bold">q/{props.community.name}</h3>
		<coreicons-shape-circle variant="filled" class="size-0.5 text-base-content/75"
		></coreicons-shape-circle>
		<span class="text-xs font-medium text-base-content/75">{props.created_at}</span>
	</div>

	<h2 class="text-xl font-extrabold text-white">{props.title}</h2>

	<p class="line-clamp-3 text-sm font-normal text-base-content" class:hidden={props.cover}>
		{props.content}
	</p>

	<img class="rounded-xl" src={props.cover} alt="" />

	<div class="block-link mt-2 flex gap-4">
		<button onclick={stopPropagation(() => {})} class="flex items-center gap-2">
			<coreicons-shape-thumbs variant="up" class="size-4"></coreicons-shape-thumbs>
			<span class="text-sm font-semibold">{readable(props.likes)}</span>
		</button>
		<button onclick={stopPropagation(() => {})} class="flex items-center gap-2">
			<coreicons-shape-thumbs variant="down" class="size-4"></coreicons-shape-thumbs>
			<span class="text-sm font-semibold">{readable(props.dislikes)}</span>
		</button>
		<button onclick={stopPropagation(() => {})} class="flex items-center gap-2">
			<coreicons-shape-forum class="size-4"></coreicons-shape-forum>
			<span class="text-sm font-semibold">{readable(props.comments)} Quibble(s)</span>
		</button>
		<button onclick={stopPropagation(() => {})} class="flex items-center gap-2">
			<coreicons-shape-share class="size-4"></coreicons-shape-share>
			<span class="text-sm font-semibold">Share</span>
		</button>
		<button
			onclick={stopPropagation(() => {})}
			class="ml-auto flex items-center gap-2"
			aria-label="more"
		>
			<coreicons-shape-more class="size-4 rotate-90"></coreicons-shape-more>
		</button>
	</div>
</a>
