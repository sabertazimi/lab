import type { ButtonProps } from '@/components/ui/button'
import { Moon, Sun } from 'lucide-react'
import { useCallback, useEffect, useRef, useState } from 'react'
import { flushSync } from 'react-dom'
import { Button } from '@/components/ui/button'
import { cn } from '@/lib/utils'

interface ThemeSwitcherProps extends React.ComponentPropsWithoutRef<'button'> {
  size?: ButtonProps['size']
  iconClassName?: string
  duration?: number
}

export function ThemeSwitcher({
  className,
  size = 'icon-xl',
  iconClassName,
  duration = 400,
  ...props
}: ThemeSwitcherProps) {
  const [isDark, setIsDark] = useState(false)
  const buttonRef = useRef<HTMLButtonElement>(null)

  useEffect(() => {
    const updateTheme = () => {
      // eslint-disable-next-line react/set-state-in-effect -- we need to set the state directly here
      setIsDark(document.documentElement.classList.contains('dark'))
    }

    updateTheme()

    const observer = new MutationObserver(updateTheme)
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class'],
    })

    return () => observer.disconnect()
  }, [])

  const toggleTheme = useCallback(async () => {
    if (!buttonRef.current) {
      return
    }

    await document.startViewTransition(() => {
      // eslint-disable-next-line react-dom/no-flush-sync -- flushSync is used to ensure the DOM is updated immediately
      flushSync(() => {
        const newTheme = !isDark
        setIsDark(newTheme)
        document.documentElement.classList.toggle('dark')
        localStorage.setItem('theme', newTheme ? 'dark' : 'light')
      })
    }).ready

    const { top, left, width, height } = buttonRef.current.getBoundingClientRect()
    const x = left + width / 2
    const y = top + height / 2
    const maxRadius = Math.hypot(Math.max(left, window.innerWidth - left), Math.max(top, window.innerHeight - top))

    document.documentElement.animate(
      {
        clipPath: [`circle(0px at ${x}px ${y}px)`, `circle(${maxRadius}px at ${x}px ${y}px)`],
      },
      {
        duration,
        easing: 'ease-in-out',
        pseudoElement: '::view-transition-new(root)',
      },
    )
  }, [isDark, duration])

  return (
    <Button
      ref={buttonRef}
      variant="link"
      size={size}
      // eslint-disable-next-line ts/no-misused-promises -- toggleTheme is a valid promise
      onClick={toggleTheme}
      className={cn('text-muted-foreground hover:text-primary transition-colors', className)}
      {...props}
    >
      {isDark ? <Moon className={cn('size-6', iconClassName)} /> : <Sun className={cn('size-6', iconClassName)} />}
      <span className="sr-only">Toggle theme</span>
    </Button>
  )
}
