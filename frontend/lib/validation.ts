import { z } from 'zod'

// Username regex
export const usernameRegex = /^[a-zA-Z0-9_]{4,20}$/

// Password regex
export const passwordRegex =
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,128}$/

// Registration validation
export const registerSchema = z.object({
  first_name: z.string()
    .trim()
    .min(1, 'First name is required.')
    .max(100),

  last_name: z.string()
    .trim()
    .min(1, 'Last name is required.')
    .max(100),

  username: z.string()
    .regex(
      usernameRegex,
      'Username must contain 4–20 letters, numbers, or underscores.'
    ),

  email: z.string()
    .email('Please enter a valid email address.'),

  password: z.string()
    .regex(
      passwordRegex,
      'Password must contain 8–128 characters, including uppercase, lowercase, number, and special character (!@#$%^&*).'
    ),

  confirm_password: z.string()
    .min(1, 'Please confirm your password.'),

  role: z.enum(['client', 'freelancer'])

}).refine(
  (data) => data.password === data.confirm_password,
  {
    message: 'Passwords do not match.',
    path: ['confirm_password']
  }
)

// Login validation
export const loginSchema = z.object({
  username: z.string()
    .regex(usernameRegex, 'Please enter a valid username.'),

  password: z.string()
    .min(1, 'Password is required.')
    .max(128, 'Password is too long.')
})