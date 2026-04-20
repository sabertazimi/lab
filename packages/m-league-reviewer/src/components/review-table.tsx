import type { HosetsuResult, RoundInfo, TableData } from '@/api/data'
import { PlusIcon, Trash2Icon } from 'lucide-react'
import { useCallback, useEffect, useRef, useState } from 'react'
import { toast } from 'sonner'
import { getTeamColorClass } from '@/api/data'
import { DefaultHosetsuResult, normalizeHosetsuResult, parseHosetsuResult } from '@/api/utils'
import { HosetsuResultContextMenu, HosetsuResultDisplay, HosetsuResultInput } from '@/components/hosetsu-result-input'
import { getPlayerOptions, PlayerDisplay, PlayerSelect } from '@/components/player-select'
import { RoundInput } from '@/components/round-input'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Table, TableBody, TableCell, TableRow } from '@/components/ui/table'
import { cn } from '@/lib/utils'

interface ReviewTableProps {
  tableData: TableData[]
  tableName: 'A' | 'B'
  selectedTeams: string[]
  editingField: string | null
  onEditField: (fieldId: string | null) => void
  onUpdatePlayer: (playerIndex: number, value: string) => void
  onUpdateRound: (roundIndex: number, value: RoundInfo) => void
  onUpdateResult: (roundIndex: number, playerIndex: number, value: HosetsuResult) => void
  onAddRow: () => void
  onRemoveRow: (roundIndex: number) => void
  onBlur: () => void
}

interface CellCoord {
  roundIndex: number
  playerIndex: number
}

function getCellCoord(cellId: string): CellCoord | null {
  const match = cellId.match(/result-(\d+)-(\d+)$/)
  if (match) {
    return {
      roundIndex: Number.parseInt(match[1], 10),
      playerIndex: Number.parseInt(match[2], 10),
    }
  }
  return null
}

function getCellsInRect(start: CellCoord, end: CellCoord, tableName: string): string[] {
  const minRow = Math.min(start.roundIndex, end.roundIndex)
  const maxRow = Math.max(start.roundIndex, end.roundIndex)
  const minCol = Math.min(start.playerIndex, end.playerIndex)
  const maxCol = Math.max(start.playerIndex, end.playerIndex)

  const cells: string[] = []
  for (let row = minRow; row <= maxRow; row++) {
    for (let col = minCol; col <= maxCol; col++) {
      cells.push(`${tableName}-result-${row}-${col}`)
    }
  }
  return cells
}

