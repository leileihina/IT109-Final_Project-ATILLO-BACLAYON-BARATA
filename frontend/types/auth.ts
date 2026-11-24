// Available user roles
export type UserRole = 'client' | 'freelancer' | 'admin'

// User information returned by the backend
export interface User {
  id: number
  first_name: string
  last_name: string
  username: string
  email: string
  role: UserRole
  is_active: boolean
  created_at: string
}

// Registration request
export interface RegisterRequest {
  first_name: string
  last_name: string
  username: string
  email: string
  password: string
  role: 'client' | 'freelancer'
}

// Login request
export interface LoginRequest {
  username: string
  password: string
}

// Login response from FastAPI
export interface LoginResponse {
  access_token: string
  token_type: string
  user: User
}

// Dashboard response
export interface DashboardResponse {
  message: string
  username: string
  role: UserRole
  permissions: string[]
}