<script lang="ts">
  import topics_data from '$lib/data/topics.json';
  import type { FormProps } from '../../types';
  import forms from '../forms';

  type Topics = Array<{
    category: string;
    topics: Array<string>;
  }>;

  let { forms_state }: FormProps<typeof forms> = $props();

  $effect(() => {
    console.log(forms_state);
  });
</script>

<div class="flex flex-col gap-4">
  <div class="flex flex-col gap-2">
    <h3 class="text-xl font-semibold text-info">Choose topics</h3>
    <p class="text-sm">Select up to 3 topics that represent what your community is about.</p>
  </div>
  <div class="flex max-h-80 flex-col gap-4 overflow-scroll pr-2">
    {#each topics_data as Topics as t}
      <div class="flex flex-col gap-2">
        <span class="text-sm font-medium">{t.category}</span>
        <div class="flex flex-wrap items-center gap-2">
          {#each t.topics as topic}
            <button class="btn btn-sm border-none bg-base-content/10 hover:btn-ghost"
              >{topic}</button
            >
          {/each}
        </div>
      </div>
    {/each}
  </div>
</div>
