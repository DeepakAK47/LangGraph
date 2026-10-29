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

## Requirements

- Python 3.11 or newer
- Jupyter Notebook or JupyterLab
- `langgraph`

## Setup

Create and activate a virtual environment from the repository root:

```bash
python -m venv .venv
```

On Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the notebook dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install langgraph ipykernel jupyter
```

Register the environment as a Jupyter kernel:

```bash
python -m ipykernel install --user --name langgraph-learning --display-name "Python (LangGraph Learning)"
```

## Running the notebook

Start Jupyter from the repository root:

```bash
jupyter notebook
```

Open `L6/prog1.ipynb`, select the `Python (LangGraph Learning)` kernel, and run
the cells in order. The example uses an input of 70 kg and 1.75 m and prints
the calculated BMI and category.

## Repository structure

```text
.
|-- L6/
|   `-- prog1.ipynb    # Sequential BMI workflow
|-- L7/ ... L28/       # Additional lesson directories
`-- README.md
```

## Notes

- Heights are expected in metres and weights in kilograms.
- The notebook contains a local interpreter path check; select the active
  virtual environment as the notebook kernel rather than relying on a
  machine-specific path.
- Do not commit API keys or other secrets. Keep local environment files out of
  version control.