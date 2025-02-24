<script lang="ts">
  import StepOne from '$lib/pages/q/create/step_one.svelte';

  const steps_mapping = {
    0: StepOne
  };

  let step = $state<keyof typeof steps_mapping>(0);
  const CurrentStep = $derived(steps_mapping[step]);
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
    <CurrentStep />
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
