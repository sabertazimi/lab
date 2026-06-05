import type { RootState } from '../store'
import { Button, Modal } from 'antd'
import { Component } from 'react'
import { connect } from 'react-redux'
import { StatisticsModal } from '../components'

interface StatisticsBarComponentProps {
  error: Error | null
  isLoading: boolean
  items: RootState['data']['items']
  venues: string[]
  year: number
}

interface StatisticsBarComponentState {
  loading: boolean
  visible: boolean
}

class StatisticsBarComponent extends Component<StatisticsBarComponentProps, StatisticsBarComponentState> {
  constructor(props: StatisticsBarComponentProps) {
    super(props)
    this.state = {
      loading: false,
      visible: false,
    }
  }

  showStatistics = (): void => {
    this.setState({
      visible: true,
    })
  }

  handleExport = (): void => {
    this.setState({ loading: true })

    setTimeout(() => {
      this.setState({ loading: false, visible: false })
    }, 3000)
  }

  handleClose = (): void => {
    this.setState({
      visible: false,
    })
  }

  render(): React.ReactNode {
    const { visible, loading } = this.state

    return (
      <div>
        <Button type="primary" onClick={this.showStatistics}>
          Open Statistics Bar
        </Button>
        <Modal
          open={visible}
          title="Statistics"
          onOk={this.handleExport}
          onCancel={this.handleClose}
          footer={[
            <Button key="back" onClick={this.handleClose}>
              Close
            </Button>,
            <Button
              key="export"
              type="primary"
              loading={loading}
              onClick={this.handleExport}
            >
              Export
            </Button>,
          ]}
        >
          <StatisticsModal {...this.props} />
        </Modal>
      </div>
    )
  }
}

function mapStateToProps(state: RootState) {
  return {
    ...state.data,
    ...state.filter,
  }
}

const StatisticsBar = connect(mapStateToProps)(StatisticsBarComponent)
export default StatisticsBar
