<script setup lang="ts">
definePageMeta({
  layout: 'dashboard',
  middleware: ['auth', 'role'],
  role: 'admin'
})
</script>

<template>
  <RoleDashboard role="admin" />
</template>