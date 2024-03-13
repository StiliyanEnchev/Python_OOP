import calendar


class DVD:
    def __init__(self, name, dvd_id, year_made, month_made, age_res):
        self.name = name
        self.id = dvd_id
        self.creation_year = year_made
        self.creation_month = month_made
        self.age_restriction = age_res
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id, name, date, age_res):
        day, month, year = [int(x) for x in date.split('.')]
        month_name = calendar.month_name[month]
        return cls(name, dvd_id, year, month_name, age_res)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has "
                f"age restriction {self.age_restriction}. Status: "
                f"{'rented' if self.is_rented else 'not rented'}")