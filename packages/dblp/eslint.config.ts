import { defineConfig } from '@dg-scripts/eslint-config'

export default defineConfig(
  { typescript: true },
  {
    name: 'react',
    files: ['**/*.js?(x)'],
    rules: {
      'react/prop-types': 'off',
      'react/purity': 'off',
    },
  },
)
