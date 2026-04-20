import { defineConfig } from '@dg-scripts/eslint-config'

export default defineConfig(
  {
    ignores: ['src/assets/**/*.json'],
  },
  {
    name: 'base',
    rules: {
      'react/component-hook-factories': 'off',
      'react/no-nested-component-definitions': 'off',
      'react/set-state-in-effect': 'off',
      'react-refresh/only-export-components': 'off',
      'style/multiline-ternary': ['error', 'never'],
      'ts/strict-boolean-expressions': 'off',
    },
  },
)
