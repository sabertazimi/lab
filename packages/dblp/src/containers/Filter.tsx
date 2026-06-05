import type { Dispatch } from 'redux'
import type { Action } from '../actions'
import type { RootState } from '../store'
import { ClockCircleOutlined, EllipsisOutlined } from '@ant-design/icons'
import { Menu } from 'antd'
import { Component } from 'react'
import { connect } from 'react-redux'
import * as Actions from '../actions'
import { VENUES_LIST } from '../api'
import { VenuesFilter, YearFilter } from '../components'

interface FilterComponentProps {
  year: number
  venues: string[]
  collapsed: boolean
  filterVenue: (venues: string[]) => void
  filterYear: (year: number) => void
}

interface FilterComponentState {
  indeterminate: boolean
  checkAll: boolean
}

class FilterComponent extends Component<FilterComponentProps, FilterComponentState> {
  constructor(props: FilterComponentProps) {
    super(props)
    this.state = {
      indeterminate: true,
      checkAll: false,
    }
  }

  onYearChange = (value: number | null): void => {
    const { filterYear } = this.props
    if (value !== null)
      filterYear(value)
  }

  onVenuesChange = (checkedValues: string[]): void => {
    const { filterVenue } = this.props
    filterVenue(checkedValues)

    this.setState({
      indeterminate:
        !!checkedValues.length && checkedValues.length < VENUES_LIST.length,
      checkAll: checkedValues.length === VENUES_LIST.length,
    })
  }

  onCheckAllChange = (event: { target: { checked: boolean } }): void => {
    const { filterVenue } = this.props
    filterVenue(event.target.checked ? VENUES_LIST : [])

    this.setState({
      indeterminate: false,
      checkAll: event.target.checked,
    })
  }

  render(): React.ReactNode {
    const { year, venues, collapsed } = this.props
    const { indeterminate, checkAll } = this.state

    if (collapsed) {
      return (
        <Menu mode="inline">
          <Menu.Item key="1">
            <ClockCircleOutlined />
            <span>Year</span>
          </Menu.Item>
          {[...Array.from({ length: 9 }).keys()].map(number => (
            <Menu.Item key={number + 2}>
              <EllipsisOutlined />
              <span>{`Venue ${number + 1}`}</span>
            </Menu.Item>
          ))}
          <Menu.Item key="11">
            <EllipsisOutlined />
            <span>Venue 10</span>
          </Menu.Item>
        </Menu>
      )
    }

    return (
      <div
        style={{
          paddingLeft: '1em',
          paddingBottom: '1em',
        }}
      >
        <YearFilter year={year} onYearChange={this.onYearChange} />
        <VenuesFilter
          venues={venues}
          indeterminate={indeterminate}
          checkAll={checkAll}
          onVenuesChange={this.onVenuesChange}
          onCheckAllChange={this.onCheckAllChange}
        />
      </div>
    )
  }
}

function mapStateToProps(state: RootState) {
  return {
    ...state.filter,
  }
}

function mapDispatchToProps(dispatch: Dispatch<Action>) {
  return {
    filterVenue: (venues: string[]) => dispatch(Actions.filterVenue(venues)),
    filterYear: (year: number) => dispatch(Actions.filterYear(year)),
  }
}

const Filter = connect(mapStateToProps, mapDispatchToProps)(FilterComponent)
export default Filter
