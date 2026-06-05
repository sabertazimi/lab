import type { ColumnType } from 'antd/es/table'
import type { Paper } from '../api'
import { Table } from 'antd'

interface TableResultProps {
  isLoading: boolean
  dataSource: Paper[]
}

function TableResult({ isLoading, dataSource }: TableResultProps) {
  const columns: ColumnType<Paper>[] = [
    {
      title: 'Title',
      dataIndex: 'title',
      key: 'title',
      sorter: (a, b) =>
        a.title.localeCompare(b.title)
        || (b.citations ?? 0) - (a.citations ?? 0)
        || b.year.localeCompare(a.year)
        || a.venue.localeCompare(b.venue)
        || a.url.localeCompare(b.url),
    },
    {
      title: 'Venue',
      dataIndex: 'venue',
      key: 'venue',
      sorter: (a, b) =>
        a.venue.localeCompare(b.venue)
        || (b.citations ?? 0) - (a.citations ?? 0)
        || b.year.localeCompare(a.year)
        || a.title.localeCompare(b.title)
        || a.url.localeCompare(b.url),
    },
    {
      title: 'Year',
      dataIndex: 'year',
      key: 'year',
      sorter: (a, b) =>
        b.year.localeCompare(a.year)
        || (b.citations ?? 0) - (a.citations ?? 0)
        || a.venue.localeCompare(b.venue)
        || a.title.localeCompare(b.title)
        || a.url.localeCompare(b.url),
    },
    {
      title: 'Citations',
      dataIndex: 'citations',
      key: 'citations',
      sorter: (a, b) =>
        (b.citations ?? 0) - (a.citations ?? 0)
        || b.year.localeCompare(a.year)
        || a.venue.localeCompare(b.venue)
        || a.title.localeCompare(b.title)
        || a.url.localeCompare(b.url),
    },
    {
      title: 'Url',
      dataIndex: 'url',
      key: 'url',
      render: (url: string) => (
        <a href={url} target="_blank" rel="noopener noreferrer nofollow">
          {url}
        </a>
      ),
      sorter: (a, b) =>
        a.url.localeCompare(b.url)
        || (b.citations ?? 0) - (a.citations ?? 0)
        || b.year.localeCompare(a.year)
        || a.venue.localeCompare(b.venue)
        || a.title.localeCompare(b.title),
    },
  ]

  return (
    <Table<Paper>
      rowKey={item => item.title}
      columns={columns}
      dataSource={dataSource}
      loading={isLoading}
      pagination={{
        defaultPageSize: 40,
        hideOnSinglePage: true,
        pageSizeOptions: ['20', '40', '60', '80', '100'],
        showTotal: (total, range) =>
          `${range[0]}-${range[1]} of ${total} items`,
        showQuickJumper: true,
        showSizeChanger: true,
      }}
    />
  )
}

export default TableResult
