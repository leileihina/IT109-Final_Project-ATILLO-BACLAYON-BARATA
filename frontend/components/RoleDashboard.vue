<script setup lang="ts">
import type { UserRole, DashboardResponse } from '@/types/auth'

const props = defineProps<{
  role: UserRole
}>()

const config = useRuntimeConfig()
const { user, token, logout } = useAuth()

const dashboard = ref<DashboardResponse | null>(null)
const loading = ref(true)
const errorMessage = ref('')

const roleName = computed(() => {
  return props.role.charAt(0).toUpperCase() + props.role.slice(1)
})

async function loadDashboard() {
  loading.value = true
  errorMessage.value = ''

  try {
    dashboard.value = await $fetch<DashboardResponse>(
      `${config.public.apiBase}/api/dashboard/${props.role}`,
      {
        headers: {
          Authorization: `Bearer ${token.value}`
        }
      }
    )
  } catch (error: any) {
    if (error.statusCode === 401 || error.response?.status === 401) {
      await logout()
      return
    }

    errorMessage.value =
      error.data?.detail || 'Unable to load dashboard.'
  } finally {
    loading.value = false
  }
}

onMounted(loadDashboard)
</script>

<template>
  <div class="space-y-6">

    <!-- Welcome Section -->
    <section class="rounded-2xl bg-indigo-600 p-8 text-white">
      <p class="mb-2 text-sm text-indigo-200">
        {{ roleName }} Dashboard
      </p>

      <h1 class="text-3xl font-bold">
        Welcome, {{ user?.first_name }}!
      </h1>

      <p class="mt-2 text-indigo-100">
        Manage your activities and explore opportunities on SkillHub.
      </p>
    </section>

    <!-- Loading State -->
    <div v-if="loading" class="py-10 text-center text-zinc-500">
      Loading dashboard...
    </div>

    <!-- Error State -->
    <div
      v-else-if="errorMessage"
      class="rounded-xl border border-red-200 bg-red-50 p-4 text-red-600"
    >
      {{ errorMessage }}

      <button
        class="ml-2 font-semibold underline"
        @click="loadDashboard"
      >
        Try again
      </button>
    </div>

    <template v-else-if="dashboard">

      <!-- Account Overview -->
      <section>
        <h2 class="mb-4 text-xl font-semibold">
          Account Overview
        </h2>

        <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">

          <div class="rounded-xl border bg-white p-6 shadow-sm">
            <p class="text-sm text-zinc-500">Username</p>
            <p class="mt-2 text-xl font-semibold">
              {{ dashboard.username }}
            </p>
          </div>

          <div class="rounded-xl border bg-white p-6 shadow-sm">
            <p class="text-sm text-zinc-500">Account Role</p>
            <p class="mt-2 text-xl font-semibold capitalize">
              {{ dashboard.role }}
            </p>
          </div>

          <div class="rounded-xl border bg-white p-6 shadow-sm">
            <p class="text-sm text-zinc-500">Account Status</p>
            <p class="mt-2 text-xl font-semibold text-green-600">
              {{ user?.is_active ? 'Active' : 'Inactive' }}
            </p>
          </div>

        </div>
      </section>

      <!-- Role Permissions -->
      <section>
        <h2 class="mb-4 text-xl font-semibold">
          Your Permissions
        </h2>

        <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">

          <div
            v-for="permission in dashboard.permissions"
            :key="permission"
            class="rounded-xl border bg-white p-6 shadow-sm"
          >
            <span
              class="rounded-full bg-indigo-100 px-3 py-1 text-xs font-medium text-indigo-700"
            >
              {{ roleName }}
            </span>

            <h3 class="mt-4 font-semibold">
              {{ permission }}
            </h3>

            <p class="mt-2 text-sm text-zinc-500">
              Coming soon
            </p>
          </div>

        </div>
      </section>

      <!-- Authentication Status -->
      <section class="rounded-xl border border-green-200 bg-green-50 p-6">
        <h2 class="font-semibold text-green-700">
          Authentication Successful
        </h2>

        <p class="mt-2 text-sm text-green-600">
          {{ dashboard.message }}
          Your account has authorized access to this dashboard.
        </p>
      </section>

    </template>
  </div>
</template>