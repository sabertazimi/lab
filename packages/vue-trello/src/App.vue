<template>
  <router-view />
</template>

<style lang="postcss">
@import 'tailwindcss';

@layer components {
  .container {
    @apply mx-auto;
  }

  .link {
    @apply text-green-500 underline transition duration-500 hover:text-green-300;
  }

  .btn {
    @apply inline-flex min-w-min max-w-max cursor-pointer items-center rounded-3xl px-4 py-2;
    @apply bg-green-500 font-bold text-white;
    @apply hover:bg-green-400;
    @apply transition duration-500;
  }

  .btn-block {
    @apply btn;
    @apply h-full w-full;
    @apply rounded-none;
  }

  .btn-round {
    @apply btn;
    @apply rounded-full px-2 py-1 text-xs;
  }

  .danger {
    @apply bg-red-500 text-white hover:bg-red-400;
  }
}

.v-enter-from {
  opacity: 0;
}

@media (prefers-reduced-motion: no-preference) {
  .v-enter-active,
  .v-leave-active {
    transition: opacity 0.2s ease-out;
  }
}

.v-leave-to {
  opacity: 0;
}

html,
body {
  height: 100%;
}

#app {
  height: 100%;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
