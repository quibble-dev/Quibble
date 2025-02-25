<script lang="ts">
  import StepOne from '$lib/pages/q/create/step_one.svelte';
  import StepTwo from '$lib/pages/q/create/step_two.svelte';

  const steps_mapping = {
    0: {
      title: `Give your community a name and a description that reflects its purpose and vibe.`,
      component: StepOne
    },
    1: {
      title: `Adding visual flair will catch new members attention and help establish your community's culture!`,
      component: StepTwo
    }
  };

  let step = $state<keyof typeof steps_mapping>(0);
  const current_step = $derived(steps_mapping[step]);

  const MAX_STEP = Object.keys(steps_mapping).length - 1;

  function handle_back_click() {
    if (step > 0) {
      step--;
    }
  }

  function handle_next_click() {
    if (step < MAX_STEP) {
      step++;
    }
  }
</script>

<svelte:head>
  <title>Create on Quibble</title>
</svelte:head>

<div class="flex h-max flex-1 flex-col gap-4 p-4">
  <div class="flex flex-col gap-2">
    <h1 class="text-xl font-semibold text-info">Create Community</h1>
    <p class="text-sm">{current_step.title} You can customize its look and settings later.</p>
  </div>
  <form class="flex flex-col gap-2">
    <!-- dynamic step rendering -->
    <current_step.component />
    <!-- dynamic step rendering -->
    <div class="flex items-center justify-between">
      <!-- form step indicators -->
      <div class="flex items-center gap-2">
        {#each Object.keys(steps_mapping) as _step_idx}
          {@const is_active = step === Number(_step_idx)}
          <button
            type="button"
            class="size-2 rounded-full bg-base-content"
            class:opacity-50={!is_active}
            aria-label="Go to step {_step_idx}"
            onclick={() => (step = Number(_step_idx) as keyof typeof steps_mapping)}
          ></button>
        {/each}
      </div>
      <div class="flex items-center gap-2">
        <button
          type="button"
          class="btn btn-neutral"
          disabled={step === 0}
          onclick={handle_back_click}
        >
          <coreicons-shape-arrow variant="left" class="size-4"></coreicons-shape-arrow>
          Back
        </button>
        <button type="button" class="btn btn-primary" onclick={handle_next_click}>
          Next
          <coreicons-shape-arrow variant="right" class="size-4"></coreicons-shape-arrow>
        </button>
      </div>
    </div>
  </form>
</div>
<div class="hidden w-80 lg:flex"></div>
