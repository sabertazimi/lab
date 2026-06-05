import { Checkbox, Col, Divider, Row } from 'antd'
import { getVenueTitle, VENUES_LIST } from '../api'

interface VenuesFilterProps {
  venues: string[]
  indeterminate: boolean
  checkAll: boolean
  onVenuesChange: (checkedValues: string[]) => void
  onCheckAllChange: (event: { target: { checked: boolean } }) => void
}

function VenuesFilter({
  venues,
  indeterminate,
  checkAll,
  onVenuesChange,
  onCheckAllChange,
}: VenuesFilterProps) {
  return (
    <>
      <Divider titlePlacement="left">Venues</Divider>
      <Checkbox
        indeterminate={indeterminate}
        onChange={onCheckAllChange}
        checked={checkAll}
        style={
          checkAll ? { color: '#1890ff' } : { color: 'rgba(0, 0, 0, 0.65)' }
        }
      >
        <b>Check All</b>
      </Checkbox>
      <Checkbox.Group
        style={{
          width: '100%',
        }}
        value={venues}
        onChange={onVenuesChange}
      >
        <Row justify="center" align="middle">
          {VENUES_LIST.map(venue => (
            <Col span={24} key={venue}>
              <Checkbox value={venue}>{getVenueTitle(venue)}</Checkbox>
            </Col>
          ))}
        </Row>
      </Checkbox.Group>
    </>
  )
}

export default VenuesFilter
