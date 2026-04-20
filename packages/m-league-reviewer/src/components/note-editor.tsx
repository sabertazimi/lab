import type { Note } from '@/api/data'
import { Placeholder } from '@tiptap/extensions'
import { EditorContent, useEditor, useEditorState } from '@tiptap/react'
import { BubbleMenu } from '@tiptap/react/menus'
import StarterKit from '@tiptap/starter-kit'
import { useEffect, useState } from 'react'
import { toast } from 'sonner'
import { NoteEditorToolbar } from '@/components/note-editor-toolbar'
import { cn } from '@/lib/utils'
import { useNotesStore } from '@/stores/notes'

export function NoteEditor({ open }: { open: boolean }) {
  const notes = useNotesStore(state => state.notes)
  const createNote = useNotesStore(state => state.createNote)
  const updateNote = useNotesStore(state => state.updateNote)
  const [note, setNote] = useState<Note | null>(null)
  const editor = useEditor({
    extensions: [
      StarterKit,
      Placeholder.configure({
        emptyNodeClass:
          'before:content-[attr(data-placeholder)] before:float-left before:text-muted-foreground before:h-0 before:pointer-events-none',
        placeholder: '写点什么...',
        includeChildren: true,
      }),
    ],
    editorProps: {
      attributes: {
        class: cn(
          'prose prose-sm sm:prose dark:prose-invert',
          'mx-auto min-h-full max-w-screen p-8 focus:outline-none sm:max-w-prose',
          'prose-headings:text-primary prose-headings:font-semibold prose-headings:text-balance prose-headings:scroll-mt-20 prose-headings:relative',
          'prose-headings:before:absolute prose-headings:before:right-full prose-headings:before:text-primary/40',
          'prose-headings:before:content-["#"] prose-headings:before:opacity-0 prose-headings:hover:before:opacity-100 prose-headings:before:transition-opacity',
          'prose-a:text-primary prose-strong:text-primary',
          'prose-inline-code:before:content-none prose-inline-code:after:content-none',
          'prose-inline-code:border prose-inline-code:border-border prose-inline-code:bg-muted',
          'prose-inline-code:px-1.5 prose-inline-code:py-0.5 prose-inline-code:mx-1',
          'prose-inline-code:font-semibold prose-inline-code:text-foreground prose-inline-code:font-mono',
        ),
      },
      handleKeyDown: (_view, event) => {
        if ((event.ctrlKey || event.metaKey) && event.key === 's') {
          event.preventDefault()

          if (note && editor) {
            const json = editor.getJSON()
            updateNote(note.id, json)
            toast.success('笔记已保存')
          }

          return true
        }

        return false
      },
    },
    content: { type: 'doc', content: [] },
    onUpdate: ({ editor }) => {
      if (note) {
        const json = editor.getJSON()
        updateNote(note.id, json)
      }
    },
  })
  const editorState = useEditorState({
    editor,
    selector: ({ editor }) => ({
      isBold: editor.isActive('bold') ?? false,
      canBold: editor.can().chain().toggleBold().run() ?? false,
      isItalic: editor.isActive('italic') ?? false,
      canItalic: editor.can().chain().toggleItalic().run() ?? false,
      isUnderline: editor.isActive('underline') ?? false,
      canUnderline: editor.can().chain().toggleUnderline().run() ?? false,
      isStrikethrough: editor.isActive('strike') ?? false,
      canStrikethrough: editor.can().chain().toggleStrike().run() ?? false,
      isCode: editor.isActive('code') ?? false,
      canCode: editor.can().chain().toggleCode().run() ?? false,
      canClearMarks: editor.can().chain().unsetAllMarks().run() ?? false,
      isParagraph: editor.isActive('paragraph') ?? false,
      isHeading1: editor.isActive('heading', { level: 1 }) ?? false,
      isHeading2: editor.isActive('heading', { level: 2 }) ?? false,
      isHeading3: editor.isActive('heading', { level: 3 }) ?? false,
      isHeading4: editor.isActive('heading', { level: 4 }) ?? false,
      isHeading5: editor.isActive('heading', { level: 5 }) ?? false,
      isHeading6: editor.isActive('heading', { level: 6 }) ?? false,
      isOrderedList: editor.isActive('orderedList') ?? false,
      isBulletList: editor.isActive('bulletList') ?? false,
      isCodeBlock: editor.isActive('codeBlock') ?? false,
      isBlockquote: editor.isActive('blockquote') ?? false,
      canUndo: editor.can().chain().undo().run() ?? false,
      canRedo: editor.can().chain().redo().run() ?? false,
    }),
  })

  useEffect(() => {
    if (open && editor) {
      let currentNote: Note

      if (notes.length === 0) {
        currentNote = createNote()
      } else {
        currentNote = notes[0]
      }

      setNote(currentNote)
      editor.commands.setContent(currentNote.content)
    }
    // eslint-disable-next-line react/exhaustive-deps -- only need to run when open changes
  }, [open, editor])

  if (!editor) {
    return null
  }

  return (
    <>
      <NoteEditorToolbar editor={editor} editorState={editorState} />
      <EditorContent editor={editor} className="flex-1 overflow-auto" />
      <BubbleMenu editor={editor} options={{ placement: 'top', offset: 8, flip: true }} className="hidden lg:block">
        <NoteEditorToolbar editor={editor} editorState={editorState} />
      </BubbleMenu>
    </>
  )
}
