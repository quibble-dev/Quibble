<script lang="ts">
  import autosize from '$lib/actions/autosize';
</script>

<svelte:head>
  <title>Create on Quibble</title>
</svelte:head>

<div class="flex h-max flex-1 flex-col gap-4 p-4">
  <div class="flex flex-col gap-2">
    <h1 class="text-xl font-semibold text-info">Create Community</h1>
    <p class="text-sm">
      Give your community a name and description. You can customize its look and settings later.
    </p>
  </div>
  <form class="flex flex-col gap-2">
    <label class="form-control">
      <label class="input input-bordered flex items-center bg-transparent">
        q/
        <input
          type="text"
          name="name"
          class="grow border-none p-0 focus:ring-0"
          placeholder="name*"
          maxlength={25}
        />
      </label>
      <div class="label py-1">
        <!-- error store and helptext -->
        <span class="label-text-alt flex items-center gap-2">
          <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
          <span class="text-xs">Think of a name that grabs attention!</span>
        </span>
        <span class="label-text-alt">0/25</span>
      </div>
    </label>
    <label class="form-control">
      <textarea
        use:autosize
        class="textarea textarea-bordered max-h-80 min-h-40 bg-transparent leading-normal placeholder:text-base-content/75"
        placeholder="description"
        maxlength={255}
      ></textarea>
      <div class="label py-1">
        <!-- error store and helptext -->
        <span class="label-text-alt flex items-center gap-2">
          <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
          <span class="text-xs">Let others know what your community is for.</span>
        </span>
        <span class="label-text-alt">0/255</span>
      </div>
    </label>
    <div class="flex items-center justify-between">
      <div></div>
      <div class="flex items-center gap-2">
        <button type="button" class="btn btn-neutral" disabled>
          <coreicons-shape-arrow variant="left" class="size-4"></coreicons-shape-arrow>
          Back
        </button>
        <button type="button" class="btn btn-primary">
          Next
          <coreicons-shape-arrow variant="right" class="size-4"></coreicons-shape-arrow>
        </button>
      </div>
    </div>
  </form>
</div>
<div class="hidden w-80 lg:flex"></div>
