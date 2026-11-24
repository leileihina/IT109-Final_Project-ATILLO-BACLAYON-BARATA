<script setup lang="ts">
import { Button } from '@/components/ui/button'
import { registerSchema } from '@/lib/validation'

definePageMeta({
  layout: 'auth',
  middleware: 'guest'
})

const { register } = useAuth()

// Registration form data
const form = reactive({
  first_name: '',
  last_name: '',
  username: '',
  email: '',
  password: '',
  confirm_password: '',
  role: 'client' as 'client' | 'freelancer'
})

// Form states
const errors = ref<Record<string, string>>({})
const errorMessage = ref('')
const successMessage = ref('')
const loading = ref(false)
const showPassword = ref(false)

// Reusable input styling
const inputClass =
  'w-full rounded-lg border border-zinc-300 px-4 py-3 text-sm outline-none transition focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100'

// Handle registration
async function handleRegister() {
  errors.value = {}
  errorMessage.value = ''
  successMessage.value = ''

  // Validate form using Zod
  const result = registerSchema.safeParse(form)

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
    // Send validated information to FastAPI
    await register({
      first_name: result.data.first_name,
      last_name: result.data.last_name,
      username: result.data.username,
      email: result.data.email,
      password: result.data.password,
      role: result.data.role
    })

    successMessage.value =
      'Account created successfully! You can now log in.'

  } catch (error: any) {
    const detail = error.data?.detail

    errorMessage.value =
      typeof detail === 'string'
        ? detail
        : 'Registration failed. Please check your information and try again.'

  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="w-full max-w-xl rounded-2xl border border-zinc-200 bg-white p-6 shadow-sm md:p-10">

    <!-- Heading -->
    <div class="mb-8 text-center">

      <h1 class="text-3xl font-bold text-zinc-900">
        Create an account
      </h1>

      <p class="mt-2 text-sm text-zinc-500">
        Start your journey with SkillHub.
      </p>

    </div>

    <!-- Success message -->
    <div
      v-if="successMessage"
      role="status"
      class="mb-6 rounded-lg border border-green-200 bg-green-50 p-4 text-sm text-green-700"
    >
      {{ successMessage }}

      <NuxtLink
        to="/login"
        class="mt-2 block font-semibold underline"
      >
        Proceed to Login
      </NuxtLink>
    </div>

    <!-- Error message -->
    <div
      v-if="errorMessage"
      role="alert"
      class="mb-6 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-600"
    >
      {{ errorMessage }}
    </div>

    <form
      v-if="!successMessage"
      class="space-y-5"
      novalidate
      @submit.prevent="handleRegister"
    >

      <!-- First and last name -->
      <div class="grid gap-4 sm:grid-cols-2">

        <div>
          <label for="first-name" class="mb-2 block text-sm font-medium">
            First Name
          </label>

          <input
            id="first-name"
            v-model="form.first_name"
            :class="inputClass"
            placeholder="Juan"
            autocomplete="given-name"
          />

          <p v-if="errors.first_name" class="mt-1 text-xs text-red-600">
            {{ errors.first_name }}
          </p>
        </div>

        <div>
          <label for="last-name" class="mb-2 block text-sm font-medium">
            Last Name
          </label>

          <input
            id="last-name"
            v-model="form.last_name"
            :class="inputClass"
            placeholder="Dela Cruz"
            autocomplete="family-name"
          />

          <p v-if="errors.last_name" class="mt-1 text-xs text-red-600">
            {{ errors.last_name }}
          </p>
        </div>

      </div>

      <!-- Username -->
      <div>
        <label for="username" class="mb-2 block text-sm font-medium">
          Username
        </label>

        <input
          id="username"
          v-model="form.username"
          :class="inputClass"
          placeholder="Enter your username"
          autocomplete="username"
        />

        <p v-if="errors.username" class="mt-1 text-xs text-red-600">
          {{ errors.username }}
        </p>
      </div>

      <!-- Email -->
      <div>
        <label for="email" class="mb-2 block text-sm font-medium">
          Email Address
        </label>

        <input
          id="email"
          v-model="form.email"
          type="email"
          :class="inputClass"
          placeholder="you@example.com"
          autocomplete="email"
        />

        <p v-if="errors.email" class="mt-1 text-xs text-red-600">
          {{ errors.email }}
        </p>
      </div>

      <!-- Password -->
      <div>
        <label for="password" class="mb-2 block text-sm font-medium">
          Password
        </label>

        <div class="relative">

          <input
            id="password"
            v-model="form.password"
            :type="showPassword ? 'text' : 'password'"
            :class="[inputClass, 'pr-16']"
            placeholder="Create a password"
            autocomplete="new-password"
          />

          <button
            type="button"
            class="absolute right-3 top-3 text-sm font-medium text-indigo-600"
            @click="showPassword = !showPassword"
          >
            {{ showPassword ? 'Hide' : 'Show' }}
          </button>

        </div>

        <p class="mt-2 text-xs text-zinc-500">
          At least 8 characters with uppercase, lowercase,
          number, and special character.
        </p>

        <p v-if="errors.password" class="mt-1 text-xs text-red-600">
          {{ errors.password }}
        </p>
      </div>

      <!-- Confirm password -->
      <div>
        <label for="confirm-password" class="mb-2 block text-sm font-medium">
          Confirm Password
        </label>

        <input
          id="confirm-password"
          v-model="form.confirm_password"
          :type="showPassword ? 'text' : 'password'"
          :class="inputClass"
          placeholder="Confirm your password"
          autocomplete="new-password"
        />

        <p v-if="errors.confirm_password" class="mt-1 text-xs text-red-600">
          {{ errors.confirm_password }}
        </p>
      </div>

      <!-- Role selection -->
      <fieldset>

        <legend class="mb-3 text-sm font-medium">
          Register as
        </legend>

        <div class="grid gap-3 sm:grid-cols-2">

          <!-- Client -->
          <label
            class="cursor-pointer rounded-xl border p-4 transition"
            :class="form.role === 'client'
              ? 'border-indigo-600 bg-indigo-50'
              : 'border-zinc-200 hover:border-indigo-300'"
          >
            <input
              v-model="form.role"
              type="radio"
              value="client"
              class="accent-indigo-600"
            />

            <span class="ml-2 font-semibold text-zinc-900">
              Client
            </span>

            <p class="mt-2 text-xs text-zinc-500">
              Find and hire talented freelancers.
            </p>
          </label>

          <!-- Freelancer -->
          <label
            class="cursor-pointer rounded-xl border p-4 transition"
            :class="form.role === 'freelancer'
              ? 'border-indigo-600 bg-indigo-50'
              : 'border-zinc-200 hover:border-indigo-300'"
          >
            <input
              v-model="form.role"
              type="radio"
              value="freelancer"
              class="accent-indigo-600"
            />

            <span class="ml-2 font-semibold text-zinc-900">
              Freelancer
            </span>

            <p class="mt-2 text-xs text-zinc-500">
              Offer your skills and find projects.
            </p>
          </label>

        </div>

      </fieldset>

      <!-- Register button -->
      <Button
        type="submit"
        :disabled="loading"
        class="w-full bg-indigo-600 py-6 text-white hover:bg-indigo-700"
      >
        {{ loading ? 'Creating account...' : 'Create Account' }}
      </Button>

    </form>

    <!-- Login link -->
    <p class="mt-6 text-center text-sm text-zinc-500">

      Already have an account?

      <NuxtLink
        to="/login"
        class="font-semibold text-indigo-600 hover:underline"
      >
        Sign In
      </NuxtLink>

    </p>

  </div>
</template>