export default defineNuxtRouteMiddleware(async () => {
  const { token, fetchUser } = useAuth()

  // Redirect unauthenticated users
  if (!token.value) {
    return navigateTo('/login')
  }

  try {
    // Verify the token with FastAPI
    const currentUser = await fetchUser()

    if (!currentUser) {
      return navigateTo('/login')
    }

  } catch {
    return navigateTo('/login')
  }
})