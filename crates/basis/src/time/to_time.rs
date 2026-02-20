use chrono::{DateTime, FixedOffset};

pub trait ToTime {
    fn to_time(&self) -> DateTime<FixedOffset>;
}

impl ToTime for i64 {
    fn to_time(&self) -> DateTime<FixedOffset> {
        let china_timezone = FixedOffset::east_opt(8 * 3600).unwrap();
        let utc_time = DateTime::from_timestamp(*self, 0).unwrap();
        utc_time.with_timezone(&china_timezone)
    }
}
