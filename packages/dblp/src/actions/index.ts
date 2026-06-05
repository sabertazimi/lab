import type { Dispatch } from 'redux'
import type { Paper } from '../api'
import { fetchDblpPapers, fetchPaperCitations } from '../api'
import * as ActionTypes from '../constants'

interface FilterVenueAction {
  type: typeof ActionTypes.FILTER_VENUE
  payload: { venues: string[] }
}

interface FilterYearAction {
  type: typeof ActionTypes.FILTER_YEAR
  payload: { year: number }
}

interface RequestDataAction {
  type: typeof ActionTypes.REQUEST_DATA
  payload: { query: string[] }
}

interface ReceiveDataAction {
  type: typeof ActionTypes.RECEIVE_DATA
  payload: { items: Paper[] }
}

interface RequestErrorAction {
  type: typeof ActionTypes.REQUEST_ERROR
  payload: { error: Error }
}

export type Action
  = | FilterVenueAction
    | FilterYearAction
    | RequestDataAction
    | ReceiveDataAction
    | RequestErrorAction

export function filterVenue(venues: string[]): FilterVenueAction {
  return {
    type: ActionTypes.FILTER_VENUE,
    payload: { venues },
  }
}

export function filterYear(year: number): FilterYearAction {
  return {
    type: ActionTypes.FILTER_YEAR,
    payload: { year },
  }
}

function requestData(query: string[]): RequestDataAction {
  return {
    type: ActionTypes.REQUEST_DATA,
    payload: { query },
  }
}

function receiveData(items: Paper[]): ReceiveDataAction {
  return {
    type: ActionTypes.RECEIVE_DATA,
    payload: { items },
  }
}

function requestErrorAction(error: Error): RequestErrorAction {
  return {
    type: ActionTypes.REQUEST_ERROR,
    payload: { error },
  }
}

interface FilterState {
  venues: string[]
  year: number
}

export function fetchData(keyword: string) {
  return async (dispatch: Dispatch<Action>, getState: () => { filter: FilterState }) => {
    const venues = getState().filter.venues

    dispatch(requestData(venues))

    const papers = await fetchDblpPapers(keyword, venues)
    if (!papers) {
      dispatch(requestErrorAction(new Error('Bad Request')))
      return
    }

    const paperCitations = await fetchPaperCitations(papers)

    const papersDataWithCitations = papers.map((paper, index) => ({
      ...paper,
      citations: paperCitations[index],
    }))

    setTimeout(() => {
      dispatch(receiveData(papersDataWithCitations))
    }, 255)
  }
}
