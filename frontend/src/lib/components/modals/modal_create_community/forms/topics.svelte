<script lang="ts">
  import type { FormProps } from '../../types';
  import forms from '../forms';

  let {}: FormProps<typeof forms> = $props();
</script>

<div>
  <div class="flex flex-col gap-2">
    <h3 class="text-xl font-semibold text-info">Choose topics</h3>
    <p class="text-sm">
      Select up to 3 topics that represent what your community is about. This will help people with
      similar interests discover it.
    </p>
  </div>
</div>
