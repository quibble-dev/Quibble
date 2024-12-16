<script lang="ts">
  const { children } = $props();
</script>

<div class="flex h-max flex-1 flex-col gap-4 p-4">
  {@render children()}
</div>
<div class="w-80">
  <div
    class="fixed top-[3.75rem] flex h-[calc(100dvh-3.75rem)] w-80 flex-col gap-4 overflow-y-scroll p-4 scrollbar-none"
  >
    Hey!
  </div>
</div>
