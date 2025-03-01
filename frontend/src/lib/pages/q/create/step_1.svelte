<script lang="ts">
  import autosize from '$lib/actions/autosize';
  import type {
    CommunityCreateErrorsType,
    CommunityCreateFormType
  } from '$lib/schemas/community-create';

  type Props = {
    form: CommunityCreateFormType;
    errors: CommunityCreateErrorsType;
  };

  let { form, errors }: Props = $props();
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
    <span
      class="label-text-alt flex items-center gap-2"
      class:text-error={$errors.name !== undefined}
    >
      <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
      <span class="text-xs">{$errors.name?.[0] ?? 'Think of a name that grabs attention!'}</span>
    </span>
    <span class="label-text-alt">{$form.name.length}/25</span>
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
    <span
      class="label-text-alt flex items-center gap-2"
      class:text-error={$errors.name !== undefined}
    >
      <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
      <span class="text-xs"
        >{$errors.name?.[0] ?? 'Let others know what your community is for.'}</span
      >
    </span>
    <span class="label-text-alt">{$form.description.length}/255</span>
  </div>
</label>
