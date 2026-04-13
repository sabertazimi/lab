import { defineConfig } from '@dg-scripts/eslint-config'

export default defineConfig(
  {
    ignores: ['src/assets/**/*.json'],
  },
  {
    name: 'base',
    rules: {
      'react/no-nested-component-definitions': 'off',
      'react-hooks/set-state-in-effect': 'off',
      'react-hooks-extra/no-direct-set-state-in-use-effect': 'off',
      'react-refresh/only-export-components': 'off',
      'style/multiline-ternary': ['error', 'never'],
      'ts/strict-boolean-expressions': 'off',
    },
  },
)
