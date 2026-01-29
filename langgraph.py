# Import necessary components from LangGraph
# - StateGraph: Main class for creating stateful graphs
# - END: Special node that marks the end of the graph execution
from langgraph.graph import StateGraph, END
from typing import TypedDict

# Define the structure of our state using TypedDict
# Think of this as a blueprint for what data flows through the graph
# - 'question': User's input question (string)
# - 'answer': Generated answer (string)
class State(TypedDict):
    question: str  # Stores the user's question
    answer: str    # Stores the generated answer

# Define a node function that processes the state
# This function takes the current state, processes it, and returns updates
def generate_answer(state: State):
    # Simple logic: Just returns a formatted string with the question
    # In real apps, this would call an LLM or other complex logic
    return {"answer": f"Answering: {state['question']}"}

# ========== BUILDING THE GRAPH ==========

# Create an empty graph with our State structure
# This graph will manage the flow of data between nodes
graph = StateGraph(State)

# Add a node to the graph
# - "generate": Name of the node (can be any string)
# - generate_answer: The function that runs when this node is executed
graph.add_node("generate", generate_answer)

# Set the starting point of the graph
# When we run the graph, execution begins at this node
graph.set_entry_point("generate")

# Connect the "generate" node to END
# This creates a one-way path: generate → END
# Once "generate" completes, the graph execution ends
graph.add_edge("generate", END)

# ========== COMPILING AND RUNNING ==========

# Compile the graph into an executable application
# This validates the graph structure and creates an optimized version
app = graph.compile()

# Run the graph with initial input
# We provide the starting state with a question
result = app.invoke({"question": "What is AI?"})

# Print the result from the final state
# The 'answer' key contains the output from our generate_answer function
print(result["answer"])
