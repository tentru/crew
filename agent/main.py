#!/usr/bin/env python
import sys
import warnings
from crew import Crew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run(topic="AI LLMs"):
    """
    Run the crew.
    """
    inputs = {'topic': topic}
    Crew().crew().kickoff(inputs=inputs)

def train(n_iterations, filename, topic="AI LLMs"):
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": topic}
    try:
        Crew().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay(task_id):
    """
    Replay the crew execution from a specific task.
    """
    try:
        Crew().crew().replay(task_id=task_id)
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(n_iterations, openai_model_name, topic="AI LLMs"):
    """
    Test the crew execution and return the results.
    """
    inputs = {"topic": topic}
    try:
        Crew().crew().test(n_iterations=n_iterations, openai_model_name=openai_model_name, inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

# Command-line entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [args]")
        print("Commands:")
        print("  run                          - Run the crew")
        print("  train <iterations> <file>    - Train the crew for given iterations")
        print("  replay <task_id>             - Replay the crew execution from a task")
        print("  test <iterations> <model>    - Test the crew execution")
        sys.exit(1)

    command = sys.argv[1]

    if command == "run":
        run()
    elif command == "train":
        if len(sys.argv) < 4:
            print("Usage: main.py train <iterations> <file>")
            sys.exit(1)
        train(n_iterations=int(sys.argv[2]), filename=sys.argv[3])
    elif command == "replay":
        if len(sys.argv) < 3:
            print("Usage: main.py replay <task_id>")
            sys.exit(1)
        replay(task_id=sys.argv[2])
    elif command == "test":
        if len(sys.argv) < 4:
            print("Usage: main.py test <iterations> <model>")
            sys.exit(1)
        test(n_iterations=int(sys.argv[2]), openai_model_name=sys.argv[3])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
