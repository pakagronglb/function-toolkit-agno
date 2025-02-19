from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools

# Create the Agent and attach the CalculatorTools
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[CalculatorTools(enable_all=True)],
    show_tool_calls=True
)

agent.print_response("What is 15 - 3")