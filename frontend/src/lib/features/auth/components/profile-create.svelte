<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';
</script>

<form class="flex flex-col gap-14">
  <div class="relative h-20 rounded-btn bg-base-100 p-4">
    <button
      type="button"
      class="btn btn-circle absolute right-2.5 top-2.5 size-8 p-0"
      aria-label="Select cover"
    >
      <coreicons-shape-edit variant="pencil" class="size-4"></coreicons-shape-edit>
    </button>
    <div class="absolute -bottom-10 flex items-end gap-4">
      <div class="relative grid size-20 place-items-center">
        <Avatar class="size-full" />
        <button type="button" class="btn btn-circle absolute size-8 p-0" aria-label="Select cover">
          <coreicons-shape-edit variant="pencil" class="size-4"></coreicons-shape-edit>
        </button>
      </div>
      <div class="flex flex-col">
        <label class="flex items-center text-lg">
          <span class="leading-none">u/</span>
          <input
            type="text"
            class="bg-transparent font-medium text-info outline-none placeholder:font-normal placeholder:text-base-content/50"
            placeholder="username*"
          />
        </label>
        <!-- errors goes here -->
      </div>
    </div>
  </div>
  <div class="flex items-center gap-4">
    <button type="button" class="btn flex-1" aria-label="Back">Back</button>
    <button class="btn btn-primary flex-1" aria-label="Create">Create</button>
  </div>
</form>
