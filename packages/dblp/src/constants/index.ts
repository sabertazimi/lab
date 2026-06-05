export const FILTER_VENUE = 'filter venue' as const
export const FILTER_YEAR = 'filter year' as const
export const REQUEST_DATA = 'request' as const
export const RECEIVE_DATA = 'receive' as const
export const REQUEST_ERROR = 'request error' as const

export type ActionType
  = | typeof FILTER_VENUE
    | typeof FILTER_YEAR
    | typeof REQUEST_DATA
    | typeof RECEIVE_DATA
    | typeof REQUEST_ERROR
