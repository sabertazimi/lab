import type { Reducer as ReduxReducer } from 'redux'
import type { Action } from '../actions'
import type { Paper } from '../api'
import { combineReducers } from 'redux'
import { DEFAULT_VENUES_LIST } from '../api'
import * as ActionTypes from '../constants'

export interface FilterState {
  venues: string[]
  year: number
}

export interface DataState {
  error: Error | null
  isLoading: boolean
  items: Paper[]
}

export interface RootState {
  filter: FilterState
  data: DataState
}

type Reducer<S> = (state: S | undefined, action: Action) => S

function createReducer<S>(initialState: S, handlers: Record<string, (state: S, action: Action) => S>): Reducer<S> {
  return (state = initialState, action) => {
    if (Object.hasOwn(handlers, action.type))
      return handlers[action.type](state, action)

    return state
  }
}

const filterReducer = createReducer<FilterState>(
  {
    venues: DEFAULT_VENUES_LIST,
    year: new Date().getFullYear() - 2,
  },
  {
    [ActionTypes.FILTER_VENUE]: (state, action) => {
      const { venues } = action.payload as { venues: string[] }

      return {
        ...state,
        venues,
      }
    },
    [ActionTypes.FILTER_YEAR]: (state, action) => {
      const { year } = action.payload as { year: number }

      return {
        ...state,
        year,
      }
    },
  },
)

const dataReducer = createReducer<DataState>(
  {
    error: null,
    isLoading: false,
    items: [],
  },
  {
    [ActionTypes.REQUEST_DATA]: state => ({
      ...state,
      error: null,
      isLoading: true,
      items: [],
    }),
    [ActionTypes.RECEIVE_DATA]: (state, action) => {
      const { items } = action.payload as { items: Paper[] }

      return {
        ...state,
        error: null,
        isLoading: false,
        items,
      }
    },
    [ActionTypes.REQUEST_ERROR]: (state, action) => {
      const { error } = action.payload as { error: Error }

      return {
        ...state,
        error,
        items: [],
      }
    },
  },
)

function createRootReducer(): ReduxReducer<RootState, Action> {
  const rootReducer = combineReducers({
    filter: filterReducer,
    data: dataReducer,
  })
  return rootReducer as unknown as ReduxReducer<RootState, Action>
}

export default createRootReducer
