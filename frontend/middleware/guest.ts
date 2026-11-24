export default defineNuxtRouteMiddleware(async () => {
  const { token, fetchUser, redirectByRole } = useAuth()

  if (!token.value) {
    return
  }

  try {
    const currentUser = await fetchUser()

    if (currentUser) {
      return redirectByRole(currentUser.role)
    }
  } catch {
    // Allow login or registration if the token is invalid
  }
})