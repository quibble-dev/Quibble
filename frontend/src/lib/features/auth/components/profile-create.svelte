<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';

  let avatar_data_url = $state<string>(),
    cover_data_url = $state<string>();

  function handle_file_on_change(e: Event, type: 'avatar' | 'cover') {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = (e) => {
      const data_url = e.target?.result;
      if (!data_url) return;

      if (type === 'avatar') avatar_data_url = String(data_url);
      if (type === 'cover') cover_data_url = String(data_url);
    };
  }
</script>

<form class="flex flex-col gap-14">
  <div
    class="relative h-20 rounded-btn bg-base-100 bg-cover bg-center p-4"
    style="background-image: url({cover_data_url});"
  >
    <input
      type="file"
      accept="image/*"
      id="cover"
      name="cover"
      class="hidden"
      onchange={(e) => handle_file_on_change(e, 'cover')}
    />
    <label class="btn btn-circle absolute right-2.5 top-2.5 size-8 p-0" for="cover">
      <coreicons-shape-edit variant="pencil" class="size-4"></coreicons-shape-edit>
    </label>
    <div class="absolute -bottom-10 flex items-end gap-4">
      <div class="relative size-20">
        <Avatar src={avatar_data_url} class="size-full ring-8 ring-base-300" />
        <input
          type="file"
          accept="image/*"
          id="avatar"
          name="avatar"
          class="hidden"
          onchange={(e) => handle_file_on_change(e, 'avatar')}
        />
        <label class="btn btn-circle absolute -right-1.5 top-0 size-8 p-0" for="avatar">
          <coreicons-shape-edit variant="pencil" class="size-4"></coreicons-shape-edit>
        </label>
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
