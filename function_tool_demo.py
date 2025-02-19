from agno.agent import Agent
from agno.models.openai import OpenAIChat

def multiply_numbers(a: int, b: int) -> int:
    """Multiplies two numbers and returns the result."""
    return str(a * b)

# Create the Agent and register the function as a tool
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[multiply_numbers],  # Registering the function directly
    show_tool_calls=True       # Visualizes when the tool is called
)

agent.print_response("What is seven times six?")