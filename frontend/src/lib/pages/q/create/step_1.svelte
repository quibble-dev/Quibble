<script lang="ts">
  import autosize from '$lib/actions/autosize';
  import type { CommunityCreateFormType } from '$lib/schemas/community-create';

  let { form }: { form: CommunityCreateFormType } = $props();
</script>

<label class="form-control">
  <label class="input input-bordered flex items-center bg-transparent">
    q/
    <input
      type="text"
      name="name"
      class="grow border-none p-0 focus:ring-0"
      placeholder="name*"
      maxlength={25}
      bind:value={$form.name}
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
    class="textarea textarea-bordered max-h-80 min-h-40 bg-transparent leading-normal placeholder:text-base-content/75"
    placeholder="description*"
    use:autosize
    bind:value={$form.description}
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
