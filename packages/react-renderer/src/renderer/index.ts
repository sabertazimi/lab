import type { ReactElement } from 'react'
import type { Container, OpaqueRoot } from '@/renderer/types'
import Reconciler from '@/renderer/reconciler'

const Renderer = {
  createRoot(
    container: Container | null,
    callback?: (root: OpaqueRoot) => void,
  ): OpaqueRoot {
    let root: OpaqueRoot | null = null

    if (container) {
      root = Reconciler.createContainer(
        container,
        0,
        null,
        true,
        null,
        '',
        (error: Error) => {
          console.error(error)
        },
        (error: Error) => {
          console.error(error)
        },
        (error: Error) => {
          console.error(error)
        },
        () => {
          // Default transition indicator callback
        },
      )

      root.render = function (element: ReactElement) {
        Reconciler.updateContainer(element, this, null)
      }

      if (callback) {
        callback(root)
      }

      return root
    }

    return root
  },
}

export default Renderer
