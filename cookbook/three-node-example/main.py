import sys
from flow import create_flow


def main():
    question = "Who won the Nobel Prize in Physics 2024?"
    for arg in sys.argv[1:]:
        if arg.startswith("--"):
            question = arg[2:]
            break

    pipeline = create_flow()
    shared = {"question": question}
    print(f"Processing question: {question}")
    pipeline.run(shared)
    print("\nFinal Answer:\n" + shared.get("answer", "No answer"))


if __name__ == "__main__":
    main()
