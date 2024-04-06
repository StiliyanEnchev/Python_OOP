from project.trip import Trip

trip_without_family = Trip(2500, 1, False)
trip_without_family.budget = 10000
trip_without_family.book_a_trip('Bulgaria')
trip_without_family.book_a_trip('Australia')


print(trip_without_family.booking_status())
