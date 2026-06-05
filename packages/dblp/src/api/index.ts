import venuesData from '../venues.json'

interface VenueItem {
  venue: string
  title?: string
}

interface Paper {
  key: string
  title: string
  venue: string
  year: string
  url: string
  citations?: number
}

export const VenuesDB: VenueItem[] = venuesData
export const VENUES_LIST: string[] = VenuesDB.map(({ venue }) => venue)
export const DEFAULT_VENUES_LIST: string[] = VENUES_LIST.slice(0, 30)

function dblpQuery(keyword: string, venue: string): string {
  return `https://dblp.org/search/publ/api?q=${keyword} venue:${venue}:&format=json&h=999`
}

function scIdsQuery(title: string): string {
  return `https://api.semanticscholar.org/graph/v1/paper/search?query=${title}&limit=1`
}

function scCitationsQuery(paperId: string): string {
  return `https://api.semanticscholar.org/graph/v1/paper/${paperId}?fields=citationCount`
}

export async function fetchDblpPapers(
  keyword: string,
  venues: string[],
): Promise<Paper[] | null> {
  const papersResponse = await Promise.all(
    venues.map(venue =>
      fetch(dblpQuery(keyword, venue), {
        method: 'GET',
        mode: 'cors',
      }),
    ),
  )

  const papersJson = await Promise.all(
    papersResponse.map(response => (response.ok ? response.json() : null)),
  )

  const papers = papersJson
    ? papersJson
        .map(({ result }: { result: { hits?: { hit?: Array<{ info: Record<string, string> }> } } }) => {
          const { hit } = result?.hits ?? {}

          if (!hit)
            return []

          return hit.map(({ info }) => ({
            key: info.key,
            title: info.title,
            venue: info.venue.replaceAll('.', ''),
            year: info.year,
            url: info.ee,
          }))
        })
        .flat()
    : null

  return papers
}

export async function fetchPaperCitations(papers: Paper[]): Promise<number[]> {
  let paperCitations: number[] = Array.from({ length: papers.length }).fill(0) as number[]

  try {
    const paperIdsResponse = await Promise.all(
      papers.map(paper =>
        fetch(scIdsQuery(paper.title), {
          method: 'GET',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
        }),
      ),
    )

    const paperIdsJson = await Promise.all(
      paperIdsResponse.map(response => (response.ok ? response.json() : {})),
    )

    if (!paperIdsJson)
      return paperCitations

    const paperIds = paperIdsJson.map(
      (paper: { data?: Array<{ paperId: string }> }) =>
        paper?.data?.[0]?.paperId ?? '0',
    )

    const paperCitationsResponse = await Promise.all(
      paperIds.map(paperId =>
        fetch(scCitationsQuery(paperId), {
          method: 'GET',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
        }),
      ),
    )

    const paperCitationsJson = await Promise.all(
      paperCitationsResponse.map(response =>
        response.ok ? response.json() : {},
      ),
    )

    if (!paperCitationsJson)
      return paperCitations

    paperCitations = paperCitationsJson.map(
      (citation: { citationCount?: number }) =>
        citation?.citationCount ?? 0,
    )
  } catch {
    console.error('Up to API limits.')
  }

  return paperCitations
}

function getVenueItem(venueName: string): VenueItem | undefined {
  return VenuesDB.find(({ venue }) => venue === venueName)
}

export function getVenueTitle(venue: string): string {
  return getVenueItem(venue)?.title ?? venue
}

export function getFilteredData(
  items: Paper[],
  { venues, year }: { venues: string[], year: number },
): Paper[] {
  return items
    .filter(
      item => venues.includes(item.venue) && Number.parseInt(item.year, 10) >= year,
    )
    .map(item => ({
      ...item,
      venue: getVenueTitle(item.venue),
    }))
}

export function getStatisticsData(
  items: Paper[],
  { venues, year }: { venues: string[], year: number },
): Array<{ venue: string, count: number }> {
  const filteredItems = getFilteredData(items, { venues, year })
  const statisticsData: Record<string, number> = {}

  filteredItems.forEach(({ venue }) => {
    if (!statisticsData[venue])
      statisticsData[venue] = 0

    statisticsData[venue] += 1
  })

  return Object.keys(statisticsData).map(key => ({
    venue: key,
    count: statisticsData[key],
  }))
}

export type { Paper }
