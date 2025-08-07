from agent_controllers.booking_agent import BookingAgent
from agent_controllers.destination_agent import DestinationAgent
from agent_controllers.explore_agent import ExploreAgent
from utils.detect_intent import detect_intent_with_llm


class TravelDesignerAgent:
    def __init__(self):
        self.destination_agent=DestinationAgent()
        self.booking_agent=BookingAgent()
        self.explore_agent=ExploreAgent()


    def main_coordinator(self,user_input: str):
        intent=detect_intent_with_llm(user_input)

        if intent == "destination":
            return self.destination_agent.find_places(user_input)
        elif intent == "booking":
            return self.booking_agent.get_booking_options(user_input)
        elif intent == "explore":
            return self.explore_agent.suggest_attractions(user_input)
        else:
            return "I'm sorry, I can't help with that. Please try again"