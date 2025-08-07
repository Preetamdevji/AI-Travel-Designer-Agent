from tools.flights import get_flights
from tools.hotels import suggest_hotels


class BookingAgent:
    def get_booking_options(self, user_input: str):
        flights=get_flights(user_input)
        hotels=suggest_hotels(user_input)

        return {
            "flights": flights,
            "hotels": hotels
        }