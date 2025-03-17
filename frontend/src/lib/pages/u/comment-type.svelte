<script lang="ts">
  import type { components } from '$lib/api';

  type Props = components['schemas']['Comment'];

  const { content }: Props = $props();
</script>

<p>{content}</p>
