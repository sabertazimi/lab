import type { Paper } from '../api'
import { Alert, Empty, List } from 'antd'
import { getStatisticsData } from '../api'

interface StatisticsModalProps {
  error: Error | null
  isLoading: boolean
  items: Paper[]
  venues: string[]
  year: number
}

function StatisticsModal({ error, isLoading, items, venues, year }: StatisticsModalProps) {
  if (error) {
    return (
      <Alert
        message="Error"
        description="Bad request - please retry."
        type="error"
        showIcon
      />
    )
  }

  const statisticsData = getStatisticsData(items, { venues, year })

  if (!statisticsData || !statisticsData.length)
    return <Empty />

  const sortedData = statisticsData.sort(
    (a, b) => b.count - a.count || a.venue.localeCompare(b.venue),
  )

  return (
    <List
      dataSource={sortedData}
      loading={isLoading}
      renderItem={item => (
        <List.Item key={item.venue}>
          <List.Item.Meta description={item.venue} />
          {item.count}
        </List.Item>
      )}
    />
  )
}

export default StatisticsModal