export function ReviewTable({
  tableData,
  tableName,
  selectedTeams,
  editingField,
  onEditField,
  onUpdatePlayer,
  onUpdateRound,
  onUpdateResult,
  onAddRow,
  onRemoveRow,
  onBlur,
}: ReviewTableProps) {
  const data = tableData.length > 0 ? tableData[0] : { players: ['', '', '', ''], rounds: [] }
  const playerOptions = getPlayerOptions()
  const tableRef = useRef<HTMLTableElement>(null)
  const [selectedCells, setSelectedCells] = useState<Set<string>>(() => new Set())

  const [isSelecting, setIsSelecting] = useState(false)
  const selectionStartRef = useRef<CellCoord | null>(null)
  const longPressTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const isLongPressRef = useRef(false)
  const LongPressThreshold = 300
  const LeftButton = 0

  const [isDragging, setIsDragging] = useState(false)
  const dragStartCoordRef = useRef<CellCoord | null>(null)

  const getFocusableCells = useCallback((): HTMLElement[] => {
    if (!tableRef.current)
      return []
    return Array.from(tableRef.current.querySelectorAll<HTMLElement>('[data-cell-id]'))
  }, [])

  const focusCell = useCallback((cellId: string) => {
    const cell = tableRef.current?.querySelector(`[data-cell-id="${cellId}"]`) as HTMLElement
    cell?.focus()
  }, [])

  const clearLongPressTimer = useCallback(() => {
    if (longPressTimerRef.current) {
      clearTimeout(longPressTimerRef.current)
      longPressTimerRef.current = null
    }
  }, [])

  const clearSelection = useCallback(() => {
    setSelectedCells(new Set())
    setIsSelecting(false)
    selectionStartRef.current = null
    isLongPressRef.current = false
  }, [])

  const getSelectedResults = useCallback((): { coord: CellCoord, result: HosetsuResult }[] => {
    const results: { coord: CellCoord, result: HosetsuResult }[] = []

    for (const cellId of selectedCells) {
      const coord = getCellCoord(cellId)

      if (coord && data.rounds[coord.roundIndex]) {
        results.push({
          coord,
          result: data.rounds[coord.roundIndex].results[coord.playerIndex],
        })
      }
    }

    return results.sort((a, b) => {
      if (a.coord.roundIndex !== b.coord.roundIndex) {
        return a.coord.roundIndex - b.coord.roundIndex
      }

      return a.coord.playerIndex - b.coord.playerIndex
    })
  }, [selectedCells, data.rounds])

  const getCellCoordFromPoint = useCallback(
    (x: number, y: number): CellCoord | null => {
      if (!tableRef.current) {
        return null
      }

      const cells = tableRef.current.querySelectorAll<HTMLElement>(`[data-cell-id^="${tableName}-result-"]`)

      for (const cell of cells) {
        const rect = cell.getBoundingClientRect()

        if (x >= rect.left && x <= rect.right && y >= rect.top && y <= rect.bottom) {
          const cellId = cell.getAttribute('data-cell-id')

          if (cellId) {
            return getCellCoord(cellId)
          }
        }
      }

      // 如果鼠标不在任何单元格内，找最近的边界单元格
      let nearestCoord: CellCoord | null = null
      let minDistance = Infinity

      for (const cell of cells) {
        const rect = cell.getBoundingClientRect()
        const cellId = cell.getAttribute('data-cell-id')

        if (!cellId) {
          continue
        }

        const coord = getCellCoord(cellId)

        if (!coord) {
          continue
        }

        // 计算到单元格中心的距离
        const centerX = (rect.left + rect.right) / 2
        const centerY = (rect.top + rect.bottom) / 2
        const distance = Math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2)

        if (distance < minDistance) {
          minDistance = distance
          nearestCoord = coord
        }
      }

      return nearestCoord
    },
    [tableName],
  )

  const handleCellClick = useCallback(
    (_e: React.MouseEvent, fieldId: string) => {
      if (selectedCells.size > 0) {
        clearSelection()
      }

      onEditField(fieldId)
    },
    [selectedCells, clearSelection, onEditField],
  )

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent, currentCellId: string) => {
      const cells = getFocusableCells()
      const currentIndex = cells.findIndex(cell => cell.getAttribute('data-cell-id') === currentCellId)

      if (currentIndex === -1) {
        return
      }

      let targetIndex = currentIndex
      const columnsPerRow = 5

      switch (e.key) {
        case 'ArrowUp':
          e.preventDefault()
          targetIndex = currentIndex - columnsPerRow
          break
        case 'ArrowDown':
          e.preventDefault()
          targetIndex = currentIndex + columnsPerRow
          break
        case 'ArrowLeft':
          e.preventDefault()
          targetIndex = currentIndex - 1
          break
        case 'ArrowRight':
          e.preventDefault()
          targetIndex = currentIndex + 1
          break
        case 'Enter':
        case ' ':
          e.preventDefault()
          onEditField(currentCellId)
          return
        case 'Escape':
          e.preventDefault()
          onEditField(null)
          focusCell(currentCellId)
          return
      }

      if (e.key === 'Tab' && e.shiftKey) {
        e.preventDefault()
        targetIndex = currentIndex - 1
      }

      if (targetIndex >= 0 && targetIndex < cells.length) {
        const targetCell = cells[targetIndex]

        if (targetCell) {
          targetCell.focus()
        }
      }
    },
    [getFocusableCells, onEditField, focusCell],
  )

  const handleCellMouseDown = useCallback(
    (e: React.MouseEvent, fieldId: string) => {
      if (e.button !== LeftButton) {
        return
      }

      const coord = getCellCoord(fieldId)

      if (!coord) {
        return
      }

      isLongPressRef.current = false
      longPressTimerRef.current = setTimeout(() => {
        isLongPressRef.current = true
        setIsSelecting(true)
        selectionStartRef.current = coord
        setSelectedCells(new Set([fieldId]))
      }, LongPressThreshold)
    },
    [LongPressThreshold],
  )

  const handleCellMouseUp = useCallback(
    (e: React.MouseEvent, _fieldId: string) => {
      clearLongPressTimer()

      if (isLongPressRef.current) {
        setIsSelecting(false)
        isLongPressRef.current = false
        e.preventDefault()
        e.stopPropagation()
      }
    },
    [clearLongPressTimer],
  )

  const handleCellMouseEnter = useCallback(
    (fieldId: string) => {
      if (!isSelecting || !selectionStartRef.current) {
        return
      }

      const coord = getCellCoord(fieldId)

      if (!coord) {
        return
      }

      const cells = getCellsInRect(selectionStartRef.current, coord, tableName)
      setSelectedCells(new Set(cells))
    },
    [isSelecting, tableName],
  )

  const handleCellMouseLeave = useCallback(() => {
    if (!isSelecting) {
      clearLongPressTimer()
    }
  }, [isSelecting, clearLongPressTimer])

  const handleEdgeDragStart = useCallback(() => {
    if (!editingField) {
      return
    }

    const coord = getCellCoord(editingField)

    if (!coord) {
      return
    }

    dragStartCoordRef.current = coord
    setIsDragging(true)
    onEditField(null)
  }, [editingField, onEditField])

  useEffect(() => {
    if (!isDragging) {
      return
    }

    const handleEdgeDragMove = (e: MouseEvent) => {
      const currentCoord = getCellCoordFromPoint(e.clientX, e.clientY)

      if (!currentCoord || !dragStartCoordRef.current) {
        return
      }

      const cells = getCellsInRect(dragStartCoordRef.current, currentCoord, tableName)
      setSelectedCells(new Set(cells))
    }

    const handleEdgeDragEnd = () => {
      setIsDragging(false)
      dragStartCoordRef.current = null
    }

    document.addEventListener('mousemove', handleEdgeDragMove)
    document.addEventListener('mouseup', handleEdgeDragEnd)

    return () => {
      document.removeEventListener('mousemove', handleEdgeDragMove)
      document.removeEventListener('mouseup', handleEdgeDragEnd)
    }
  }, [isDragging, getCellCoordFromPoint, tableName])

  useEffect(() => {
    const handleGlobalMouseUp = () => {
      clearLongPressTimer()

      if (isSelecting) {
        setIsSelecting(false)
        isLongPressRef.current = false
      }
    }

    document.addEventListener('mouseup', handleGlobalMouseUp)
    return () => {
      document.removeEventListener('mouseup', handleGlobalMouseUp)
    }
  }, [isSelecting, clearLongPressTimer])

  useEffect(() => {
    if (selectedCells.size === 0) {
      return
    }

    const handleGlobalClick = (e: MouseEvent) => {
      if (tableRef.current && !tableRef.current.contains(e.target as Node)) {
        clearSelection()
      }
    }

    document.addEventListener('click', handleGlobalClick)
    return () => {
      document.removeEventListener('click', handleGlobalClick)
    }
  }, [selectedCells.size, clearSelection])

  const handleBatchCopy = useCallback(() => {
    const results = getSelectedResults()
    if (results.length === 0) {
      return
    }

    const dataToClipboard = results.map(r => r.result)
    const text = JSON.stringify(dataToClipboard)
    navigator.clipboard
      .writeText(text)
      .then(() => toast.success(`已复制 ${results.length} 个单元格`))
      .catch((err: unknown) => toast.error(`复制失败: ${err instanceof Error ? err.message : String(err)}`))
  }, [getSelectedResults])

  const handleBatchCut = useCallback(() => {
    const results = getSelectedResults()
    if (results.length === 0) {
      return
    }

    const dataToClipboard = results.map(r => r.result)
    const text = JSON.stringify(dataToClipboard)
    navigator.clipboard
      .writeText(text)
      .then(() => {
        for (const { coord } of results) {
          onUpdateResult(coord.roundIndex, coord.playerIndex, DefaultHosetsuResult)
        }

        onBlur()
        toast.success(`已剪切 ${results.length} 个单元格`)
      })
      .catch((err: unknown) => toast.error(`剪切失败: ${err instanceof Error ? err.message : String(err)}`))
  }, [getSelectedResults, onUpdateResult, onBlur])

  const handleBatchPaste = useCallback(async () => {
    const results = getSelectedResults()

    if (results.length === 0) {
      return
    }

    try {
      const text = await navigator.clipboard.readText()
      let parsedArray: HosetsuResult[] | null = null

      try {
        const parsed = JSON.parse(text) as unknown

        if (Array.isArray(parsed)) {
          parsedArray = parsed
            .map(item => normalizeHosetsuResult(item))
            .filter((item): item is HosetsuResult => item !== null)
        }
      } catch {}

      const parsedSingle = parseHosetsuResult(text)

      if (parsedArray && parsedArray.length > 0) {
        const count = Math.min(parsedArray.length, results.length)

        for (let i = 0; i < count; i++) {
          const { coord } = results[i]
          onUpdateResult(coord.roundIndex, coord.playerIndex, parsedArray[i])
        }

        onBlur()
        toast.success(`已粘贴 ${count} 个单元格`)
      } else if (parsedSingle) {
        for (const { coord } of results) {
          onUpdateResult(coord.roundIndex, coord.playerIndex, parsedSingle)
        }

        onBlur()
        toast.success(`已粘贴到 ${results.length} 个单元格`)
      } else {
        toast.warning('无法解析剪贴板内容')
      }
    } catch (err: unknown) {
      toast.error(`粘贴失败: ${err instanceof Error ? err.message : String(err)}`)
    }
  }, [getSelectedResults, onUpdateResult, onBlur])

  const handleBatchToggleSignificant = useCallback(() => {
    const results = getSelectedResults()

    if (results.length === 0) {
      return
    }

    const allSignificant = results.every(r => r.result.isSignificant)
    const newValue = !allSignificant

    for (const { coord, result } of results) {
      onUpdateResult(coord.roundIndex, coord.playerIndex, {
        ...result,
        isSignificant: newValue,
      })
    }

    onBlur()
    toast.success(`已${newValue ? '标记' : '取消标记'}为严重: ${results.length} 个单元格`)
  }, [getSelectedResults, onUpdateResult, onBlur])

  const handleBatchClear = useCallback(() => {
    const results = getSelectedResults()

    if (results.length === 0) {
      return
    }

    for (const { coord } of results) {
      onUpdateResult(coord.roundIndex, coord.playerIndex, DefaultHosetsuResult)
    }

    onBlur()
    toast.success(`已清空 ${results.length} 个单元格`)
  }, [getSelectedResults, onUpdateResult, onBlur])

  useEffect(() => {
    const handleGlobalKeyDown = (e: KeyboardEvent) => {
      if (selectedCells.size === 0) {
        return
      }

      if (e.key === 'Backspace' || e.key === 'Delete') {
        e.preventDefault()
        handleBatchClear()
        return
      }

      if (!e.ctrlKey && !e.metaKey) {
        return
      }

      switch (e.key.toLowerCase()) {
        case 'c':
          e.preventDefault()
          handleBatchCopy()
          break
        case 'x':
          e.preventDefault()
          handleBatchCut()
          break
        case 'v':
          e.preventDefault()
          void handleBatchPaste()
          break
        case 'b':
          e.preventDefault()
          handleBatchToggleSignificant()
          break
      }
    }

    document.addEventListener('keydown', handleGlobalKeyDown)
    return () => {
      document.removeEventListener('keydown', handleGlobalKeyDown)
    }
  }, [selectedCells, handleBatchCopy, handleBatchCut, handleBatchPaste, handleBatchToggleSignificant, handleBatchClear])

  return (
    <Card className="rounded-xs">
      <CardHeader>
        <CardTitle>
          {tableName}
          桌
        </CardTitle>
      </CardHeader>
      <CardContent>
        <Table ref={tableRef}>
          <TableBody>
            <TableRow className="bg-accent">
              <TableCell className="w-24 font-semibold">小局</TableCell>
              {[0, 1, 2, 3].map((playerIndex) => {
                const fieldId = `${tableName}-player-${playerIndex}`
                const isEditing = editingField === fieldId
                const playerName = data.players[playerIndex]
                const playerTeamId = playerName ? playerOptions.find(p => p.value === playerName)?.teamId : undefined
                const teamColors = playerTeamId ? getTeamColorClass(playerTeamId) : ''

                return (
                  <TableCell
                    key={playerIndex}
                    data-cell-id={fieldId}
                    tabIndex={isEditing ? -1 : 0}
                    role="button"
                    aria-label={`选手 ${playerIndex + 1}: ${playerName || '未选择'}`}
                    className={cn(
                      'focus-visible:ring-primary cursor-pointer transition-all focus-visible:ring-2 focus-visible:outline-none focus-visible:ring-inset',
                      teamColors,
                    )}
                    onClick={() => !isEditing && onEditField(fieldId)}
                    onKeyDown={e => !isEditing && handleKeyDown(e, fieldId)}
                  >
                    {isEditing ? (
                      <PlayerSelect
                        value={data.players[playerIndex]}
                        onChange={(value) => {
                          onUpdatePlayer(playerIndex, value)
                          onEditField(null)
                          setTimeout(focusCell, 0, fieldId)
                        }}
                        open={isEditing}
                        onOpenChange={(open) => {
                          if (!open) {
                            onEditField(null)
                            focusCell(fieldId)
                          }
                        }}
                        placeholder={`プロ ${playerIndex + 1}`}
                        filterByTeams={selectedTeams}
                      />
                    ) : (
                      <PlayerDisplay
                        playerName={data.players[playerIndex]}
                        playerOptions={playerOptions}
                        placeholder={`プロ ${playerIndex + 1}`}
                      />
                    )}
                  </TableCell>
                )
              })}
              <TableCell className="w-12"></TableCell>
            </TableRow>
            {data.rounds.map((round, roundIndex) => (
              <TableRow key={`${round.round.field}-${round.round.round}-${round.round.honba}`}>
                <TableCell
                  data-cell-id={`${tableName}-round-${roundIndex}`}
                  tabIndex={editingField === `${tableName}-round-${roundIndex}` ? -1 : 0}
                  role="button"
                  aria-label={`局数: ${roundIndex + 1}`}
                  className={cn(
                    'focus-visible:ring-primary cursor-pointer transition-all focus-visible:ring-2 focus-visible:outline-none focus-visible:ring-inset',
                  )}
                  onClick={() => {
                    if (editingField !== `${tableName}-round-${roundIndex}`) {
                      onEditField(`${tableName}-round-${roundIndex}`)
                    }
                  }}
                  onKeyDown={e =>
                    editingField !== `${tableName}-round-${roundIndex}`
                    && handleKeyDown(e, `${tableName}-round-${roundIndex}`)}
                >
                  <RoundInput
                    value={round.round}
                    onChange={(value) => {
                      onUpdateRound(roundIndex, value)
                      onBlur()
                    }}
                    open={editingField === `${tableName}-round-${roundIndex}`}
                    onOpenChange={(open) => {
                      if (!open) {
                        onEditField(null)
                      }
                    }}
                    existingRounds={data.rounds.map(r => r.round)}
                  />
                </TableCell>
                {[0, 1, 2, 3].map((playerIndex) => {
                  const fieldId = `${tableName}-result-${roundIndex}-${playerIndex}`
                  const isEditing = editingField === fieldId
                  const isSelected = selectedCells.has(fieldId)
                  const result = round.results[playerIndex]
                  return (
                    <TableCell
                      key={playerIndex}
                      data-cell-id={fieldId}
                      tabIndex={isEditing ? -1 : 0}
                      role="button"
                      aria-label={`第 ${roundIndex + 1} 局，选手 ${playerIndex + 1} 结果`}
                      className={cn(
                        'focus-visible:ring-primary cursor-text p-0 transition-all focus-visible:ring-2 focus-visible:outline-none focus-visible:ring-inset',
                        isSelected && 'ring-primary ring-2 ring-inset',
                        isEditing && 'ring-primary ring-2 ring-inset',
                      )}
                      onClick={e => handleCellClick(e, fieldId)}
                      onKeyDown={e => !isEditing && handleKeyDown(e, fieldId)}
                      onMouseDown={e => handleCellMouseDown(e, fieldId)}
                      onMouseUp={e => handleCellMouseUp(e, fieldId)}
                      onMouseEnter={() => handleCellMouseEnter(fieldId)}
                      onMouseLeave={handleCellMouseLeave}
                    >
                      {isEditing ? (
                        <HosetsuResultInput
                          value={result}
                          onChange={value => onUpdateResult(roundIndex, playerIndex, value)}
                          onClose={() => {
                            onEditField(null)
                            onBlur()
                            setTimeout(focusCell, 0, fieldId)
                          }}
                          onEdgeDragStart={handleEdgeDragStart}
                          autoFocus
                        />
                      ) : (
                        <HosetsuResultContextMenu
                          value={result}
                          onChange={value => onUpdateResult(roundIndex, playerIndex, value)}
                          disabled={isSelected}
                        >
                          <HosetsuResultDisplay value={result} />
                        </HosetsuResultContextMenu>
                      )}
                    </TableCell>
                  )
                })}
                <TableCell align="center" className="p-0">
                  <Button
                    size="icon-lg"
                    variant="ghost"
                    onClick={() => onRemoveRow(roundIndex)}
                    aria-label={`删除第 ${roundIndex + 1} 局`}
                  >
                    <Trash2Icon className="text-destructive size-4" />
                  </Button>
                </TableCell>
              </TableRow>
            ))}
            <TableRow className="hover:bg-accent group border-none transition-all">
              <TableCell colSpan={6} className="h-11 border-none p-0">
                <div
                  className="flex size-full cursor-pointer items-center justify-center opacity-0 transition-all duration-200 group-hover:opacity-100"
                  onClick={onAddRow}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' || e.key === ' ') {
                      e.preventDefault()
                      onAddRow()
                    }
                  }}
                  role="button"
                  tabIndex={0}
                  title="添加局数"
                  aria-label="添加新局数"
                >
                  <PlusIcon className="text-primary size-4" />
                </div>
              </TableCell>
            </TableRow>
            <TableRow className="pointer-events-none border-none opacity-0" aria-hidden="true">
              <TableCell className="h-12 border-none p-0" />
              <TableCell className="h-12 border-none p-0" />
              <TableCell className="h-12 border-none p-0" />
              <TableCell className="h-12 border-none p-0" />
              <TableCell className="h-12 border-none p-0" />
              <TableCell className="h-12 border-none p-0" />
            </TableRow>
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  )
}
