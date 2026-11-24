<script setup lang="ts">
const { user, logout } = useAuth()

const menuItems = computed(() => {
  switch (user.value?.role) {
    case 'client':
      return [
        'Post a Project',
        'Browse Freelancers',
        'My Projects'
      ]

    case 'freelancer':
      return [
        'Browse Projects',
        'My Services',
        'My Applications'
      ]

    case 'admin':
      return [
        'Manage Users',
        'Manage Listings',
        'Transactions'
      ]

    default:
      return []
  }
})
</script>

<template>
  <aside
    class="flex min-h-screen w-64 shrink-0 flex-col border-r bg-white"
  >
    <!-- Logo -->
    <div class="border-b p-6">
      <NuxtLink
        to="/"
        class="text-2xl font-bold text-indigo-600"
      >
        SkillHub
      </NuxtLink>

      <p class="mt-1 text-xs text-zinc-500">
        Student Gig & Skill Marketplace
      </p>
    </div>

    <!-- User Information -->
    <div class="border-b p-6">
      <p class="font-semibold">
        {{ user?.first_name }} {{ user?.last_name }}
      </p>

      <span
        class="mt-2 inline-block rounded-full bg-indigo-100 px-3 py-1 text-xs font-medium capitalize text-indigo-700"
      >
        {{ user?.role }}
      </span>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 space-y-2 p-4">

      <NuxtLink
        :to="`/dashboard/${user?.role}`"
        class="block rounded-lg bg-indigo-50 px-4 py-3 font-medium text-indigo-600"
      >
        Dashboard
      </NuxtLink>

      <div
        v-for="item in menuItems"
        :key="item"
        class="flex items-center justify-between rounded-lg px-4 py-3 text-sm text-zinc-500"
      >
        <span>{{ item }}</span>

        <span class="text-xs text-zinc-400">
          Soon
        </span>
      </div>

    </nav>

    <!-- Logout -->
    <div class="border-t p-4">
      <button
        class="w-full rounded-lg bg-red-50 px-4 py-3 text-sm font-medium text-red-600 transition hover:bg-red-100"
        @click="logout"
      >
        Logout
      </button>
    </div>
  </aside>
</template>