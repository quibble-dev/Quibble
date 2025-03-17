<script lang="ts">
  import type { CommentOverview as Props } from '$lib/types/comment';

  const { commenter, content }: Props = $props();
</script>

<p>{commenter}: {content}</p>
