import type { Dispatch } from 'redux'
import type { Action } from '../actions'
import { Input } from 'antd'
import { connect } from 'react-redux'
import * as Actions from '../actions'

const { Search } = Input

interface SearchBarComponentProps {
  fetchData: (keyword: string) => void
  style?: React.CSSProperties
}

function SearchBarComponent({ fetchData, style }: SearchBarComponentProps) {
  const onSearch = (value: string) => value && fetchData(value)

  return (
    <Search
      allowClear
      style={style}
      enterButton
      placeholder="Search paper here ..."
      onSearch={onSearch}
    />
  )
}

function mapDispatchToProps(dispatch: Dispatch<Action>) {
  return {
    fetchData: (keyword: string) => dispatch(Actions.fetchData(keyword) as unknown as Action),
  }
}

const SearchBar = connect(null, mapDispatchToProps)(SearchBarComponent)
export default SearchBar
