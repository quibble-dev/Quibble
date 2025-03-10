<script lang="ts">
  import GoogleLogo from '$lib/components/icons/logos/google.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble-text.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import { cn } from '$lib/functions/classnames';
</script>

<div class="flex flex-col items-center justify-center gap-2">
  <a href="/" class="flex items-center gap-2">
    <QuibbleLogo class="size-7" />
    <QuibbleTextLogo class="h-7 w-auto" />
  </a>
  <span class="flex flex-col text-center font-medium">
    Join in, share your take, and<br /> make some waves!
  </span>
</div>
<div class="flex w-full items-center gap-3">
  <!-- oauth section: google -->
  <button class="btn flex-1">
    <GoogleLogo class="size-5" />
    Google
  </button>
  <button class="btn flex-1">
    <coreicons-logo-github class="size-5"></coreicons-logo-github>
    Github
  </button>
</div>
<div class="divider my-0 text-xs font-bold">OR</div>
<form method="POST" action="?/login" class="flex flex-col gap-3">
  <label class="floating-label">
    <span class="bg-base-300! duration-100!">Email address*</span>
    <div class="input w-full bg-transparent">
      <coreicons-shape-mail class="size-4 shrink-0"></coreicons-shape-mail>
      <input type="email" name="email" placeholder="mail@site.com" />
    </div>
  </label>
  <label class="floating-label">
    <span class="bg-base-300! duration-100!">Password*</span>
    <div class="input w-full bg-transparent pr-1.5">
      <coreicons-shape-lock class="size-4 shrink-0"></coreicons-shape-lock>
      <input type="password" name="password" placeholder="yourpassword" />
      <button
        type="button"
        tabindex="-1"
        class="btn btn-square btn-neutral btn-xs ml-auto"
        aria-label="Show/hide password"
      >
        <coreicons-shape-eye class="size-4" variant="open"></coreicons-shape-eye>
      </button>
    </div>
  </label>
  <div class="flex items-center justify-between gap-1">
    <span class="text-sm">
      New to Quibble?
      <a href="/" tabindex="-1" class="text-accent font-medium">Sign up</a>
    </span>
    <a href="/password" tabindex="-1" class="text-accent text-sm">Forgot password?</a>
  </div>
  <button class={cn(false && 'btn-active pointer-events-none', 'btn btn-primary')}>
    Log in
    <coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
  </button>
</form>
<p class="text-center text-xs">
  By continuing, you agree to the <a
    href="/support/terms-and-conditions"
    class="text-info font-medium underline">Terms of use</a
  >,
  <a href="/support/privary" class="text-info font-medium underline">Privacy</a>
  and <a href="/support/policy" class="text-info font-medium underline">Policy</a> Preplaced.
</p>
