import path from 'node:path'
import { defineConfig } from 'vite'

export default defineConfig(({ mode }) => ({
  base: mode === 'production' ? '/vue-design/' : '/',
  resolve: {
    alias: {
      src: path.resolve(__dirname, './src'),
    },
  },
}))
