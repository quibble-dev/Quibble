<script lang="ts">
  import type { SVGAttributes } from 'svelte/elements';

  let { ...props }: SVGAttributes<SVGElement> = $props();
</script>

<svg {...props} viewBox="0 0 157 86" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path
    d="M143.6 13L113.366 43L143.6 73M13 13L43.2344 43L13 73"
    stroke="currentColor"
    stroke-width="25"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
</svg>
