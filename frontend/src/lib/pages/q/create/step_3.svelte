<script lang="ts">
  import client from '$lib/clients/v1/client';
  import type { components } from '$lib/clients/v1/schema';
  import { cn } from '$lib/functions/classnames';
  import type { CommunityCreateFormType } from '$lib/schemas/community-create';
  import { onMount } from 'svelte';

  // internal types
  type Topic = components['schemas']['Topic'];

  // constants
  const SELECTED_TOPIC_LIMIT = 3;

  let { form }: { form: CommunityCreateFormType } = $props();

  let pending = $state(false);
  let filter_input_value = $state('');

  let selected_topics = $state<Topic[]>([]);
  let topics_raw = $state<Topic[]>([]);

  let topics = $derived.by<Topic[]>(() => {
    const value = filter_input_value.toLowerCase();
    // https://stackoverflow.com/a/41543705/26860113
    const emoji_regex = /([\uE000-\uF8FF]|\uD83C[\uDF00-\uDFFF]|\uD83D[\uDC00-\uDDFF])/g;

    function normalize_str(str: string) {
      return str.replace(emoji_regex, '').trim().toLowerCase();
    }

    function filter_str(str: string) {
      return normalize_str(str)
        .split(' ')
        .some((s) => s.startsWith(value));
    }

    return topics_raw.filter(
      (topic) =>
        filter_str(topic.display_name) ||
        (topic.children as unknown as Topic[]).some((t) => filter_str(t.display_name))
    );
  });

  async function fetch_topics() {
    try {
      pending = true;

      const { data, response } = await client.GET('/q/topics/');
      if (response.ok && data) {
        topics_raw = data;
      }
    } finally {
      pending = false;
    }
  }

  function check_is_selected(id: number): boolean {
    return selected_topics.some((t) => t.id === id);
  }

  function handle_toggle_select_topic(topic: Topic) {
    // remove topic if already selected
    if (check_is_selected(topic.id)) {
      selected_topics = selected_topics.filter((t) => t.id !== topic.id);
      // remove from state
      const topic_idx = $form.topics.indexOf(topic.id);
      if (topic_idx !== -1) $form.topics.splice(topic_idx, 1);
    } else {
      if (selected_topics.length >= SELECTED_TOPIC_LIMIT) return;
      selected_topics = [...selected_topics, topic].sort((a, b) => a.id - b.id);
      // update form state
      $form.topics.push(topic.id);
    }
  }

  onMount(async () => {
    await fetch_topics();
    // update selected_topics state
    if ($form.topics.length) {
      const flattened_topics = topics_raw.flatMap((t) => [
        t,
        ...(t.children as unknown as Topic[])
      ]);
      selected_topics = flattened_topics.filter((t) => $form.topics.includes(t.id));
    }
  });
</script>

<div class="flex flex-col gap-2">
  <label class="input input-bordered relative flex h-10 items-center bg-transparent pl-3 pr-1.5">
    <coreicons-shape-search class="size-5"></coreicons-shape-search>
    <input
      type="text"
      class="grow border-none px-2 text-sm font-medium placeholder:text-base-content/75 focus:ring-0"
      placeholder="Filter topics..."
      bind:value={filter_input_value}
    />
    <button
      type="button"
      class="btn btn-square btn-ghost btn-xs"
      aria-label="clear topic filters"
      disabled={!filter_input_value}
      onclick={() => (filter_input_value = '')}
    >
      <coreicons-shape-x class="size-4" variant="no-border"></coreicons-shape-x>
    </button>
  </label>
  <div class="flex flex-wrap items-center gap-2">
    <span class="text-sm font-medium">Topics {selected_topics.length}/3:</span>
    {#each selected_topics as topic}
      <button
        type="button"
        class="btn btn-xs md:btn-sm"
        onclick={() => handle_toggle_select_topic(topic)}
      >
        {topic.display_name}
        <coreicons-shape-x variant="circle" class="size-4"></coreicons-shape-x>
      </button>
    {/each}
  </div>
</div>
<div class="mt-2 flex max-h-80 flex-col gap-2 overflow-y-scroll pr-2">
  {#if pending}
    <div class="grid place-items-center">
      <span class="loading loading-dots loading-md"></span>
      <span class="text-sm">Fetching topics...</span>
    </div>
  {:else}
    {#each topics as topic (topic.id)}
      <div class="flex flex-col gap-1">
        <span class="text-sm font-medium">{topic.icon} {topic.display_name}</span>
        <div class="flex flex-wrap items-center gap-2">
          {#each topic.children as unknown as Topic[] as t (t.id)}
            {@const is_selected = check_is_selected(t.id)}

            <button
              type="button"
              onclick={() => handle_toggle_select_topic(t)}
              class={cn(
                is_selected ? 'btn-ghost btn-active' : 'btn-neutral',
                'btn btn-xs border-none md:btn-sm'
              )}
            >
              <span>{t.display_name}</span>
              {#if is_selected}
                <coreicons-shape-x variant="circle" class="size-4"></coreicons-shape-x>
              {/if}
            </button>
          {/each}
        </div>
      </div>
    {/each}
  {/if}
</div>
