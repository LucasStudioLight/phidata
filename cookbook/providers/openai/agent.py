from phi.agent import Agent, RunResponse  # noqa
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

agent = Agent(
    model=OpenAIChat(model="gpt-4o"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)

# Get the response in a variable
# run: RunResponse = agent.run("Whats the latest from France")
# print(run.content)

# Print the response on the terminal
agent.print_response("Whats the latest from France")