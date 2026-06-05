import { readFile, writeFile } from 'node:fs/promises'
import { resolve } from 'node:path'
import config from './config.ts'

interface GameItem {
  id: string
  time: string
  cmd: Command
  args: string[]
}

type Command
  = | 'area'
    | 'player'
    | 'point'
    | 'gamestart'
    | 'gameend'
    | 'kyokustart'
    | 'haipai'
    | 'kyokuend'
    | 'ryukyoku'
    | 'dice'
    | 'dora'
    | 'uradora'
    | 'tsumo'
    | 'sutehai'
    | 'say'
    | 'richi'
    | 'open'
    | 'agari'

async function readGame(game: string) {
  return readFile(resolve(config.dataPath, game)).then((buffer) => {
    return JSON.parse(buffer.toString()) as GameItem[]
  })
}

async function writeGame(game: string, umdGame: GameItem[]) {
  return writeFile(resolve(config.dataPath, game), JSON.stringify(umdGame))
}

// These may be caused by the wrong hand input, correct these after fetching data
readGame('L001_S007_0010_02A.json')
  .then(async (game) => {
    // B0: 0.4 -> -0.4
    game[game.length - 1].args[3] = '-0.4'
    return writeGame('L001_S007_0010_02A.json', game)
  })
  .catch((error) => {
    console.error(error)
  })

readGame('L001_S010_0015_02A.json')
  .then(async (game) => {
    // A0: 58.0 -> 38.0
    // C0: 18.0 -> 38.0
    game[game.length - 1].args[1] = '38.0'
    game[game.length - 1].args[3] = '38.0'
    return writeGame('L001_S010_0015_02A.json', game)
  })
  .catch((error) => {
    console.error(error)
  })

readGame('L001_S010_0080_02A.json')
  .then(async (game) => {
    // B0: -42.8 -> -72.8
    // D0: 26.4 -> 76.4
    game[game.length - 1].args[1] = '76.4'
    game[game.length - 1].args[7] = '-72.8'
    return writeGame('L001_S010_0080_02A.json', game)
  })
  .catch((error) => {
    console.error(error)
  })
