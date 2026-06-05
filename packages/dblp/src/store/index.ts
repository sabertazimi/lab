import type { RootState } from '../reducers'
import { applyMiddleware, compose, createStore } from 'redux'
import { thunk as thunkMiddleware } from 'redux-thunk'
import createRootReducer from '../reducers'

const middleware = [thunkMiddleware]

function configureStore(preloadedState?: RootState) {
  const store = createStore(
    createRootReducer(),
    preloadedState,
    compose(applyMiddleware(...middleware)),
  )

  return store
}

export default configureStore
export type { RootState }
