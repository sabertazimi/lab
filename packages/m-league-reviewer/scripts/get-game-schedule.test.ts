import { parse } from 'node-html-parser'
import { describe, expect, it } from 'vitest'
import getGameSchedule from './get-game-schedule.ts'

describe('getGameSchedule', () => {
  it('should extract game schedules from HTML correctly', () => {
    const html = `
      <ul class="p-gamesSchedule2__lists">
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>1<span class="p-gamesSchedule2__dayWeek">（月）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="KADOKAWAサクラナイツ"></li>
            <li><img src="test.png" alt="渋谷ABEMAS"></li>
            <li><img src="test.png" alt="セガサミーフェニックス"></li>
            <li><img src="test.png" alt="TEAM RAIDEN / 雷電"></li>
          </ul>
        </li>
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>2<span class="p-gamesSchedule2__dayWeek">（火）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EARTH JETS"></li>
            <li><img src="test.png" alt="KONAMI麻雀格闘倶楽部"></li>
            <li><img src="test.png" alt="BEAST X"></li>
            <li><img src="test.png" alt="U-NEXT Pirates"></li>
          </ul>
        </li>
      </ul>
    `

    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    expect(schedules).toHaveLength(2)

    // First game (Monday)
    expect(schedules[0].date).toBe('2025-12-01')
    expect(schedules[0].dayOfWeek).toBe('月')
    expect(schedules[0].teamIds).toEqual([4, 6, 7, 8]) // Sorted by ID

    // Second game (Tuesday)
    expect(schedules[1].date).toBe('2025-12-02')
    expect(schedules[1].dayOfWeek).toBe('火')
    expect(schedules[1].teamIds).toEqual([1, 5, 9, 10]) // Sorted by ID
  })

  it('should merge Thursday games into one record with 8 teams', () => {
    const html = `
      <ul class="p-gamesSchedule2__lists">
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>4<span class="p-gamesSchedule2__dayWeek">（木）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EARTH JETS"></li>
            <li><img src="test.png" alt="EX風林火山"></li>
            <li><img src="test.png" alt="KADOKAWAサクラナイツ"></li>
            <li><img src="test.png" alt="TEAM RAIDEN / 雷電"></li>
          </ul>
        </li>
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>4<span class="p-gamesSchedule2__dayWeek">（木）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="赤坂ドリブンズ"></li>
            <li><img src="test.png" alt="KONAMI麻雀格闘倶楽部"></li>
            <li><img src="test.png" alt="渋谷ABEMAS"></li>
            <li><img src="test.png" alt="セガサミーフェニックス"></li>
          </ul>
        </li>
      </ul>
    `

    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    // Should be merged into one record
    expect(schedules).toHaveLength(1)

    // Thursday with 8 teams
    expect(schedules[0].date).toBe('2025-12-04')
    expect(schedules[0].dayOfWeek).toBe('木')
    expect(schedules[0].teamIds).toEqual([1, 2, 3, 4, 5, 6, 7, 8])
    expect(schedules[0].teamIds).toHaveLength(8)
  })

  it('should merge Friday games into one record with 8 teams', () => {
    const html = `
      <ul class="p-gamesSchedule2__lists">
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>5<span class="p-gamesSchedule2__dayWeek">（金）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EX風林火山"></li>
            <li><img src="test.png" alt="渋谷ABEMAS"></li>
            <li><img src="test.png" alt="TEAM RAIDEN / 雷電"></li>
            <li><img src="test.png" alt="U-NEXT Pirates"></li>
          </ul>
        </li>
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>5<span class="p-gamesSchedule2__dayWeek">（金）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="赤坂ドリブンズ"></li>
            <li><img src="test.png" alt="KADOKAWAサクラナイツ"></li>
            <li><img src="test.png" alt="セガサミーフェニックス"></li>
            <li><img src="test.png" alt="BEAST X"></li>
          </ul>
        </li>
      </ul>
    `

    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    // Should be merged into one record
    expect(schedules).toHaveLength(1)

    // Friday with 8 teams
    expect(schedules[0].date).toBe('2025-12-05')
    expect(schedules[0].dayOfWeek).toBe('金')
    expect(schedules[0].teamIds).toEqual([2, 3, 4, 6, 7, 8, 9, 10])
    expect(schedules[0].teamIds).toHaveLength(8)
  })

  it('should handle complete schedule with all days (4 unique days)', () => {
    const html = `
      <ul class="p-gamesSchedule2__lists">
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>1<span class="p-gamesSchedule2__dayWeek">（月）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="KADOKAWAサクラナイツ"></li>
            <li><img src="test.png" alt="渋谷ABEMAS"></li>
            <li><img src="test.png" alt="セガサミーフェニックス"></li>
            <li><img src="test.png" alt="TEAM RAIDEN / 雷電"></li>
          </ul>
        </li>
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>2<span class="p-gamesSchedule2__dayWeek">（火）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EARTH JETS"></li>
            <li><img src="test.png" alt="KONAMI麻雀格闘倶楽部"></li>
            <li><img src="test.png" alt="BEAST X"></li>
            <li><img src="test.png" alt="U-NEXT Pirates"></li>
          </ul>
        </li>
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>4<span class="p-gamesSchedule2__dayWeek">（木）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EARTH JETS"></li>
            <li><img src="test.png" alt="EX風林火山"></li>
            <li><img src="test.png" alt="KADOKAWAサクラナイツ"></li>
            <li><img src="test.png" alt="TEAM RAIDEN / 雷電"></li>
          </ul>
        </li>
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>4<span class="p-gamesSchedule2__dayWeek">（木）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="赤坂ドリブンズ"></li>
            <li><img src="test.png" alt="KONAMI麻雀格闘倶楽部"></li>
            <li><img src="test.png" alt="渋谷ABEMAS"></li>
            <li><img src="test.png" alt="セガサミーフェニックス"></li>
          </ul>
        </li>
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>5<span class="p-gamesSchedule2__dayWeek">（金）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EX風林火山"></li>
            <li><img src="test.png" alt="渋谷ABEMAS"></li>
            <li><img src="test.png" alt="TEAM RAIDEN / 雷電"></li>
            <li><img src="test.png" alt="U-NEXT Pirates"></li>
          </ul>
        </li>
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>5<span class="p-gamesSchedule2__dayWeek">（金）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="赤坂ドリブンズ"></li>
            <li><img src="test.png" alt="KADOKAWAサクラナイツ"></li>
            <li><img src="test.png" alt="セガサミーフェニックス"></li>
            <li><img src="test.png" alt="BEAST X"></li>
          </ul>
        </li>
      </ul>
    `

    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    // 4 unique days: 12/1, 12/2, 12/4, 12/5
    expect(schedules).toHaveLength(4)

    // Monday (12/1) - 4 teams
    expect(schedules[0].date).toBe('2025-12-01')
    expect(schedules[0].dayOfWeek).toBe('月')
    expect(schedules[0].teamIds).toEqual([4, 6, 7, 8])
    expect(schedules[0].teamIds).toHaveLength(4)

    // Tuesday (12/2) - 4 teams
    expect(schedules[1].date).toBe('2025-12-02')
    expect(schedules[1].dayOfWeek).toBe('火')
    expect(schedules[1].teamIds).toEqual([1, 5, 9, 10])
    expect(schedules[1].teamIds).toHaveLength(4)

    // Thursday (12/4) - 8 teams (merged from 2 matches)
    expect(schedules[2].date).toBe('2025-12-04')
    expect(schedules[2].dayOfWeek).toBe('木')
    expect(schedules[2].teamIds).toEqual([1, 2, 3, 4, 5, 6, 7, 8])
    expect(schedules[2].teamIds).toHaveLength(8)

    // Friday (12/5) - 8 teams (merged from 2 matches)
    expect(schedules[3].date).toBe('2025-12-05')
    expect(schedules[3].dayOfWeek).toBe('金')
    expect(schedules[3].teamIds).toEqual([2, 3, 4, 6, 7, 8, 9, 10])
    expect(schedules[3].teamIds).toHaveLength(8)
  })

  it('should return empty array for empty HTML', () => {
    const html = '<div></div>'
    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    expect(schedules).toEqual([])
  })

  it('should handle malformed date format gracefully', () => {
    const html = `
      <ul class="p-gamesSchedule2__lists">
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">Invalid Date</p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EARTH JETS"></li>
          </ul>
        </li>
      </ul>
    `

    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    // Should skip items with malformed dates
    expect(schedules).toEqual([])
  })

  it('should filter out unknown team names', () => {
    const html = `
      <ul class="p-gamesSchedule2__lists">
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>1<span class="p-gamesSchedule2__dayWeek">（月）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EARTH JETS"></li>
            <li><img src="test.png" alt="Unknown Team"></li>
            <li><img src="test.png" alt="KONAMI麻雀格闘倶楽部"></li>
          </ul>
        </li>
      </ul>
    `

    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    expect(schedules).toHaveLength(1)
    expect(schedules[0].date).toBe('2025-12-01')
    // Should only include known teams (1 and 5)
    expect(schedules[0].teamIds).toEqual([1, 5])
  })

  it('should handle empty schedule', () => {
    const html = `
      <ul class="p-gamesSchedule2__lists">
        <li class="p-gamesSchedule2__list"></li>
      </ul>
    `

    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    expect(schedules).toEqual([])
  })

  it('should handle unparsed day of week', () => {
    const html = `
      <ul class="p-gamesSchedule2__lists">
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>1<span class="p-gamesSchedule2__dayWeek">Unknown</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EARTH JETS"></li>
          </ul>
        </li>
      </ul>
    `

    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    expect(schedules).toHaveLength(1)
    expect(schedules[0].date).toBe('2025-12-01')
    expect(schedules[0].dayOfWeek).toBe('')
    expect(schedules[0].teamIds).toEqual([1])
  })

  it('should handle duplicate teams in same day (edge case)', () => {
    const html = `
      <ul class="p-gamesSchedule2__lists">
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>1<span class="p-gamesSchedule2__dayWeek">（月）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EARTH JETS"></li>
            <li><img src="test.png" alt="EX風林火山"></li>
            <li><img src="test.png" alt="KADOKAWAサクラナイツ"></li>
          </ul>
        </li>
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>1<span class="p-gamesSchedule2__dayWeek">（月）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EARTH JETS"></li>
            <li><img src="test.png" alt="渋谷ABEMAS"></li>
            <li><img src="test.png" alt="セガサミーフェニックス"></li>
          </ul>
        </li>
      </ul>
    `

    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    expect(schedules).toHaveLength(1)
    expect(schedules[0].date).toBe('2025-12-01')
    expect(schedules[0].dayOfWeek).toBe('月')
    // EARTH JETS (id: 1) should not be duplicated
    expect(schedules[0].teamIds).toEqual([1, 3, 4, 6, 7])
    expect(schedules[0].teamIds).toHaveLength(5)
  })

  it('should handle images without alt attribute', () => {
    const html = `
      <ul class="p-gamesSchedule2__lists">
        <li class="p-gamesSchedule2__list">
          <p class="p-gamesSchedule2__data">12<span class="p-gamesSchedule2__slash">/</span>1<span class="p-gamesSchedule2__dayWeek">（月）</span></p>
          <ul class="p-gamesSchedule2__logos">
            <li><img src="test.png" alt="EARTH JETS"></li>
            <li><img src="test.png"></li>
            <li><img src="test.png" alt=""></li>
            <li><img src="test.png" alt="KONAMI麻雀格闘倶楽部"></li>
          </ul>
        </li>
      </ul>
    `

    const seasonPage = parse(html)
    const schedules = getGameSchedule(seasonPage, 2025)

    expect(schedules).toHaveLength(1)
    expect(schedules[0].date).toBe('2025-12-01')
    // Should only include teams with valid alt attributes (1 and 5)
    expect(schedules[0].teamIds).toEqual([1, 5])
    expect(schedules[0].teamIds).toHaveLength(2)
  })
})
