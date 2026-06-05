<script setup lang="ts">
import type { BoardColumnType } from 'src/services'
import ColumnTask from 'src/components/ColumnTask.vue'
import { move as moveColumn } from 'src/composables'
import { useAppStore } from 'src/store'

defineProps<{ columnIndex: number, column: BoardColumnType }>()

const store = useAppStore()

function createTask(event: Event, columnIndex: number) {
  const inputElement = event.target as HTMLInputElement
  store.commit('createTask', {
    columnIndex,
    name: inputElement.value,
  })
  inputElement.value = ''
}

const deleteColumn = (id: string) => store.commit('deleteColumn', { id })

function pickupColumn(event: DragEvent, fromColumnIndex: number) {
  const dataTransfer = event.dataTransfer

  if (dataTransfer) {
    dataTransfer.dropEffect = 'move'
    dataTransfer.effectAllowed = 'move'
    dataTransfer.setData('fromColumnIndex', fromColumnIndex.toString())
    dataTransfer.setData('type', 'column')
  }
}
</script>

<template>
  <div
    draggable="true"
    @dragenter.prevent
    @dragover.prevent
    @dragstart.stop="pickupColumn($event, columnIndex)"
    @drop.stop="moveColumn(store, $event, columnIndex)"
  >
    <div class="mb-2 flex items-center font-bold">
      <span>{{ column.name }}</span>
      <button
        class="btn-block danger ml-auto"
        @click.stop="deleteColumn(column.id)"
      >
        X
      </button>
    </div>
    <div v-if="column.tasks">
      <transition-group>
        <ColumnTask
          v-for="(task, taskIndex) in column.tasks"
          :key="task.id"
          :column-index="columnIndex"
          :task-index="taskIndex"
          :task="task"
        />
      </transition-group>
      <input
        type="text"
        class="block w-full border border-transparent bg-transparent p-2 outline-none focus:border-green-500 transition duration-500"
        placeholder="+ Enter new task ..."
        @keyup.enter="createTask($event, columnIndex)"
      >
    </div>
  </div>
</template>
