import type { GameSchedule } from './get-game-schedule.ts'
import { writeFile } from 'node:fs'
import path from 'node:path'
import process from 'node:process'
import { parse } from 'node-html-parser'
import config from './config.ts'
import getGameSchedule from './get-game-schedule.ts'
import { req, sleep } from './utils.ts'

/**
 * Extract year from season string
 * @param season - Season string like 'games/2024-season' or 'games'
 * @returns Start year of the season
 */
function getSeasonStartYear(season: string): number {
  // Try to extract year from season string (e.g., 'games/2024-season' -> 2024)
  const yearMatch = season.match(/(\d{4})/)
  if (yearMatch) {
    return Number.parseInt(yearMatch[1], 10)
  }

  // If no year found (e.g., 'games'), use current date to determine season year
  const now = new Date()
  const currentYear = now.getFullYear()
  const currentMonth = now.getMonth() + 1 // getMonth() returns 0-11

  // M.League season starts in September
  // If current month is 1-8, we're in the second half of the season (use previous year)
  // If current month is 9-12, we're in the first half of the season (use current year)
  return currentMonth >= 9 ? currentYear : currentYear - 1
}

/**
 * Generate month parameters for fetching game schedules
 * M.League season runs from September to May of the following year
 * @param season - Season string to determine the year range
 */
function generateMonthParams(season: string): Array<{ mly: number, mlm: number }> {
  const params: Array<{ mly: number, mlm: number }> = []
  const startYear = getSeasonStartYear(season)
  const endYear = startYear + 1

  // First year: September to December (9-12)
  for (let month = 9; month <= 12; month++) {
    params.push({ mly: startYear, mlm: month })
  }

  // Second year: January to May (1-5)
  for (let month = 1; month <= 5; month++) {
    params.push({ mly: endYear, mlm: month })
  }

  return params
}

/**
 * Fetch game schedules for the current season
 */
async function fetchGameSchedule() {
  // Get the last season from seasonList
  const currentSeason = config.seasonList[config.seasonList.length - 1]
  const startYear = getSeasonStartYear(currentSeason)
  console.log(`Fetching game schedule for season: ${currentSeason} (${startYear}-${startYear + 1})`)

  const allSchedules: GameSchedule[] = []
  const monthParams = generateMonthParams(currentSeason)

  for (const { mly, mlm } of monthParams) {
    try {
      console.log(`Fetching schedule for ${mly}-${mlm.toString().padStart(2, '0')}...`)

      const url = `${config.baseUrl}/${currentSeason}/?mly=${mly}&mlm=${mlm}`
      const response = await req.get<string>(url)

      const seasonPage = parse(response.data)
      const schedules = getGameSchedule(seasonPage, mly)

      if (schedules.length > 0) {
        allSchedules.push(...schedules)
        console.log(`  Found ${schedules.length} game(s) in ${mly}-${mlm.toString().padStart(2, '0')}`)
      } else {
        console.log(`  No games found in ${mly}-${mlm.toString().padStart(2, '0')}`)
      }

      // Wait before next request
      await sleep()
    } catch (error) {
      console.error(`Error fetching schedule for ${mly}-${mlm.toString().padStart(2, '0')}:`, error)
    }
  }

  // Save all schedules to a JSON file
  const outputPath = path.resolve('./data', 'game-schedule.json')
  writeFile(outputPath, JSON.stringify(allSchedules, null, 2), { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error('Error writing game schedule file:', err)
    } else {
      console.log(`\nGame schedule saved to ${outputPath}`)
      console.log(`Total games: ${allSchedules.length}`)
    }
  })
}

// Run the fetch
fetchGameSchedule().catch((error) => {
  console.error('Fatal error:', error)
  process.exit(1)
})
