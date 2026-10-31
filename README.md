# LangGraph Learning Examples

This repository contains progressively organized examples for learning
[LangGraph](https://langchain-ai.github.io/langgraph/) with Python. Each `L*`
directory represents a lesson or experiment.

## Current example

[`L6/prog1.ipynb`](./L6/prog1.ipynb) demonstrates a sequential workflow that:

1. Accepts a person's weight and height.
2. Calculates their body mass index (BMI).
3. Assigns a BMI category.
4. Returns the updated state from the compiled graph.

The workflow is built from two nodes:

```text
START -> calculate_bmi -> label_bmi -> END
```

The notebook uses a typed `BMIState` dictionary to pass data between nodes.

### L6

1. Building a sequential workflow with LangGraph.
2. Using typed dictionaries to manage state between nodes.
3. Invoking the workflow with an initial state and retrieving the final state.
4. Using LangGraph to create a simple BMI calculator with labeled categories.
5. Demonstrating the use of LangGraph's `StateGraph` to define and execute a workflow.
6. Showcasing the integration of LangGraph with LangChain's Google Generative AI model for prompt chaining.
7. Illustrating how to create nodes for generating outliers and blogs based on input text.
8. Highlighting the use of environment variables for API key management in LangGraph workflows.
9. Providing a clear example of how to structure and execute a LangGraph workflow with typed state dictionaries.


### L7
