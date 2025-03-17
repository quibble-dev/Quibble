<script lang="ts">
  import type { components } from '$lib/api';

  type Props = components['schemas']['Post'];

  const { title }: Props = $props();
</script>

<p>{title}</p>
