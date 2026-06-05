import path from 'node:path'
import tailwindcss from '@tailwindcss/vite'
import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'

export default defineConfig(({ mode }) => ({
  base: mode === 'production' ? '/vue-trello/' : '/',
  plugins: [tailwindcss(), vue()],
  resolve: {
    alias: {
      src: path.resolve(__dirname, './src'),
    },
  },
}))
