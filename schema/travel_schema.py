from pydantic import BaseModel
from typing import Optional, List, Dict



class Flight(BaseModel):
    airline: str
    flight_no: str
    departure: str  # ISO datetime
    arrival: str    # ISO datetime
    price_usd: float
    duration: str
    stops: int


class Hotel(BaseModel):
    name: str
    rating: Optional[float]
    price_per_night_usd: Optional[float]
    address: Optional[str]
    manager: Optional[Dict[str, str]]


class DestinationSuggestion(BaseModel):
    place: str
    reason: str
    best_time: Optional[str]
    popular_activities: List[str]


class ExploreItem(BaseModel):
    name: str
    type: str    # 'attraction'|'food'|'experience'
    description: Optional[str]


class TravelPlan(BaseModel):
    flight: Flight
    hotel: Hotel
    destination: DestinationSuggestion
    itinerary: Optional[List[str]]
