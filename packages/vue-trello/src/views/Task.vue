<script setup lang="ts">
import type { TaskType } from 'src/services'
import { useAppRouter } from 'src/router'
import { useAppStore } from 'src/store'
import { computed } from 'vue'

const props = defineProps<{ id: string }>()
const router = useAppRouter()
const store = useAppStore()
const task = computed(() => store.getters.getTask(props.id))

const close = () => router.push({ name: 'board' })

function updateTask(event: Event, task: TaskType, key: string) {
  store.commit('updateTask', {
    task,
    key,
    value: (event.target as HTMLInputElement).value,
  })
}
</script>

<template>
  <div class="absolute inset-0 bg-black/50" @click.stop.self="close">
    <div class="relative inset-0 m-32 mx-auto flex max-w-3xl flex-col bg-white p-8 text-left shadow-2xl">
      <input
        type="text"
        class="block w-full border border-transparent text-xl font-bold outline-none focus:border-green-500 focus:outline-none transition duration-500"
        :value="task.name"
        @change="updateTask($event, task, 'name')"
      >
      <textarea
        id="task-description"
        name="task-description"
        class="relative my-4 h-64 w-full border bg-transparent p-2 focus:border-green-500 focus:outline-none transition duration-500"
        placeholder="Task description here ..."
        :rows="10"
        :cols="30"
        :value="task.description"
        @change="updateTask($event, task, 'description')"
      />
      <button class="btn ml-auto" @click.stop="close">
        Close
      </button>
    </div>
  </div>
</template>
