import type {
  User,
  UserRole,
  RegisterRequest,
  LoginRequest,
  LoginResponse
} from '@/types/auth'

export const useAuth = () => {
  const config = useRuntimeConfig()

  const apiBase = config.public.apiBase

  // Shared authentication state
  const user = useState<User | null>('auth-user', () => null)

  const token = useState<string | null>('auth-token', () => null)

  // Check if the user is authenticated
  const isAuthenticated = computed(() => {
    return !!token.value && !!user.value
  })

  // Register a new user
  async function register(data: RegisterRequest) {
    return await $fetch<User>(`${apiBase}/api/auth/register`, {
      method: 'POST',
      body: data
    })
  }

  // Log in an existing user
  async function login(data: LoginRequest) {
    const response = await $fetch<LoginResponse>(
      `${apiBase}/api/auth/login`,
      {
        method: 'POST',
        body: data
      }
    )

    token.value = response.access_token
    user.value = response.user

    return response
  }

  // Retrieve the authenticated user's information
  async function fetchUser() {
    if (!token.value) {
      return null
    }

    try {
      const response = await $fetch<User>(
        `${apiBase}/api/auth/me`,
        {
          headers: {
            Authorization: `Bearer ${token.value}`
          }
        }
      )

      user.value = response

      return response

    } catch (error) {
      token.value = null
      user.value = null

      throw error
    }
  }

  // Redirect users based on their roles
  async function redirectByRole(role: UserRole) {
    switch (role) {
      case 'client':
        return navigateTo('/dashboard/client')

      case 'freelancer':
        return navigateTo('/dashboard/freelancer')

      case 'admin':
        return navigateTo('/dashboard/admin')
    }
  }

  // Log out the current user
  async function logout() {
    token.value = null
    user.value = null

    return navigateTo('/login')
  }

  return {
    user,
    token,
    isAuthenticated,
    register,
    login,
    fetchUser,
    redirectByRole,
    logout
  }
}