from open_ai_sdk import external_client
from agents import OpenAIChatCompletionsModel
from agents.run import RunConfig
from agents import Agent, Runner

class ExploreAgent:
    
    async def explore_activities(self):
    
        model=OpenAIChatCompletionsModel(
            model='gpt-3.5-turbo',
            openai_client=external_client
        )

        explore_agent = Agent(
            name="Explore Activities",
            instructions="""You are the Explore Agent in an AI Travel Designer system.  
                            Your role is to explore and suggest travel destinations that match the user’s preferences, interests, and mood.  
                            Use clear, concise, and engaging descriptions.""",
            model=model
        )

        config= RunConfig(
            model=model,
            tracing_disabled=True
        )

        result = Runner.run(explore_agent, f"Explorer activities and suggests according to user's mood or interest", run_config=config)
        return result.final_output