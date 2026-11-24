<script setup lang="ts">
definePageMeta({
  layout: 'dashboard',
  middleware: ['auth', 'role'],
  role: 'freelancer'
})
</script>

<template>
  <RoleDashboard role="freelancer" />
</template>