/**
 * @see https://github.com/streamich/react-use/blob/master/src/useDebounce.ts
 */
import type { DependencyList } from 'react'
import { useEffect } from 'react'
import useTimeoutFn from '@/hooks/useTimeoutFn'

export type UseDebounceReturn = [() => boolean | null, () => void]

export default function useDebounce(
  fn: (...args: any[]) => void,
  ms: number = 0,
  deps: DependencyList = [],
): UseDebounceReturn {
  const [isReady, cancel, reset] = useTimeoutFn(fn, ms)

  // eslint-disable-next-line react/exhaustive-deps -- We don't need to pass all dependencies to the effect
  useEffect(reset, deps)

  return [isReady, cancel]
}
