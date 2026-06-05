import { Divider, InputNumber } from 'antd'

interface YearFilterProps {
  year: number
  onYearChange: (value: number | null) => void
}

const currentYear = new Date().getFullYear()

function YearFilter({ year, onYearChange }: YearFilterProps) {
  return (
    <>
      <Divider titlePlacement="left">Year</Divider>
      <InputNumber
        min={0}
        max={currentYear}
        defaultValue={year}
        onChange={onYearChange}
      />
    </>
  )
}

export default YearFilter
