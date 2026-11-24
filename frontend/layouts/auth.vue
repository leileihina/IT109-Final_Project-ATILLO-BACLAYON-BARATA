<template>
  <div class="flex min-h-screen flex-col bg-zinc-50">

    <AppNavbar />

    <main class="flex flex-1 items-center justify-center px-4 py-12">
      <slot />
    </main>

    <AppFooter />

  </div>
</template>