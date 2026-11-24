<script setup lang="ts">
import { Button } from '@/components/ui/button'
import { loginSchema } from '@/lib/validation'

definePageMeta({
  layout: 'auth',
  middleware: 'guest'
})

const { login, redirectByRole } = useAuth()

// Login form data
const form = reactive({
  username: '',
  password: ''
})

// Form states
const errors = ref<Record<string, string>>({})
const errorMessage = ref('')
const loading = ref(false)
const showPassword = ref(false)

// Reusable input styling
const inputClass =
  'w-full rounded-lg border border-zinc-300 px-4 py-3 text-sm outline-none transition focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100'

// Handle login
async function handleLogin() {
  errors.value = {}
  errorMessage.value = ''

  // Validate form using Zod
  const result = loginSchema.safeParse(form)

  if (!result.success) {
    for (const issue of result.error.issues) {
      const field = String(issue.path[0])

      if (!errors.value[field]) {
        errors.value[field] = issue.message
      }
    }

    return
  }

  loading.value = true

  try {
    // Send login credentials to FastAPI
    const response = await login({
      username: result.data.username,
      password: result.data.password
    })

    // Clear password after successful login
    form.password = ''

    // Redirect based on the user's role
    await redirectByRole(response.user.role)

  } catch (error: any) {
    const detail = error.data?.detail

    errorMessage.value =
      typeof detail === 'string'
        ? detail
        : 'Unable to log in. Please try again.'

  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="w-full max-w-md rounded-2xl border border-zinc-200 bg-white p-6 shadow-sm md:p-10">

    <!-- Logo -->
    <div class="mb-6 text-center">

      <NuxtLink to="/" class="text-3xl font-bold text-indigo-600">
        Skill<span class="text-zinc-900">Hub</span>
      </NuxtLink>

    </div>

    <!-- Heading -->
    <div class="mb-8 text-center">

      <h1 class="text-3xl font-bold text-zinc-900">
        Welcome back!
      </h1>

      <p class="mt-2 text-sm text-zinc-500">
        Sign in to continue to your account.
      </p>

    </div>

    <!-- Backend error message -->
    <div
      v-if="errorMessage"
      role="alert"
      class="mb-6 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-600"
    >
      {{ errorMessage }}
    </div>

    <!-- Login form -->
    <form
      class="space-y-5"
      novalidate
      @submit.prevent="handleLogin"
    >

      <!-- Username -->
      <div>

        <label
          for="username"
          class="mb-2 block text-sm font-medium"
        >
          Username
        </label>

        <input
          id="username"
          v-model="form.username"
          :class="inputClass"
          placeholder="Enter your username"
          autocomplete="username"
        />

        <p
          v-if="errors.username"
          class="mt-1 text-xs text-red-600"
        >
          {{ errors.username }}
        </p>

      </div>

      <!-- Password -->
      <div>

        <label
          for="password"
          class="mb-2 block text-sm font-medium"
        >
          Password
        </label>

        <div class="relative">

          <input
            id="password"
            v-model="form.password"
            :type="showPassword ? 'text' : 'password'"
            :class="[inputClass, 'pr-16']"
            placeholder="Enter your password"
            autocomplete="current-password"
          />

          <button
            type="button"
            class="absolute right-3 top-3 text-sm font-medium text-indigo-600"
            @click="showPassword = !showPassword"
          >
            {{ showPassword ? 'Hide' : 'Show' }}
          </button>

        </div>

        <p
          v-if="errors.password"
          class="mt-1 text-xs text-red-600"
        >
          {{ errors.password }}
        </p>

      </div>

      <!-- Login button -->
      <Button
        type="submit"
        :disabled="loading"
        class="w-full bg-indigo-600 py-6 text-white hover:bg-indigo-700"
      >
        {{ loading ? 'Signing in...' : 'Sign In' }}
      </Button>

    </form>

    <!-- Registration link -->
    <p class="mt-6 text-center text-sm text-zinc-500">

      Don't have an account?

      <NuxtLink
        to="/register"
        class="font-semibold text-indigo-600 hover:underline"
      >
        Create an account
      </NuxtLink>

    </p>

  </div>
</template>