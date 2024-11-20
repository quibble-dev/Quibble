<script>
	import Card from "../icons/card.svelte";
import Compact from "../icons/compact.svelte";
import Hot from "../icons/Hot.svelte";
	import New from "../icons/new.svelte";
	import Rocket from "../icons/rocket.svelte";
	import Top from "../icons/top.svelte";

</script>
<div class="flex w-full h-7 justify-between" >
  <div class="flex gap-4">
    <a href="/" aria-label="Home" class="flex items-center gap-2">
      <Rocket/>
      <span class="text-sm font-bold">Best</span>
    </a>
    <a href="/" aria-label="Home" class="flex items-center gap-2">
      <Hot/>
      <span class="text-sm font-bold">Hot</span>
    </a>
    <a href="/" aria-label="Home" class="flex items-center gap-2">
   <New/>
      <span class="text-sm font-bold">New</span>
    </a>
    <a href="/" aria-label="Home" class="flex items-center gap-2">
   <Top/>
      <span class="text-sm font-bold">Top</span>
    </a>
  </div>
  <div class="flex gap-4">
    <a href="/" aria-label="Home" class="flex items-center gap-2">
       <Compact/>
      <span class="text-sm font-bold">Compact view</span>
    </a>
    <a href="/" aria-label="Home" class="flex items-center gap-2">
      <Card/>
      <span class="text-sm font-bold">Card view</span>
    </a>
  </div>
</div>