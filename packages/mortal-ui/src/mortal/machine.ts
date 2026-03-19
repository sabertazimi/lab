import type { Event, Log, ReviewLog } from './data'
import { UIState } from './state'
import { TileUtils } from './utils'

class Machine {
  gameLog: Event[] = []
  reviewLog: ReviewLog
  state: UIState[][] = []
  uiState: UIState
  round: number = -1
  turn: number = 0
  rounds: number = 0
  turns: number[] = []
  heroId: number = 0
  isHereReached: boolean = false
  reviewCounter: number = 0

  constructor(log: Log) {
    this.gameLog = log.mjai_log
    this.reviewLog = log.review
    this.heroId = log.player_id
    this.uiState = new UIState()
  }

  run() {
    for (const [index, event] of this.gameLog.entries()) {
      switch (event.type) {
        case 'start_game':
          this.round = -1
          this.rounds = 0
          this.turns = []
          this.state = []
          break
        case 'start_kyoku':
          this.round += 1
          this.reviewCounter = 0
          event.heroId = this.heroId // Registry heroId to event.
          this.uiState = new UIState(event)
          this.recordState(true)
          break
        case 'tsumo': {
          const { actor } = event
          const position = TileUtils.getRelativePosition(this.heroId, actor)
          const pai = TileUtils.get(event.pai)
          const hand = this.uiState.hands.at(position)

          if (hand) {
            hand.tsumo = pai
          }

          if (actor === this.heroId)
            this.advanceReview(actor)

          this.recordState()
          break
        }
        case 'dahai': {
          const { actor, tsumogiri } = event
          const position = TileUtils.getRelativePosition(this.heroId, actor)
          const pai = TileUtils.get(event.pai)
          const hand = this.uiState.hands.at(position)
          const discard = this.uiState.discards.at(position)

          if (hand) {
            const { tehai, tsumo } = hand

            if (tsumo) {
              tehai.push(tsumo)
            }

            const discardIndex = tehai.findIndex(t => t === pai)
            hand.tehai = tehai
              .slice(0, discardIndex)
              .concat(tehai.slice(discardIndex + 1))
            TileUtils.sort(hand.tehai)
            hand.tsumo = ''
          }

          if (discard) {
            discard.tiles.push({
              type:
                this.gameLog[index - 1]?.type === 'reach' ? 'riichi' : 'normal',
              pai,
              tsumogiri,
              claimed: false,
            })
          }

          if (actor !== this.heroId)
            this.advanceReview(actor)

          this.recordState()
          break
        }
        case 'chi':
        case 'pon':
        case 'daiminkan': {
          const { actor, consumed, target } = event
          const position = TileUtils.getRelativePosition(this.heroId, actor)
          const targetPosition = TileUtils.getRelativePosition(
            this.heroId,
            target,
          )
          const hand = this.uiState.hands.at(position)
          const targetDiscard = this.uiState.discards.at(targetPosition)

          if (hand) {
            const consumedTiles = TileUtils.consume(hand.tehai, consumed)
            hand.tehai = consumedTiles
            hand.claimed.push(event)
          }

          if (targetDiscard) {
            const targetDiscardTile = targetDiscard.tiles.pop()
            if (targetDiscardTile) {
              targetDiscard.tiles.push({
                ...targetDiscardTile,
                tsumogiri: false,
                claimed: true,
              })
            }
          }

          if (actor === this.heroId)
            this.advanceReview(actor)

          this.recordState()
          break
        }
        case 'kakan': {
          const { actor } = event
          const position = TileUtils.getRelativePosition(this.heroId, actor)
          const hand = this.uiState.hands.at(position)

          if (hand) {
            const ponClaimed = hand.claimed.find(
              c => c.type === 'pon' && c.pai === event.pai,
            )

            if (ponClaimed?.type === 'pon') {
              const { target } = ponClaimed
              event.target = target // Register target to event.
              hand.claimed = hand.claimed.filter(c => c !== ponClaimed)
              hand.claimed.push(event)
            }
          }

          this.recordState()
          break
        }
        case 'ankan': {
          const { actor, consumed } = event
          const position = TileUtils.getRelativePosition(this.heroId, actor)
          const hand = this.uiState.hands.at(position)

          if (hand) {
            if (hand.tsumo) {
              hand.tehai.push(hand.tsumo)
            }

            const consumedTiles = TileUtils.consume(hand.tehai, consumed)
            hand.tehai = consumedTiles
            event.pai = consumed[0] // Register ankan tile to event.
            hand.claimed.push(event)
          }

          this.recordState()
          break
        }
        case 'dora': {
          const { dora_marker } = event
          const { doraMarkers } = this.uiState.info

          doraMarkers.push(TileUtils.get(dora_marker))

          this.recordState()
          break
        }
        case 'reach':
          break
        case 'reach_accepted':
          if (event.actor === this.heroId)
            this.isHereReached = true
          break
        case 'hora':
        case 'ryukyoku': {
          const { deltas } = event
          const { deltasQueue } = this.uiState.info
          const normalizedDeltas: number[] = []

          for (let i = 0; i < 4; i++) {
            normalizedDeltas[i] = deltas[(i + this.heroId) % 4] ?? 0
          }

          // Queue for double or triple ron.
          deltasQueue.push(normalizedDeltas)

          // Prevent duplicate uraMarkers from double or triple ron.
          if (event.type === 'hora') {
            this.uiState.info.uraMarkers = event.ura_markers.map(marker =>
              TileUtils.get(marker),
            )
          }

          break
        }
        case 'end_kyoku':
          this.uiState.info.endOfKyoku = true
          this.turns.push(this.state?.[this.round]?.length ?? 0 + 1)
          this.recordState()
          break
        case 'end_game':
          this.rounds = this.round + 1
          break
        case 'none':
          break
        default:
          break
      }
    }
  }

