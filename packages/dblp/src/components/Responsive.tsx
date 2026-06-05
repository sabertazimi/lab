import { Component } from 'react'

// const onlyMobile = { minWidth: 320, maxWidth: 767 };
// const onlyTablet = { minWidth: 768, maxWidth: 991 };
// const onlyComputer = { minWidth: 992 };
// const onlyLargeScreen = { minWidth: 1200, maxWidth: 1919 };
// const onlyWidescreen = { minWidth: 1920 };

interface ResponsiveProps {
  maxWidth?: number
  minWidth?: number
  children: React.ReactNode
  getWidth?: () => number
  onUpdate?: (event?: Event, props?: ResponsiveProps & { width: number }) => void
}

interface ResponsiveState {
  visible: boolean
}

function fitsMaxWidth(width: number, maxWidth?: number): boolean {
  return !maxWidth || width <= maxWidth
}

function fitsMinWidth(width: number, minWidth?: number): boolean {
  return !minWidth || width >= minWidth
}

function isVisible(
  width: number,
  { maxWidth, minWidth }: Pick<ResponsiveProps, 'maxWidth' | 'minWidth'>,
): boolean {
  return fitsMinWidth(width, minWidth) && fitsMaxWidth(width, maxWidth)
}

export default class Responsive extends Component<ResponsiveProps, ResponsiveState> {
  private ticking = false
  private frameId = 0

  constructor(props: ResponsiveProps) {
    super(props)
    this.state = {
      visible: true,
    }
  }

  componentDidMount(): void {
    window.addEventListener('resize', this.handleResize)
    this.handleUpdate()
  }

  componentWillUnmount(): void {
    window.removeEventListener('resize', this.handleResize)
    cancelAnimationFrame(this.frameId)
  }

  getWidth = (): number => {
    const { getWidth: gw } = this.props

    if (gw)
      return gw()

    return window.innerWidth || 0
  }

  handleResize = (event: Event): void => {
    if (this.ticking)
      return

    this.ticking = true
    this.frameId = requestAnimationFrame(() => this.handleUpdate(event))
  }

  handleUpdate = (event?: Event): void => {
    this.ticking = false

    const { onUpdate } = this.props
    const { visible } = this.state
    const width = this.getWidth()
    const nextVisible = isVisible(width, this.props)

    if (visible !== nextVisible)
      this.setState({ visible: nextVisible })

    if (onUpdate)
      onUpdate(event, { ...this.props, width })
  }

  render(): React.ReactNode {
    const { children } = this.props
    const { visible } = this.state

    if (visible)
      return <>{children}</>

    return null
  }
}
