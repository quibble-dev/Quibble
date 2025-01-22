<script lang="ts">
  import Avatar from '$lib/components/ui/avatar.svelte';
  import type { FormProps } from '../../types';
  import forms from '../forms';

  let {}: FormProps<typeof forms> = $props();

  let community_name = $state('');
  let community_description = $state('');
</script>

<div class="flex flex-col gap-4">
  <div class="flex flex-col gap-2">
    <h3 class="text-xl font-semibold text-info">Introduce your community</h3>
    <p class="text-sm">
      Give your community a name and a description that reflects its purpose and vibe. This will
      help others discover and connect with it.
    </p>
  </div>
  <form class="flex grid grid-cols-2">
    <div class="flex-1">
      <label class="form-control">
        <div class="label pt-0">
          <span class="label-text font-medium">Community name*</span>
        </div>
        <label class="input input-bordered flex items-center gap-2 text-sm font-medium">
          q/
          <input
            bind:value={community_name}
            type="text"
            class="grow border-none p-0 text-sm focus:ring-0"
            placeholder="eg: quibble"
          />
        </label>
        <div class="label">
          <span class="label-text-alt flex items-center gap-1.5">
            <coreicons-shape-info class="size-4"></coreicons-shape-info>
            Name it unique and cool!
          </span>
          <span class="label-text-alt">0/21</span>
        </div>
      </label>
      <label class="form-control">
        <div class="label pt-0">
          <span class="label-text font-medium">Description*</span>
        </div>
        <textarea
          bind:value={community_description}
          class="textarea textarea-bordered h-40 leading-normal"
          placeholder="Tell something nice about your community..."
        ></textarea>
        <div class="label">
          <span class="label-text-alt flex items-center gap-1.5">
            <coreicons-shape-info class="size-4"></coreicons-shape-info>
            A quick cool introduction!
          </span>
          <span class="label-text-alt">0/21</span>
        </div>
      </label>
    </div>
    <div class="flex-1 p-7">
      <div class="overflow-hidden rounded-2xl bg-neutral shadow-xl">
        <div class="h-10 bg-base-content"></div>
        <div class="flex flex-col gap-4 p-4">
          <div class="flex items-center gap-4">
            <Avatar class="size-14 !bg-base-content/25" />
            <div class="flex flex-col">
              <span class="text-lg font-semibold text-info"
                >q/{community_name || 'communityname'}</span
              >
              <div class="flex items-center gap-2">
                <span class="text-xs">1 member</span>
                <coreicons-shape-circle class="size-0.5" variant="filled"></coreicons-shape-circle>
                <span class="text-xs">1 online</span>
              </div>
            </div>
          </div>
          <p class="whitespace-pre-line text-sm">
            {community_description || 'Community description'}
          </p>
        </div>
      </div>
    </div>
  </form>
</div>
