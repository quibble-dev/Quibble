<script lang="ts">
  import EighteenPlusIcon from '$lib/components/icons/18-plus.svelte';
  import { cn } from '$lib/functions/classnames';
  import type {
    CommunityCreateErrorsType,
    CommunityCreateFormType
  } from '$lib/schemas/community-create';

  type Props = {
    form: CommunityCreateFormType;
    errors: CommunityCreateErrorsType;
  };

  const types = {
    PRIVATE: {
      label: 'Private',
      description: 'Only approved users can view and contribute',
      icon: '<coreicons-shape-lock class="flex-shrink-0 size-4 md:size-5"></coreicons-shape-lock>'
    },
    RESTRICTED: {
      label: 'Restricted',
      description: 'Anyone can view, but only approved users can contribute',
      icon: '<coreicons-shape-shield variant="on" class="flex-shrink-0 size-4 md:size-5"></coreicons-shape-shield>'
    },
    PUBLIC: {
      label: 'Public',
      description: 'Anyone can view, post, and comment to this community',
      icon: '<coreicons-shape-globe class="flex-shrink-0 size-4 md:size-5"></coreicons-shape-globe>'
    }
  };

  let { form, errors }: Props = $props();
</script>

<div class="flex flex-col">
  {#each Object.entries(types) as [key, item]}
    {@const checked = $form.type === key}

    <div class={cn(checked && 'bg-base-200 ring-1', 'form-control rounded-xl ring-neutral')}>
      <label class="label size-full cursor-pointer gap-2 p-0 p-3">
        <div class="flex items-center gap-3">
          <!-- eslint-disable svelte/no-at-html-tags -->
          <span class:text-accent={checked}>
            {@html item.icon}
          </span>
          <div class="flex flex-col">
            <span class="label-text font-medium text-info">{item.label}</span>
            <span class="text-xs text-base-content/75">{item.description}</span>
          </div>
        </div>
        <input
          type="radio"
          name="type"
          class="radio radio-sm"
          class:radio-accent={checked}
          bind:group={$form.type}
          value={key}
        />
      </label>
    </div>
  {/each}
</div>
<div class="divider my-0 h-max before:h-px after:h-px"></div>
<div class="form-control">
  <label class="label size-full cursor-pointer gap-2 p-0 p-3">
    <div class="flex items-center gap-3">
      <EighteenPlusIcon class={cn($form.nsfw && 'text-accent', 'size-5')} />
      <div class="flex flex-col">
        <span class="label-text font-medium text-info">Mature (18+)</span>
        <span class="text-xs text-base-content/75">
          Users must be over 18 to view and contribute
        </span>
      </div>
    </div>
    <input
      type="checkbox"
      class="toggle toggle-accent toggle-sm rounded-box checked:!border-accent"
      bind:checked={$form.nsfw}
    />
  </label>
</div>
{#if $errors.type || $errors.nsfw}
  <span class="label-text-alt flex items-center gap-2 text-error">
    <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
    <span class="text-xs">{$errors.type?.[0] || $errors.nsfw?.[0]}</span>
  </span>
{/if}
<span class="text-xs text-base-content/75">
  By continuing, you agree to our
  <a href="/policies/moderator-code-of-conduct" class="text-base-content underline">
    Mod Code of Conduct
  </a>
  and acknowledge that you understand the
  <a href="/policies/quibble-rules" class="text-base-content underline">Quibble Rules</a>.
</span>
