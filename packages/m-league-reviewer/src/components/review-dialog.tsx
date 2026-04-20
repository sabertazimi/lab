import type { HosetsuResult, RoundInfo, TableData } from '@/api/data'
import type { MultiSelectOption } from '@/components/ui/multi-select'
import { format } from 'date-fns'
import { zhCN } from 'date-fns/locale/zh-CN'
import DOMPurify from 'dompurify'
import { CalendarIcon, LinkIcon, LoaderIcon, UsersIcon } from 'lucide-react'
import { useEffect, useRef, useState } from 'react'
import { getTeamColorClassByName, statusConfig, teams } from '@/api/data'
import { createDefaultRoundInfo, createEmptyHosetsuResult } from '@/api/utils'
import { EditableField } from '@/components/editable-field'
import { ReviewItem } from '@/components/review-item'
import { ReviewLabel } from '@/components/review-label'
import { ReviewRow } from '@/components/review-row'
import { ReviewTable } from '@/components/review-table'
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from '@/components/ui/alert-dialog'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Calendar } from '@/components/ui/calendar'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog'
import { Input } from '@/components/ui/input'
import { MultiSelect } from '@/components/ui/multi-select'
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Textarea } from '@/components/ui/textarea'
import useDebounce from '@/hooks/useDebounce'
import { cn } from '@/lib/utils'
import { useReviewsStore } from '@/stores/reviews'

interface ReviewDialogProps {
  open: boolean
  onOpenChange: (open: boolean) => void
  reviewId: string | null
}

