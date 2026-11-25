# LangGraph Learning Examples

This repository contains progressively organized examples for learning
[LangGraph](https://langchain-ai.github.io/langgraph/) with Python. Each `L*`
directory represents a lesson or experiment.

## Lessons

### L6 - Sequential workflows

- [`prog1.ipynb`](./L6/prog1.ipynb): Builds a sequential BMI calculator with
  `StateGraph`, typed state, and the flow
  `START -> calculate_bmi -> label_bmi -> END`.
- [`prog2.ipynb`](./L6/prog2.ipynb): Builds a simple LLM-based application
  using LangGraph and Google Generative AI.
- [`prog3.ipynb`](./L6/prog3.ipynb): Demonstrates prompt chaining with
  multiple workflow nodes.

### L7 - Parallel workflows and essay evaluation

- [`prog1.ipynb`](./L7/prog1.ipynb): Runs independent cricket statistics
  calculations in parallel before combining them into a summary.
- [`prog2.ipynb`](./L7/prog2.ipynb): Evaluates an essay in parallel for
  language quality, depth of analysis, and clarity of thought. Pydantic
  structured output provides feedback and scores, which are combined into an
  overall evaluation.

### L8 - Conditional workflows

- [`prog1.ipynb`](./L8/prog1.ipynb): Uses conditional edges to calculate
  quadratic-equation roots based on the discriminant without an LLM.
- [`prog2.ipynb`](./L8/prog2.ipynb): Analyzes sentiment and diagnoses a
  technical issue before routing to an appropriate recommendation.

### L9 - Generate, evaluate, and optimize

- [`prog1.ipynb`](./L9/prog1.ipynb): Generates a LinkedIn post, evaluates it
  with structured Pydantic output, and iteratively optimizes it using feedback
  until it is approved or the iteration limit is reached.

### L10 - Chatbot

- [`prog1.ipynb`](./L10/prog1.ipynb): Builds a basic chatbot with a
  message-based state, `add_messages`, and a Google Generative AI model.

### L11 - Persistence and fault tolerance

- [`prog1.ipynb`](./L11/prog1.ipynb): Demonstrates the use of persistence and
  fault tolerance in LangGraph. It shows how to save and restore the state of a
  workflow, allowing it to resume from a checkpoint after an interruption.
  