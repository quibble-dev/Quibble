<script lang="ts">
  import GoogleLogo from '$lib/components/icons/logos/google.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble-text.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';

  let { children } = $props();
</script>

<div class="relative grid flex-1 place-items-center">
  <div
    class="absolute inset-0 bg-base-100 [mask-image:url('/assets/svgs/standalone-auth-bg.svg')] [mask-size:cover]"
  ></div>
  <div
    class="relative flex w-[25rem] flex-col gap-4 rounded-box
    bg-base-300 p-6"
  >
    <!-- header section -->
    <div class="flex flex-col items-center justify-center gap-4">
      <a href="/" class="flex items-center gap-2">
        <QuibbleLogo class="size-7" />
        <QuibbleTextLogo class="h-7 w-auto" />
      </a>
      <p class="text-center font-medium">
        Join in, share your take, and<br /> make some waves!
      </p>
    </div>
    <!-- oauth section -->
    <div class="flex w-full items-center gap-3">
      <!-- oauth section: google -->
      <button class="btn flex-1">
        <GoogleLogo class="size-5" />
        Google
      </button>
      <!-- oauth section: github -->
      <button class="btn flex-1">
        <coreicons-logo-github class="size-5"></coreicons-logo-github>
        Github
      </button>
    </div>
    <div class="divider my-0 text-xs font-bold">OR</div>
    <!-- rest pages -->
    {@render children()}
    <!-- footer section -->
    <p class="text-center text-xs">
      By continuing, you agree to the <a
        href="/support/terms-and-conditions"
        class="font-medium text-info underline">Terms of use</a
      >,
      <a href="/support/privary" class="font-medium text-info underline">Privacy</a>
      and <a href="/support/policy" class="font-medium text-info underline">Policy</a> Preplaced.
    </p>
  </div>
</div>
