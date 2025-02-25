<script lang="ts">
  import client from '$lib/clients/v1/client';
  import type { components } from '$lib/clients/v1/schema';
  import { cn } from '$lib/functions/classnames';

  type Topic = components['schemas']['Topic'];

  let selected_topics = $state<Topic[]>([]);

  async function fetch_topics() {
    const { data, response } = await client.GET('/q/topics/');
    if (response.ok && data) {
      return data;
    }
  }

  function handle_toggle_select_topic(topic: Topic) {
    // remove topic if already selected
    if (selected_topics.includes(topic)) {
      selected_topics = selected_topics.filter((t) => t !== topic);
    } else {
      if (selected_topics.length >= 3) return;
      selected_topics = [...selected_topics, topic];
    }
  }
</script>

<div class="flex flex-col gap-2">
  <label class="input input-bordered relative flex h-10 items-center bg-transparent pl-3 pr-1.5">
    <coreicons-shape-search class="size-5"></coreicons-shape-search>
    <input
      type="text"
      class="grow border-none px-2 text-sm font-medium placeholder:opacity-50 focus:ring-0"
      placeholder="Filter topics..."
    />
    <button type="button" class="btn btn-square btn-ghost btn-xs" aria-label="clear topic filters">
      <coreicons-shape-x class="size-4" variant="no-border"></coreicons-shape-x>
    </button>
  </label>
  <div class="flex flex-wrap items-center gap-2">
    <span class="text-sm font-medium">Topics {selected_topics.length}/3:</span>
    {#each selected_topics as topic}
      <button
        class="btn btn-ghost btn-active btn-xs md:btn-sm"
        onclick={() => handle_toggle_select_topic(topic)}
      >
        {topic}
        <coreicons-shape-x variant="circle" class="size-4"></coreicons-shape-x>
      </button>
    {/each}
  </div>
</div>
<div class="flex max-h-80 flex-col gap-2 overflow-y-scroll pr-2">
  {#await fetch_topics()}
    <div class="grid place-items-center">
      <span class="loading loading-dots loading-md"></span>
      <span class="text-sm">Fetching topics...</span>
    </div>
  {:then topics}
    {#each topics ?? [] as topic}
      <div class="flex flex-col gap-2">
        <span class="text-sm font-medium">{topic.display_name}</span>
        <div class="flex flex-wrap items-center gap-2">
          {#each topic.children as unknown as Topic[] as sub_topic}
            {@const is_selected = selected_topics.includes(sub_topic)}
            <button
              onclick={() => handle_toggle_select_topic(sub_topic)}
              class={cn(
                is_selected ? 'btn-info' : 'bg-base-content/10 hover:btn-ghost',
                'btn btn-xs border-none md:btn-sm'
              )}
            >
              <span>{sub_topic.icon} {sub_topic.display_name}</span>
              {#if is_selected}
                <coreicons-shape-x variant="circle" class="size-4"></coreicons-shape-x>
              {/if}
            </button>
          {/each}
        </div>
      </div>
    {/each}
  {/await}
</div>
