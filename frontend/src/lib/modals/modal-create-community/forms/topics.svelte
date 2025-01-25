<script lang="ts">
  import type { FormProps } from '../../types';
  import forms from '../forms';

  let { forms_state }: FormProps<typeof forms> = $props();

  $effect(() => {
    console.log(forms_state);
  });
</script>

<div>
  <div class="flex flex-col gap-2">
    <h3 class="text-xl font-semibold text-info">Choose topics</h3>
    <p class="text-sm">Select up to 3 topics that represent what your community is about.</p>
  </div>
</div>
