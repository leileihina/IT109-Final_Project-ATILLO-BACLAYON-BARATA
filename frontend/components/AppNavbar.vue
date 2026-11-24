<script setup lang="ts">
import { Button } from '@/components/ui/button'
</script>

<template>
  <header class="sticky top-0 z-50 border-b border-zinc-200 bg-white">
    <nav class="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-4 px-6 py-4">

      <!-- Website logo -->
      <NuxtLink to="/" class="text-2xl font-bold text-indigo-600">
        Skill<span class="text-zinc-900">Hub</span>
      </NuxtLink>

      <!-- Navigation links -->
      <div class="flex items-center gap-4">

        <NuxtLink
          to="/"
          class="text-sm font-medium text-zinc-600 hover:text-indigo-600"
        >
          Home
        </NuxtLink>

        <NuxtLink to="/login">
          <Button variant="outline">
            Login
          </Button>
        </NuxtLink>

        <NuxtLink to="/register">
          <Button class="bg-indigo-600 text-white hover:bg-indigo-700">
            Register
          </Button>
        </NuxtLink>

      </div>
    </nav>
  </header>
</template>