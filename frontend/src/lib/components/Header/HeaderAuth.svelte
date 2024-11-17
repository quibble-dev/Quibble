<script>

	import Notification from "../Icons/Notification.svelte";
	import Plus from "../Icons/Plus.svelte";

</script>
<button class="btn btn-md btn-primary font-bold"><Plus /> <span>Create New</span></button>
<Notification />
<div draggable="false" class="avatar cursor-pointer select-none">
  <div class="w-[50px] rounded-[15px]">
    <img
      draggable="false"
      alt="avatar"
      src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
    />
  </div>
</div>