  recordState(newRound: boolean = false) {
    if (newRound) {
      this.state.push([JSON.parse(JSON.stringify(this.uiState))] as UIState[])
    } else {
      this.state?.[this.round]?.push(
        JSON.parse(JSON.stringify(this.uiState)) as UIState,
      )
    }

    // Reset mortal review after current state is recorded.
    this.uiState.mortalReview = {
      show: false,
      tehaiProb: {},
      tehaiActual: {},
      tehaiExpected: {},
      tsumoProb: 0,
      tsumoActual: false,
      tsumoExpected: false,
      isEqual: true,
      claimAdvice: [],
      claimActual: -1,
      claimExpected: -1,
    }
  }

  advanceReview(actor: number) {
    const kyoku = this.reviewLog.kyokus.at(this.round)

    if (!kyoku) {
      return
    }

    const { entries } = kyoku

    // TODO: Remove reviewCounter check after all logs are fixed.
    if (this.reviewCounter < entries.length) {
      const review = entries.at(this.reviewCounter)

      if (!review) {
        return
      }

      const { last_actor, details, is_equal, actual, expected } = review

      switch (actor) {
        case this.heroId: {
          const { tsumo } = this.uiState.hands[0] ?? {}
          const tehaiProb: { [key: string]: number } = {}
          const tehaiActual: { [key: string]: boolean } = {}
          const tehaiExpected: { [key: string]: boolean } = {}
          let tsumoProb = 0
          let tsumoActual = false
          let tsumoExpected = false

          const tsumoIndex = details.findIndex(
            ({ action }) =>
              action.type === 'dahai'
              && action.tsumogiri === true
              && TileUtils.get(action.pai) === tsumo,
          )

          // Dahai review for hero after tsumo or claim.
          if (tsumoIndex !== -1) {
            // Tsumo.
            details
              .slice(0, tsumoIndex)
              .concat(details.slice(tsumoIndex + 1))
              .forEach(({ action, prob }) => {
                if (action.type === 'dahai')
                  tehaiProb[TileUtils.get(action.pai)] = prob
              })
            tsumoProb = details[tsumoIndex]?.prob ?? 0
          } else {
            // Claim.
            details.forEach(({ action, prob }) => {
              if (action.type === 'dahai')
                tehaiProb[TileUtils.get(action.pai)] = prob
            })
            tsumoProb = 0
          }

          const actualPai
            = actual.type === 'dahai' && !actual.tsumogiri
              ? TileUtils.get(actual.pai)
              : ''
          const expectedPai
            = expected.type === 'dahai' && !expected.tsumogiri
              ? TileUtils.get(expected.pai)
              : ''
          tehaiActual[actualPai] = true
          tehaiExpected[expectedPai] = true
          tsumoActual = actual.type === 'dahai' && actual.tsumogiri
          tsumoExpected = expected.type === 'dahai' && expected.tsumogiri

          this.uiState.mortalReview = {
            show: true,
            tehaiProb,
            tehaiActual,
            tehaiExpected,
            tsumoActual,
            tsumoExpected,
            tsumoProb,
            isEqual: is_equal,
            claimAdvice: [],
            claimActual: -1,
            claimExpected: -1,
          }
          this.reviewCounter += 1

          break
        }
        case last_actor: {
          // TODO: compare consumed tiles for chi, pon, daiminkan, and kakan.
          const claimActual = details.findIndex(
            ({ action }) => action.type === actual.type,
          )
          // TODO: compare consumed tiles for chi, pon, daiminkan, and kakan.
          const claimExpected = details.findIndex(
            ({ action }) => action.type === expected.type,
          )

          this.uiState.mortalReview = {
            show: true,
            tehaiProb: {},
            tehaiActual: {},
            tehaiExpected: {},
            tsumoProb: 0,
            tsumoActual: false,
            tsumoExpected: false,
            isEqual: is_equal,
            claimAdvice: details,
            claimActual,
            claimExpected,
          }
          this.reviewCounter += 1
          break
        }
        default:
          break
      }
    }
  }
}

function createMachine(log: Log) {
  const machine = new Machine(log)
  return machine
}

export { createMachine }
