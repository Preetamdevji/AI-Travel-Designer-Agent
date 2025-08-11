from open_ai_sdk import external_client
from agents import OpenAIChatCompletionsModel
from agents.run import RunConfig
from agents import Agent, Runner

class DestinationAgentt:
    
    async def suggest_destinations(self):
    
        model=OpenAIChatCompletionsModel(
            model='gpt-3.5-turbo',
            openai_client=external_client
        )

        destination_agent = Agent(
            name="Suggest Destination",
            instructions="""You are a travel destination recommendation agent.
                Suggest a destination based on the user's mood and interests.
                Use the `suggest_destinations` tool to generate the result.
                Return a DestinationSuggestion object.""",
            model=model
        )

        config= RunConfig(
            model=model,
            tracing_disabled=True
        )

        result = Runner.run(destination_agent, f"Suggest destination according to user's mood and interest", run_config=config)
        return result.final_output