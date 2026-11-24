<script setup lang="ts">
const { user } = useAuth()

const initials = computed(() => {
  if (!user.value) return ''

  return (
    user.value.first_name.charAt(0) +
    user.value.last_name.charAt(0)
  ).toUpperCase()
})
</script>

<template>
  <div class="flex min-h-screen bg-zinc-50">

    <!-- Sidebar -->
    <DashboardSidebar />

    <div class="min-w-0 flex-1">

      <!-- Dashboard Header -->
      <header
        class="sticky top-0 z-20 flex items-center justify-between border-b bg-white px-6 py-4"
      >
        <div>
          <h2 class="text-lg font-semibold capitalize">
            {{ user?.role }} Dashboard
          </h2>

          <p class="text-sm text-zinc-500">
            SkillHub Marketplace
          </p>
        </div>

        <div class="flex items-center gap-3">

          <div
            class="flex h-10 w-10 items-center justify-center rounded-full bg-indigo-100 font-semibold text-indigo-700"
          >
            {{ initials }}
          </div>

          <div class="hidden sm:block">
            <p class="text-sm font-semibold">
              {{ user?.username }}
            </p>

            <p class="text-xs capitalize text-zinc-500">
              {{ user?.role }}
            </p>
          </div>

        </div>
      </header>

      <!-- Dashboard Content -->
      <main class="p-6">
        <slot />
      </main>

    </div>
  </div>
</template>