<script lang="ts">
  import { cn } from '$lib/functions/classnames';
  import type { FormProps } from '$lib/modals/types';
  import forms from '../forms';
  import { untrack } from 'svelte';

  type Type = keyof typeof type_mapping;

  let { update_forms_state, forms_state }: FormProps<typeof forms> = $props();

  let checked_type = $state<Type>(
    (forms_state.type as { data: { type: Type } }).data.type ?? 'public'
  );

  const type_mapping = {
    public: {
      label: 'Public',
      description: 'Anyone can view, post, and comment to this community',
      icon: '<coreicons-shape-globe class="flex-shrink-0 size-4 md:size-5"></coreicons-shape-globe>'
    },
    restricted: {
      label: 'Restricted',
      description: 'Anyone can view, but only approved users can contribute',
      icon: '<coreicons-shape-shield variant="on" class="flex-shrink-0 size-4 md:size-5"></coreicons-shape-shield>'
    },
    private: {
      label: 'Private',
      description: 'Only approved users can view and contribute',
      icon: '<coreicons-shape-lock class="flex-shrink-0 size-4 md:size-5"></coreicons-shape-lock>'
    }
  };

  $effect(() => {
    const type = checked_type;
    untrack(() =>
      update_forms_state('type', {
        valid: true,
        data: { type }
      })
    );
  });
</script>

<div class="flex flex-col gap-4">
  <div class="flex flex-col gap-2">
    <h3 class="text-xl font-semibold text-info">Set your community type</h3>
    <p class="text-sm">
      Choose who can see and join your community. Public communities are visible in search, while
      private ones are invite-only.
    </p>
  </div>
  <div class="flex flex-col">
    {#each Object.entries(type_mapping) as [key, item]}
      {@const checked = checked_type === key}

      <div class={cn(checked && 'bg-base-200 ring-1', 'form-control rounded-xl p-3 ring-neutral')}>
        <label class="label cursor-pointer gap-2 p-0">
          <div class="flex items-center gap-3">
            <!-- eslint-disable svelte/no-at-html-tags -->
            {@html item.icon}
            <div class="flex flex-col">
              <span class="label-text font-medium text-info">{item.label}</span>
              <span class="text-xs text-base-content/75">{item.description}</span>
            </div>
          </div>
          <input
            type="radio"
            name="type"
            class="radio radio-sm bg-transparent checked:bg-accent"
            bind:group={checked_type}
            value={key}
          />
        </label>
      </div>
    {/each}
  </div>
</div>
