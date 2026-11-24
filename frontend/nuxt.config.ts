import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',

  devtools: {
    enabled: true
  },

  css: ['~/assets/css/main.css'],

  vite: {
    plugins: [tailwindcss()]
  },

  modules: ['shadcn-nuxt'],

  shadcn: {
    prefix: '',
    componentDir: './components/ui'
  },

  // Backend API configuration
  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:8000'
    }
  }
})