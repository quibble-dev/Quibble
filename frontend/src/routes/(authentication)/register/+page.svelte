<!-- site head and seo -->
<svelte:head>
  <title>Register on Quibble</title>
</svelte:head>

<!-- form element: email and password -->
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
  <span class="text-sm">
    Already a quibbler?
    <a href="/login" class="font-medium text-accent">Log in</a>
  </span>
  <button type="button" class="btn btn-primary">
    Register
    <coreicons-shape-arrow class="size-4" variant="right"></coreicons-shape-arrow>
  </button>
</form>
