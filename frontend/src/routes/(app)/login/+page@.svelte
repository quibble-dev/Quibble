<script lang="ts">
  import GoogleLogo from '$lib/components/icons/logos/google.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble-text.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import { cn } from '$lib/functions/classnames';
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
      <div class="flex items-center gap-2">
        <QuibbleLogo class="size-7" />
        <QuibbleTextLogo class="h-7 w-auto" />
      </div>
      <p class="text-center font-medium">
        Join in, share your take, and<br /> make some waves!
      </p>
    </div>

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

    <!-- form element: email and password -->
    <!-- for login and register -->
    <form method="POST" class="flex flex-col gap-3" novalidate>
      <!-- email input field with errors store -->
      <div class="flex flex-col gap-1">
        <label class="input input-bordered flex items-center gap-2 bg-transparent">
          <coreicons-shape-mail class="size-4"></coreicons-shape-mail>
          <input
            type="email"
            name="email"
            class="grow border-none p-2 text-sm font-medium focus:ring-0"
            placeholder="Email address*"
          />
        </label>
      </div>

      <!-- password input field with errors store -->
      <div class="flex flex-col gap-1">
        <label class="input input-bordered flex items-center gap-2 bg-transparent pr-2">
          <coreicons-shape-lock class="size-4"></coreicons-shape-lock>
          <input
            type="password"
            name="password"
            class="grow border-none p-2 text-sm font-medium focus:ring-0"
            placeholder="Password*"
          />

          <!-- change password field type to see -->
          <button
            type="button"
            class="btn btn-square btn-ghost btn-sm ml-auto border border-base-content/25 bg-transparent"
            aria-label="Show/hide password"
          >
            <coreicons-shape-eye class="size-4" variant="open"></coreicons-shape-eye>
          </button>
        </label>
      </div>

      <!-- render message store if any, else render help text -->
      <div class="flex items-center gap-2">
        <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
        <span class="text-xs">Hint: you can switch b/w 'login' and 'register</span>
      </div>

      <!-- submit btn with auth type changer -->
      <div class="flex items-center gap-3">
        <button
          type="submit"
          class={cn(false && 'btn-active pointer-events-none', 'btn btn-primary flex-1')}
        >
          Log in
          <coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
        </button>

        <!-- switch b/w login and register -->
        <button type="button" class="btn btn-secondary" aria-label="Switch b/w authentication type">
          <coreicons-shape-refresh class="size-4"></coreicons-shape-refresh>
        </button>
      </div>
    </form>

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
