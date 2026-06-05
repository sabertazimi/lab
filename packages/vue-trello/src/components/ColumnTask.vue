<script setup lang="ts">
import type { TaskType } from 'src/services'
import { move as moveTask } from 'src/composables'
import { useAppRouter } from 'src/router'
import { useAppStore } from 'src/store'

defineProps<{ columnIndex: number, taskIndex: number, task: TaskType }>()

const store = useAppStore()
const router = useAppRouter()

function goToTask(task: TaskType) {
  return router.push({ name: 'task', params: { id: task.id } })
}

function deleteTask(columnIndex: number, taskId: string) {
  return store.commit('deleteTask', { columnIndex, taskId })
}

function pickupTask(event: DragEvent, fromColumnIndex: number, fromTaskIndex: number) {
  const dataTransfer = event.dataTransfer

  if (dataTransfer) {
    dataTransfer.dropEffect = 'move'
    dataTransfer.effectAllowed = 'move'
    dataTransfer.setData('fromColumnIndex', fromColumnIndex.toString())
    dataTransfer.setData('fromTaskIndex', fromTaskIndex.toString())
  }
}
</script>

<template>
  <div
    class="mb-2 flex flex-wrap items-center cursor-pointer bg-white text-gray-900 no-underline shadow"
    draggable="true"
    @dragenter.prevent
    @dragover.prevent
    @dragstart.stop="pickupTask($event, columnIndex, taskIndex)"
    @drop.stop="moveTask(store, $event, columnIndex, taskIndex)"
    @click.stop="goToTask(task)"
  >
    <div class="flex w-full flex-shrink-0 flex-row items-center font-bold">
      <span class="px-4 py-2">{{ task.name }}</span>
      <button
        class="btn-block ml-auto"
        @click.stop="deleteTask(columnIndex, task.id)"
      >
        X
      </button>
    </div>
    <p v-if="task.description" class="mt-1 w-full flex-shrink-0 px-4 py-2">
      {{ task.description }}
    </p>
  </div>
</template>
