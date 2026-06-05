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
  <div class="flex flex-col items-center justify-start h-full overflow-auto bg-green-500 p-4">
    <div v-if="columns" class="flex flex-row flex-wrap items-start justify-center md:justify-start">
      <BoardColumn
        v-for="(column, columnIndex) in columns"
        :key="column.id"
        class="mb-4 mr-4 bg-gray-300 p-2 text-left shadow-lg column"
        :column-index="columnIndex"
        :column="column"
      />
      <div class="mb-4 mr-4 bg-gray-300 p-2 text-left shadow-lg column">
        <input
          type="text"
          class="block w-full border border-transparent bg-white p-2 outline-none focus:border-green-500 transition duration-500"
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
