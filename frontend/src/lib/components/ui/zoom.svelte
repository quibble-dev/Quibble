<script lang="ts">
  import Zoom from 'svelte-medium-image-zoom';

  let { children } = $props();
</script>

<Zoom class_button_unzoom="btn" class_button_zoom="btn" zoom_margin={10}>
  {#snippet icon_zoom()}
    <coreicons-shape-expand class="size-5"></coreicons-shape-expand>
  {/snippet}
  {#snippet icon_unzoom()}
    <coreicons-shape-shrink class="size-5"></coreicons-shape-shrink>
  {/snippet}
  {@render children()}
</Zoom>
