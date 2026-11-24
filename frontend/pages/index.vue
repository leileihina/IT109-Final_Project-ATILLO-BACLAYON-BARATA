<script setup lang="ts">
import { Button } from '@/components/ui/button'

const features = [
  {
    icon: '🎯',
    title: 'Find Opportunities',
    description: 'Discover projects that match your skills and interests.'
  },
  {
    icon: '💻',
    title: 'Showcase Your Skills',
    description: 'Offer your services and build your professional experience.'
  },
  {
    icon: '🤝',
    title: 'Connect and Collaborate',
    description: 'Work with students and faculty within your university community.'
  }
]
</script>

<template>
  <div>

    <!-- Hero section -->
    <section class="bg-linear-to-br from-indigo-50 via-white to-violet-50 px-6 py-24 md:py-32">

      <div class="mx-auto max-w-4xl text-center">

        <span class="rounded-full bg-indigo-100 px-4 py-2 text-sm font-medium text-indigo-700">
          Built for the university community
        </span>

        <h1 class="mt-8 text-4xl font-bold tracking-tight text-zinc-900 md:text-6xl">
          Turn your skills into
          <span class="text-indigo-600">
            opportunities.
          </span>
        </h1>

        <p class="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-zinc-600">
          Connect with talented students, discover freelance projects,
          and earn while learning through our Student Gig & Skill Marketplace.
        </p>

        <div class="mt-8 flex flex-wrap justify-center gap-4">

          <NuxtLink to="/register">
            <Button
              size="lg"
              class="bg-indigo-600 text-white hover:bg-indigo-700"
            >
              Get Started
            </Button>
          </NuxtLink>

          <NuxtLink to="/login">
            <Button size="lg" variant="outline">
              Sign In
            </Button>
          </NuxtLink>

        </div>

      </div>

    </section>

    <!-- Features section -->
    <section class="mx-auto max-w-7xl px-6 py-20">

      <div class="mb-12 text-center">

        <h2 class="text-3xl font-bold text-zinc-900">
          Why choose SkillHub?
        </h2>

        <p class="mt-3 text-zinc-600">
          A platform designed to help students grow and succeed.
        </p>

      </div>

      <div class="grid gap-6 md:grid-cols-3">

        <div
          v-for="feature in features"
          :key="feature.title"
          class="rounded-2xl border border-zinc-200 bg-white p-8 transition hover:border-indigo-300 hover:shadow-lg"
        >

          <div class="mb-5 flex h-14 w-14 items-center justify-center rounded-xl bg-indigo-50 text-3xl">
            {{ feature.icon }}
          </div>

          <h3 class="text-xl font-semibold text-zinc-900">
            {{ feature.title }}
          </h3>

          <p class="mt-3 leading-relaxed text-zinc-600">
            {{ feature.description }}
          </p>

        </div>

      </div>

    </section>

    <!-- Call to action section -->
    <section class="bg-indigo-600 px-6 py-16 text-center text-white">

      <h2 class="text-3xl font-bold">
        Ready to get started?
      </h2>

      <p class="mt-4 text-indigo-100">
        Join our community as a Client or Freelancer.
      </p>

      <NuxtLink to="/register">
        <Button class="mt-6 bg-white text-indigo-600 hover:bg-indigo-50">
          Create an Account
        </Button>
      </NuxtLink>

    </section>

  </div>
</template>