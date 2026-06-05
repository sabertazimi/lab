<script setup lang="ts">
import BoardColumn from 'src/components/BoardColumn.vue'
import { useAppStore } from 'src/store'
import { computed } from 'vue'

const store = useAppStore()
const columns = computed(() => store.state.board.columns)

function createColumn(event: Event) {
  const inputElement = event.target as HTMLInputElement

  if (inputElement.value) {
    store.commit('createColumn', { name: inputElement.value })
    inputElement.value = ''
  }
}
</script>

<template>
  <div class="board-view">
    <div v-if="columns" class="columns">
      <BoardColumn
        v-for="(column, columnIndex) in columns"
        :key="column.id"
        class="column"
        :column-index="columnIndex"
        :column="column"
      />
      <div class="column">
        <input
          type="text"
          class="column-input"
          placeholder="+ Enter new column ..."
          @keyup.enter="createColumn($event)"
        >
      </div>
    </div>
    <router-view v-slot="{ Component }">
      <transition>
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<style lang="postcss" scoped>
@reference 'tailwindcss';

.board-view {
  @apply flex flex-col items-center justify-start;
  @apply h-full overflow-auto bg-green-500 p-4;
}

.columns {
  @apply flex flex-row flex-wrap items-start justify-center md:justify-start;
}

.column {
  @apply mb-4 mr-4 bg-gray-300 p-2 text-left shadow-lg;

  min-width: 350px;
}

.column-input {
  @apply block w-full border border-transparent bg-white p-2 outline-none;
  @apply focus:border-green-500;
  @apply transition duration-500;
}
</style>
