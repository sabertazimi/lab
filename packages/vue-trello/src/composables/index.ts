import type { AppStore } from '../store'

function moveTask(store: AppStore, event: DragEvent, toColumnIndex: number, toTaskIndex?: number) {
  const dataTransfer = event.dataTransfer

  if (dataTransfer) {
    const fromColumnIndex = Number.parseInt(dataTransfer.getData('fromColumnIndex'))
    const fromTaskIndex = Number.parseInt(dataTransfer.getData('fromTaskIndex'))
    store.commit('moveTask', {
      fromColumnIndex,
      toColumnIndex,
      fromTaskIndex,
      toTaskIndex,
    })
  }
}

function moveColumn(store: AppStore, event: DragEvent, toColumnIndex: number) {
  const dataTransfer = event.dataTransfer

  if (dataTransfer) {
    const fromColumnIndex = Number.parseInt(dataTransfer.getData('fromColumnIndex'))
    store.commit('moveColumn', { fromColumnIndex, toColumnIndex })
  }
}

function move(store: AppStore, event: DragEvent, toColumnIndex: number, toTaskIndex?: number) {
  const dataTransfer = event.dataTransfer

  if (dataTransfer) {
    const type = dataTransfer.getData('type')

    if (type === 'column')
      moveColumn(store, event, toColumnIndex)
    else
      moveTask(store, event, toColumnIndex, toTaskIndex)
  }
}

export { move }
