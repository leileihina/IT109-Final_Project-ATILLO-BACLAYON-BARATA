<script setup lang="ts">
definePageMeta({
  layout: 'dashboard',
  middleware: ['auth', 'role'],
  role: 'client'
})
</script>

<template>
  <RoleDashboard role="client" />
</template>