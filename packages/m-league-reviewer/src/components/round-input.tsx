import type { RoundInfo } from '@/api/data'
import { useEffect, useRef, useState } from 'react'
import { formatRound, numberToKanji } from '@/api/utils'
import { RoundLabel } from '@/components/round-label'
import { Button } from '@/components/ui/button'
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'
import { cn } from '@/lib/utils'

interface RoundInputProps {
  value: RoundInfo
  onChange: (value: RoundInfo) => void
  onClose?: () => void
  open?: boolean
  onOpenChange?: (open: boolean) => void
  existingRounds?: RoundInfo[]
}

export function RoundInput({ value, onChange, onClose, open, onOpenChange, existingRounds = [] }: RoundInputProps) {
  const [localValue, setLocalValue] = useState<RoundInfo>(value)
  const [error, setError] = useState<string>('')
  const roundButtonsRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    setLocalValue(value)
    setError('')
  }, [value])

  const isDuplicate = (round: RoundInfo): boolean => {
    return existingRounds.some(
      existing =>
        existing.field === round.field
        && existing.round === round.round
        && existing.honba === round.honba
        && !(existing.field === value.field && existing.round === value.round && existing.honba === value.honba),
    )
  }

  const handleFieldChange = (field: 'east' | 'south') => {
    setLocalValue({ ...localValue, field, round: 1, honba: 0 })
  }

  const handleRoundChange = (round: number) => {
    setLocalValue({ ...localValue, round, honba: 0 })
  }

  const handleHonbaChange = (honba: number) => {
    setLocalValue({ ...localValue, honba })
  }

  const handleConfirm = () => {
    if (isDuplicate(localValue)) {
      setError('该小局已存在，请选择其他小局')
      return
    }

    if (onOpenChange) {
      onOpenChange(false)
    }

    setTimeout(() => {
      onChange(localValue)
      if (onClose) {
        onClose()
      }
    }, 0)
  }

  const handleCancel = () => {
    setLocalValue(value)

    if (onOpenChange) {
      onOpenChange(false)
    }

    if (onClose) {
      onClose()
    }
  }

  return (
    <Popover open={open} onOpenChange={onOpenChange}>
      <PopoverTrigger asChild>
        <div className="flex min-h-[32px] w-full items-center">
          <span className={cn('text-sm', !value.field && 'text-muted-foreground')}>{formatRound(value) || '小局'}</span>
        </div>
      </PopoverTrigger>
      <PopoverContent className="w-auto p-3" align="start" onClick={e => e.stopPropagation()}>
        <div className="space-y-3">
          <div>
            <RoundLabel>场风</RoundLabel>
            <div className="flex gap-2">
              <Button
                size="sm"
                variant={localValue.field === 'east' ? 'default' : 'outline'}
                onClick={() => handleFieldChange('east')}
                className="flex-1"
              >
                東
              </Button>
              <Button
                size="sm"
                variant={localValue.field === 'south' ? 'default' : 'outline'}
                onClick={() => handleFieldChange('south')}
                className="flex-1"
              >
                南
              </Button>
            </div>
          </div>
          <div>
            <RoundLabel>小局</RoundLabel>
            <div ref={roundButtonsRef} className="flex gap-2">
              {[1, 2, 3, 4].map(num => (
                <Button
                  key={num}
                  size="sm"
                  variant={localValue.round === num ? 'default' : 'outline'}
                  onClick={() => handleRoundChange(num)}
                  className="flex-1"
                >
                  {numberToKanji(num)}
                </Button>
              ))}
            </div>
          </div>
          <div>
            <RoundLabel>本場</RoundLabel>
            <div className="grid grid-cols-5 gap-2">
              {[0, 1, 2, 3, 4, 5, 6, 7, 8, 9].map(num => (
                <Button
                  key={num}
                  size="sm"
                  variant={localValue.honba === num ? 'default' : 'outline'}
                  onClick={() => handleHonbaChange(num)}
                  className="w-10"
                >
                  {num}
                </Button>
              ))}
            </div>
          </div>
          {error && <div className="text-destructive bg-destructive/10 px-3 py-2 text-xs">{error}</div>}
          <div className="flex justify-end gap-2 pt-2">
            <Button size="sm" variant="outline" onClick={handleCancel}>
              取消
            </Button>
            <Button size="sm" onClick={handleConfirm}>
              确认
            </Button>
          </div>
        </div>
      </PopoverContent>
    </Popover>
  )
}
