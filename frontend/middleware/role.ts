import type { UserRole } from '@/types/auth'

export default defineNuxtRouteMiddleware((to) => {
  const { user, redirectByRole } = useAuth()

  // Check if the user is authenticated
  if (!user.value) {
    return navigateTo('/login')
  }

  // Get the required role of the page
  const requiredRole = to.meta.role as UserRole | undefined

  // Prevent access to another role's dashboard
  if (requiredRole && user.value.role !== requiredRole) {
    return redirectByRole(user.value.role)
  }
})