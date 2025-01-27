<script lang="ts">
  import topics_data from '$lib/data/topics.json';
  import { cn } from '$lib/functions/classnames';
  import type { FormProps } from '../../types';
  import forms from '../forms';

  type Topic = {
    category: string;
    topics: Array<string>;
  };

  let { forms_state }: FormProps<typeof forms> = $props();

  let topics = $state<Topic[]>(topics_data);
  let selected_topics = $state<Topic['topics']>([]);

  function handle_toggle_select_topic(topic: string) {
    // remove topic if already selected
    if (selected_topics.includes(topic)) {
      selected_topics = selected_topics.filter((t) => t !== topic);
    } else {
      if (selected_topics.length >= 3) return;
      selected_topics = [...selected_topics, topic];
    }
  }

  function handle_filter_input(e: Event) {
    const value = (e.target as HTMLInputElement).value.toLowerCase();
    // https://stackoverflow.com/a/41543705/26860113
    const emoji_regex = /([\uE000-\uF8FF]|\uD83C[\uDF00-\uDFFF]|\uD83D[\uDC00-\uDDFF])/g;

    topics = topics_data.filter(
      (t) =>
        t.category.replace(emoji_regex, '').trim().toLowerCase().startsWith(value) ||
        t.topics.some((topic) => topic.toLowerCase().startsWith(value))
    );
  }

  $effect(() => {
    console.log(forms_state);
  });
</script>

<div class="flex flex-col gap-4">
  <div class="flex flex-col gap-2">
    <h3 class="text-xl font-semibold text-info">Choose topics</h3>
    <p class="text-sm">Select up to 3 topics that represent what your community is about.</p>
  </div>
  <div class="flex flex-col gap-2">
    <label class="input input-bordered relative flex h-10 items-center px-3">
      <coreicons-shape-search class="size-5"></coreicons-shape-search>
      <input
        type="text"
        class="grow border-none text-sm font-medium focus:ring-0"
        placeholder="Filter topics..."
        oninput={handle_filter_input}
      />
    </label>
    <div class="flex items-center gap-2">
      <span class="text-sm font-medium">Topics {selected_topics.length}/3:</span>
      {#each selected_topics as topic}
        <button
          class="btn btn-ghost btn-active btn-sm"
          onclick={() => handle_toggle_select_topic(topic)}
        >
          {topic}
          <coreicons-shape-x variant="circle" class="size-4"></coreicons-shape-x>
        </button>
      {/each}
    </div>
  </div>
  <div class="flex max-h-64 flex-col gap-4 overflow-scroll pr-2">
    {#each topics as t}
      <div class="flex flex-col gap-2">
        <span class="text-sm font-medium">{t.category}</span>
        <div class="flex flex-wrap items-center gap-2">
          {#each t.topics as topic}
            {@const is_selected = selected_topics.includes(topic)}

            <button
              class={cn(
                is_selected ? 'btn-info' : 'bg-base-content/10 hover:btn-ghost',
                'btn btn-sm border-none'
              )}
              onclick={() => handle_toggle_select_topic(topic)}
            >
              {topic}
              {#if is_selected}
                <coreicons-shape-x variant="circle" class="size-4"></coreicons-shape-x>
              {/if}
            </button>
          {/each}
        </div>
      </div>
    {/each}
  </div>
</div>
