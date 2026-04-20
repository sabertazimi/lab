/**
 * @see https://github.com/streamich/react-use/blob/master/src/useTimeoutFn.ts
 */
import { useCallback, useEffect, useRef } from 'react'

export type UseTimeoutFnReturn = [() => boolean | null, () => void, () => void]

export default function useTimeoutFn(fn: (...args: any[]) => void, ms: number = 0): UseTimeoutFnReturn {
  const readyRef = useRef<boolean | null>(false)
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const callbackRef = useRef(fn)

  const isReady = useCallback(() => readyRef.current, [])

  const set = useCallback(() => {
    readyRef.current = false
    timeoutRef.current && clearTimeout(timeoutRef.current)

    timeoutRef.current = setTimeout(() => {
      readyRef.current = true
      callbackRef.current()
    }, ms)
  }, [ms])

  const clear = useCallback(() => {
    readyRef.current = null
    timeoutRef.current && clearTimeout(timeoutRef.current)
  }, [])

  // update ref when function changes
  useEffect(() => {
    callbackRef.current = fn
  }, [fn])

  // set on mount, clear on unmount
  useEffect(() => {
    set()

    return clear
    // eslint-disable-next-line react/exhaustive-deps -- We don't need to pass all dependencies to the effect
  }, [ms])

  return [isReady, clear, set]
}
