from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner
from open_ai_sdk import external_client
from tools import flights, hotels

class BookingAgent:
    
    def get_booking_options(self):

        model=OpenAIChatCompletionsModel(
            model="gpt-3.5-turbo",
            openai_client=external_client
        )
        booking_agent= Agent(
            name="Booking Agent",
            instructions="""
            You are a helpful travel booking assistant.
            Suggest the most suitable flight and hotel options based on the user's 
            preferences, ensuring clarity and relevance in your recommendations.""",
            tools=[flights.get_fights, hotels.suggest_hotels],
            model=model
        )

        config= RunConfig(
            model=model,
            tracing_disabled=True
        )

        result= Runner.run(booking_agent, f"You are a helpful travel booking assistant.", run_config=config)
        return result.final_output