export function ReviewDialog({ open, onOpenChange, reviewId }: ReviewDialogProps) {
  const { getReviewById, updateReview, deleteReview } = useReviewsStore()
  const [title, setTitle] = useState('')
  const [linkA, setLinkA] = useState('')
  const [linkB, setLinkB] = useState('')
  const [selectedTeams, setSelectedTeams] = useState<string[]>([])
  const [reviewDate, setReviewDate] = useState<Date>()
  const [status, setStatus] = useState<'not_started' | 'in_progress' | 'completed'>('not_started')
  const [socialUrl, setSocialUrl] = useState('')
  const [tableA, setTableA] = useState<TableData[]>([])
  const [tableB, setTableB] = useState<TableData[]>([])
  const [content, setContent] = useState('')
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false)
  const [editingField, setEditingField] = useState<string | null>(null)

  const titleFieldRef = useRef<HTMLDivElement>(null)
  const linkAFieldRef = useRef<HTMLDivElement>(null)
  const linkBFieldRef = useRef<HTMLDivElement>(null)
  const socialUrlFieldRef = useRef<HTMLDivElement>(null)
  const contentFieldRef = useRef<HTMLDivElement>(null)

  const fieldRefMap: Record<string, React.RefObject<HTMLDivElement | null>> = {
    title: titleFieldRef,
    linkA: linkAFieldRef,
    linkB: linkBFieldRef,
    socialUrl: socialUrlFieldRef,
    content: contentFieldRef,
  }

  const focusField = (field: string) => {
    const ref = fieldRefMap[field]
    if (ref?.current) {
      ref.current.focus()
    }
  }

  const autoSave = () => {
    if (!reviewId || !title.trim()) {
      return
    }

    updateReview(reviewId, {
      title: title.trim(),
      linkA,
      linkB,
      teams: selectedTeams,
      date: reviewDate ? format(reviewDate, 'yyyy-MM-dd') : '',
      status,
      socialUrl,
      tableA,
      tableB,
      content: content.trim(),
    })
  }

  useDebounce(
    () => {
      if (!reviewId || !title.trim())
        return
      autoSave()
    },
    300,
    [title, linkA, linkB, selectedTeams, reviewDate, status, socialUrl, tableA, tableB, content],
  )

  const teamOptions: MultiSelectOption[] = teams.map(team => ({
    label: team.teamName,
    value: team.teamName,
    className: getTeamColorClassByName(team.teamName),
  }))

  useEffect(() => {
    if (open && reviewId) {
      const review = getReviewById(reviewId)
      if (review) {
        setTitle(review.title)
        setLinkA(review.linkA || '')
        setLinkB(review.linkB || '')
        setSelectedTeams(review.teams || [])
        setReviewDate(review.date ? new Date(review.date) : undefined)
        setStatus(review.status || 'not_started')
        setSocialUrl(review.socialUrl || '')
        setTableA(review.tableA || [])
        setTableB(review.tableB || [])
        setContent(review.content || '')
        setEditingField(null)
      }
    }
  }, [open, reviewId, getReviewById])

  // 当编辑队伍字段时,自动触发 MultiSelect 打开
  useEffect(() => {
    if (editingField === 'teams') {
      const timeout = setTimeout(() => {
        const button = document.querySelector('[data-team-multi-select] button')
        if (button instanceof HTMLElement) {
          button.click()
        }
      }, 10)
      return () => clearTimeout(timeout)
    }
  }, [editingField])

  const confirmDelete = () => {
    if (!reviewId)
      return
    deleteReview(reviewId)
    setDeleteDialogOpen(false)
    onOpenChange(false)
  }

  const handleBlur = () => {
    setEditingField(null)
    autoSave()
  }

  const handleInputKeyDown = (e: React.KeyboardEvent, field: string) => {
    if (e.key === 'Enter' || e.key === 'Escape' || ((e.ctrlKey || e.metaKey) && e.key === 's')) {
      e.preventDefault()
      setEditingField(null)
      autoSave()
      setTimeout(focusField, 0, field)
    }
  }

  const addTableRow = (table: 'A' | 'B') => {
    const currentTable = table === 'A' ? tableA : tableB
    const setTable = table === 'A' ? setTableA : setTableB

    if (currentTable.length === 0) {
      setTable([{ players: ['', '', '', ''], rounds: [] }])
    } else {
      const newTable = [...currentTable]
      const existingRounds = newTable[0].rounds.map(r => r.round)
      newTable[0].rounds.push({
        round: createDefaultRoundInfo(existingRounds),
        results: [
          createEmptyHosetsuResult(),
          createEmptyHosetsuResult(),
          createEmptyHosetsuResult(),
          createEmptyHosetsuResult(),
        ],
      })
      setTable(newTable)
    }
  }

  const removeTableRow = (table: 'A' | 'B', roundIndex: number) => {
    const currentTable = table === 'A' ? tableA : tableB
    const setTable = table === 'A' ? setTableA : setTableB

    if (currentTable.length > 0) {
      const newTable = [...currentTable]
      newTable[0].rounds = newTable[0].rounds.filter((_, i) => i !== roundIndex)
      setTable(newTable)
    }
  }

  const updatePlayer = (table: 'A' | 'B', playerIndex: number, value: string) => {
    const currentTable = table === 'A' ? tableA : tableB
    const setTable = table === 'A' ? setTableA : setTableB

    if (currentTable.length === 0) {
      const newTable = { players: ['', '', '', ''], rounds: [] }
      newTable.players[playerIndex] = value
      setTable([newTable])
    } else {
      const newTable = [...currentTable]
      newTable[0].players[playerIndex] = value
      setTable(newTable)
    }
  }

  const updateRound = (table: 'A' | 'B', roundIndex: number, value: RoundInfo) => {
    const currentTable = table === 'A' ? tableA : tableB
    const setTable = table === 'A' ? setTableA : setTableB

    if (currentTable.length > 0) {
      const newTable = [...currentTable]
      newTable[0].rounds[roundIndex].round = value
      setTable(newTable)
    }
  }

  const updateResult = (table: 'A' | 'B', roundIndex: number, playerIndex: number, value: HosetsuResult) => {
    const currentTable = table === 'A' ? tableA : tableB
    const setTable = table === 'A' ? setTableA : setTableB

    if (currentTable.length > 0) {
      const newTable = [...currentTable]
      newTable[0].rounds[roundIndex].results[playerIndex] = value
      setTable(newTable)
    }
  }

  return (
    <>
      <Dialog open={open} onOpenChange={onOpenChange}>
        <DialogContent className="max-w-full rounded-xs p-0 sm:max-w-full" disableCloseButton>
          <div className="flex h-screen flex-col">
            <div className="border-border flex items-center justify-between border-b px-6 py-3">
              <span className="text-muted-foreground font-mono text-xs">review.tsx</span>
              <div className="flex items-center gap-2">
                <Button size="sm" variant="destructive" onClick={() => setDeleteDialogOpen(true)}>
                  删除
                </Button>
                <DialogClose asChild>
                  <Button size="sm">关闭</Button>
                </DialogClose>
              </div>
            </div>
            <DialogHeader className="border-border border-b px-6 py-4">
              <div className="flex items-center justify-between">
                <div className="flex-1">
                  <DialogDescription className="font-mono">比赛复盘</DialogDescription>
                  <DialogTitle className="text-foreground mt-1 font-mono text-2xl font-bold">
                    {title || '复盘详情'}
                  </DialogTitle>
                </div>
              </div>
            </DialogHeader>
            <div className="flex-1 overflow-y-auto py-6">
              <div className="bg-border space-y-px">
                <Card className="rounded-xs">
                  <CardHeader>
                    <EditableField
                      ref={titleFieldRef}
                      isEditing={editingField === 'title'}
                      onEdit={() => setEditingField('title')}
                      className="-mx-3 -my-2"
                      editComponent={(
                        <Input
                          value={title}
                          onChange={e => setTitle(e.target.value)}
                          onBlur={handleBlur}
                          onKeyDown={e => handleInputKeyDown(e, 'title')}
                          autoFocus
                          placeholder="输入标题..."
                          className="text-lg font-semibold"
                        />
                      )}
                      displayComponent={
                        <CardTitle>{title || <span className="text-muted-foreground">输入标题...</span>}</CardTitle>
                      }
                    />
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <ReviewRow>
                      <ReviewItem>
                        <ReviewLabel>
                          <LinkIcon className="text-primary size-4" />
                          牌谱A
                        </ReviewLabel>
                        <EditableField
                          ref={linkAFieldRef}
                          isEditing={editingField === 'linkA'}
                          onEdit={() => setEditingField('linkA')}
                          className="mt-1"
                          editComponent={(
                            <Input
                              value={linkA}
                              onChange={e => setLinkA(DOMPurify.sanitize(e.target.value))}
                              onBlur={handleBlur}
                              onKeyDown={e => handleInputKeyDown(e, 'linkA')}
                              autoFocus
                              className="-mx-3 -my-2 h-8"
                            />
                          )}
                          displayComponent={(
                            <p className="min-h-[32px] truncate leading-8">
                              {linkA ? (
                                <a
                                  href={linkA}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="text-primary hover:underline"
                                  onClick={e => e.stopPropagation()}
                                >
                                  {linkA}
                                </a>
                              ) : (
                                <span className="text-muted-foreground">{linkA}</span>
                              )}
                            </p>
                          )}
                        />
                      </ReviewItem>
                      <ReviewItem>
                        <ReviewLabel>
                          <LinkIcon className="text-primary size-4" />
                          牌谱B
                        </ReviewLabel>
                        <EditableField
                          ref={linkBFieldRef}
                          isEditing={editingField === 'linkB'}
                          onEdit={() => setEditingField('linkB')}
                          className="mt-1"
                          editComponent={(
                            <Input
                              value={linkB}
                              onChange={e => setLinkB(DOMPurify.sanitize(e.target.value))}
                              onBlur={handleBlur}
                              onKeyDown={e => handleInputKeyDown(e, 'linkB')}
                              autoFocus
                              className="-mx-3 -my-2 h-8"
                            />
                          )}
                          displayComponent={(
                            <p className="min-h-[32px] truncate leading-8">
                              {linkB ? (
                                <a
                                  href={linkB}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="text-primary hover:underline"
                                  onClick={e => e.stopPropagation()}
                                >
                                  {linkB}
                                </a>
                              ) : (
                                <span className="text-muted-foreground">{linkB}</span>
                              )}
                            </p>
                          )}
                        />
                      </ReviewItem>
                    </ReviewRow>
                    <ReviewRow>
                      <ReviewItem>
                        <ReviewLabel>
                          <CalendarIcon className="text-primary size-4" />
                          日期
                        </ReviewLabel>
                        <Popover
                          open={editingField === 'date'}
                          onOpenChange={(open) => {
                            if (open) {
                              setEditingField('date')
                            } else {
                              setEditingField(null)
                              autoSave()
                            }
                          }}
                        >
                          <PopoverTrigger asChild>
                            <div
                              className={cn(
                                'mt-1 cursor-pointer px-3 py-2 transition-all rounded-md',
                                editingField !== 'date' && 'hover:bg-accent',
                              )}
                            >
                              <div className="flex min-h-[32px] items-center">
                                <span>
                                  {reviewDate ? (
                                    format(reviewDate, 'yyyy-MM-dd')
                                  ) : (
                                    <span className="text-muted-foreground">选择日期</span>
                                  )}
                                </span>
                              </div>
                            </div>
                          </PopoverTrigger>
                          <PopoverContent className="w-auto p-0">
                            <Calendar
                              mode="single"
                              selected={reviewDate}
                              locale={zhCN}
                              onSelect={(date) => {
                                setReviewDate(date)
                                setEditingField(null)
                              }}
                            />
                          </PopoverContent>
                        </Popover>
                      </ReviewItem>
                      <ReviewItem>
                        <ReviewLabel>
                          <LoaderIcon className="text-primary size-4" />
                          状态
                        </ReviewLabel>
                        <EditableField
                          isEditing={editingField === 'status'}
                          onEdit={() => setEditingField('status')}
                          className="mt-1"
                          cursorType="pointer"
                          editComponent={(
                            <Select
                              value={status}
                              onValueChange={(v) => {
                                setStatus(v as 'not_started' | 'in_progress' | 'completed')
                                setEditingField(null)
                                setTimeout(autoSave, 100)
                              }}
                              open={true}
                              onOpenChange={(open) => {
                                if (!open) {
                                  setEditingField(null)
                                }
                              }}
                            >
                              <SelectTrigger className="-mx-3 -my-2 h-8">
                                <SelectValue />
                              </SelectTrigger>
                              <SelectContent>
                                {Object.entries(statusConfig).map(([key, config]) => (
                                  <SelectItem key={key} value={key}>
                                    {config.label}
                                  </SelectItem>
                                ))}
                              </SelectContent>
                            </Select>
                          )}
                          displayComponent={(
                            <Badge variant={statusConfig[status].variant} className={statusConfig[status].className}>
                              {statusConfig[status].label}
                            </Badge>
                          )}
                        />
                      </ReviewItem>
                    </ReviewRow>
                    <ReviewRow>
                      <ReviewItem>
                        <ReviewLabel>
                          <UsersIcon className="text-primary size-4" />
                          队伍
                        </ReviewLabel>
                        <EditableField
                          isEditing={editingField === 'teams'}
                          onEdit={() => setEditingField('teams')}
                          className="mt-1"
                          cursorType="pointer"
                          editComponent={(
                            <div className="-mx-3 -my-2" data-team-multi-select>
                              <MultiSelect
                                options={teamOptions}
                                onValueChange={(teams) => {
                                  setSelectedTeams(teams)
                                }}
                                defaultValue={selectedTeams}
                                maxCount={10}
                                closeOnSelect={false}
                                onClose={() => {
                                  setEditingField(null)
                                  autoSave()
                                }}
                                onBlur={handleBlur}
                              />
                            </div>
                          )}
                          displayComponent={(
                            <div className="flex min-h-[32px] flex-wrap items-center gap-2">
                              {selectedTeams.length > 0 ? (
                                selectedTeams.map((teamName) => {
                                  const teamColors = getTeamColorClassByName(teamName)
                                  return (
                                    <Badge key={teamName} variant="outline" className={teamColors}>
                                      {teamName}
                                    </Badge>
                                  )
                                })
                              ) : (
                                <span className="text-muted-foreground"></span>
                              )}
                            </div>
                          )}
                        />
                      </ReviewItem>
                      <ReviewItem>
                        <ReviewLabel>
                          <LinkIcon className="text-primary size-4" />
                          网址
                        </ReviewLabel>
                        <EditableField
                          ref={socialUrlFieldRef}
                          isEditing={editingField === 'socialUrl'}
                          onEdit={() => setEditingField('socialUrl')}
                          className="mt-1"
                          editComponent={(
                            <Input
                              value={socialUrl}
                              onChange={e => setSocialUrl(DOMPurify.sanitize(e.target.value))}
                              onBlur={handleBlur}
                              onKeyDown={e => handleInputKeyDown(e, 'socialUrl')}
                              autoFocus
                              className="-mx-3 -my-2 h-8"
                            />
                          )}
                          displayComponent={(
                            <p className="min-h-[32px] leading-8">
                              {socialUrl ? (
                                <a
                                  href={socialUrl}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="text-primary hover:underline"
                                  onClick={e => e.stopPropagation()}
                                >
                                  {socialUrl}
                                </a>
                              ) : (
                                <span className="text-muted-foreground">{socialUrl}</span>
                              )}
                            </p>
                          )}
                        />
                      </ReviewItem>
                    </ReviewRow>
                  </CardContent>
                </Card>
                <ReviewTable
                  tableData={tableA}
                  tableName="A"
                  selectedTeams={selectedTeams}
                  editingField={editingField}
                  onEditField={setEditingField}
                  onUpdatePlayer={(playerIndex, value) => {
                    updatePlayer('A', playerIndex, value)
                  }}
                  onUpdateRound={(roundIndex, value) => {
                    updateRound('A', roundIndex, value)
                  }}
                  onUpdateResult={(roundIndex, playerIndex, value) => {
                    updateResult('A', roundIndex, playerIndex, value)
                  }}
                  onAddRow={() => addTableRow('A')}
                  onRemoveRow={roundIndex => removeTableRow('A', roundIndex)}
                  onBlur={handleBlur}
                />
                <ReviewTable
                  tableData={tableB}
                  tableName="B"
                  selectedTeams={selectedTeams}
                  editingField={editingField}
                  onEditField={setEditingField}
                  onUpdatePlayer={(playerIndex, value) => {
                    updatePlayer('B', playerIndex, value)
                  }}
                  onUpdateRound={(roundIndex, value) => {
                    updateRound('B', roundIndex, value)
                  }}
                  onUpdateResult={(roundIndex, playerIndex, value) => {
                    updateResult('B', roundIndex, playerIndex, value)
                  }}
                  onAddRow={() => addTableRow('B')}
                  onRemoveRow={roundIndex => removeTableRow('B', roundIndex)}
                  onBlur={handleBlur}
                />
                <Card className="hidden rounded-xs border-0">
                  <CardHeader>
                    <CardTitle>备注</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <EditableField
                      ref={contentFieldRef}
                      isEditing={editingField === 'content'}
                      onEdit={() => setEditingField('content')}
                      editComponent={(
                        <Textarea
                          value={content}
                          onChange={e => setContent(e.target.value)}
                          onBlur={handleBlur}
                          onKeyDown={e => handleInputKeyDown(e, 'content')}
                          autoFocus
                          className="-mx-3 -my-2 min-h-[200px] resize-y"
                        />
                      )}
                      displayComponent={(
                        <div className="prose min-h-[200px] max-w-none">
                          {content ? (
                            <pre className="text-foreground font-sans whitespace-pre-wrap">{content}</pre>
                          ) : (
                            <p className="text-muted-foreground italic"></p>
                          )}
                        </div>
                      )}
                    />
                  </CardContent>
                </Card>
              </div>
            </div>
          </div>
        </DialogContent>
      </Dialog>
      <AlertDialog open={deleteDialogOpen} onOpenChange={setDeleteDialogOpen}>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>确认删除</AlertDialogTitle>
            <AlertDialogDescription>确定要删除这个复盘吗？此操作无法撤销。</AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>取消</AlertDialogCancel>
            <AlertDialogAction variant="destructive" onClick={confirmDelete}>
              删除
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </>
  )
}
