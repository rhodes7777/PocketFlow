<<<<<<< HEAD
# Search-Answer System

A 3-node AI system built with PocketFlow that intelligently decides whether to search for information or answer questions directly.

## System Overview

The system consists of three main nodes:

1. **DecideNode**: Analyzes the user's question and decides whether to search for more information or answer directly
2. **SearchNode**: Performs web searches using DuckDuckGo when more information is needed
3. **AnswerNode**: Provides the final answer based on the question and any search results

## Flow Diagram

```mermaid
flowchart TD
    A[DecideNode] -->|search| B[SearchNode]
    A -->|answer| C[AnswerNode]
    B -->|decide| A
    C -->|complete| D[End]
```

## Setup

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

You need to set your OpenAI API key:

```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

### 4. Run the System

#### Interactive Mode
```bash
source venv/bin/activate  # Ensure virtual environment is activated
python main.py
```

#### Command Line Mode
```bash
source venv/bin/activate  # Ensure virtual environment is activated
python main.py "What is the weather like in New York today?"
```

## Example Usage

### Example 1: Current Information (Will Search)
```bash
python main.py "Who won the Nobel Prize in Physics 2024?"
```

The system will:
1. Decide to search for current information
2. Search for Nobel Prize 2024 information
3. Provide an answer based on search results

### Example 2: General Knowledge (May Answer Directly)
```bash
python main.py "What is the capital of France?"
```

The system may:
1. Decide it has enough knowledge to answer directly
2. Provide the answer without searching

## System Architecture

### Utility Functions

- **`utils/call_llm.py`**: OpenAI GPT API wrapper
- **`utils/search_web.py`**: DuckDuckGo search functionality

### Nodes

- **`DecideNode`**: Uses LLM to decide whether to search or answer
- **`SearchNode`**: Performs web searches and stores results
- **`AnswerNode`**: Generates final answers using LLM

### Flow Control

The system uses action-based transitions:
- `"search"`: DecideNode → SearchNode
- `"answer"`: DecideNode → AnswerNode  
- `"decide"`: SearchNode → DecideNode (for re-evaluation)

## Key Features

- **Intelligent Decision Making**: The system analyzes questions to determine if current information is needed
- **Search Loop**: Can perform multiple searches if initial results are insufficient
- **Context Preservation**: Maintains search history for better decision making
- **Error Handling**: Includes retries and fallback mechanisms
- **Structured Output**: Uses YAML for reliable LLM response parsing

## Customization

You can modify the behavior by:

1. **Adjusting Node Parameters**: Change `max_retries` and `wait` times in `flow.py`
2. **Modifying Search Results**: Change `max_results` in `utils/search_web.py`
3. **Updating Prompts**: Modify the decision logic in `DecideNode.exec()`
4. **Changing Models**: Update the model in `utils/call_llm.py`

## Troubleshooting

### Common Issues

1. **Missing API Key**: Ensure `OPENAI_API_KEY` is set
2. **Rate Limits**: The system includes retry logic with waits
3. **Network Issues**: DuckDuckGo search has error handling
4. **Parsing Errors**: YAML parsing includes fallback mechanisms

### Debug Mode

To see detailed flow execution, you can add logging or print statements to the nodes.

## Project Structure

```
.
├── utils/
│   ├── __init__.py
│   ├── call_llm.py          # OpenAI API wrapper
│   └── search_web.py        # DuckDuckGo search
├── nodes.py                 # Node definitions
├── flow.py                  # Flow creation
├── main.py                  # Main entry point
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Contributing

This system follows the PocketFlow framework guidelines for agentic coding. When making changes:

1. Keep utility functions simple and testable
2. Maintain clear separation between data (shared store) and compute (nodes)
3. Use structured outputs for reliable LLM interactions
4. Include error handling and retries for robust operation

=======
>>>>>>> upstream/main
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – 100-line minimalist LLM framework" width="600"/>
</div>

<!-- For translation, replace English with [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md), and remove the link for the target language. -->

English | [中文](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_CHINESE.md) | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | [Deutsch](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_GERMAN.md) | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow is a [100-line](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) minimalist LLM framework

- **Lightweight**: Just 100 lines. Zero bloat, zero dependencies, zero vendor lock-in.
  
- **Expressive**: Everything you love—([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agents](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html), and more.

- **[Agentic Coding](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**: Let AI Agents (e.g., Cursor AI) build Agents—10x productivity boost!

Get started with Pocket Flow:
- To install, ```pip install pocketflow```or just copy the [source code](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) (only 100 lines).
- To learn more, check out the [documentation](https://the-pocket.github.io/PocketFlow/). To learn the motivation, read the [story](https://zacharyhuang.substack.com/p/i-built-an-llm-framework-in-just).
- Have questions? Check out this [AI Assistant](https://chatgpt.com/g/g-677464af36588191b9eba4901946557b-pocket-flow-assistant), or [create an issue!](https://github.com/The-Pocket/PocketFlow/issues/new)
- 🎉 Join our [Discord](https://discord.gg/hUHHE9Sa6T) to connect with other developers building with Pocket Flow!
- 🎉 Pocket Flow is initially Python, but we now have [Typescript](https://github.com/The-Pocket/PocketFlow-Typescript), [Java](https://github.com/The-Pocket/PocketFlow-Java), [C++](https://github.com/The-Pocket/PocketFlow-CPP) and [Go](https://github.com/The-Pocket/PocketFlow-Go) versions!

## Why Pocket Flow?

Current LLM frameworks are bloated... You only need 100 lines for LLM Framework!

<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/meme.jpg" width="400"/>


  |                | **Abstraction**          | **App-Specific Wrappers**                                      | **Vendor-Specific Wrappers**                                    | **Lines**       | **Size**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | Agent, Chain               | Many <br><sup><sub>(e.g., QA, Summarization)</sub></sup>              | Many <br><sup><sub>(e.g., OpenAI, Pinecone, etc.)</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | Agent, Chain            | Many <br><sup><sub>(e.g., FileReadTool, SerperDevTool)</sub></sup>         | Many <br><sup><sub>(e.g., OpenAI, Anthropic, Pinecone, etc.)</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | Agent                      | Some <br><sup><sub>(e.g., CodeAgent, VisitWebTool)</sub></sup>         | Some <br><sup><sub>(e.g., DuckDuckGo, Hugging Face, etc.)</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | Agent, Graph           | Some <br><sup><sub>(e.g., Semantic Search)</sub></sup>                     | Some <br><sup><sub>(e.g., PostgresStore, SqliteSaver, etc.) </sub></sup>        | 37K           | +51MB                      |
| AutoGen    | Agent                | Some <br><sup><sub>(e.g., Tool Agent, Chat Agent)</sub></sup>              | Many <sup><sub>[Optional]<br> (e.g., OpenAI, Pinecone, etc.)</sub></sup>        | 7K <br><sup><sub>(core-only)</sub></sup>    | +26MB <br><sup><sub>(core-only)</sub></sup>          |
| **PocketFlow** | **Graph**                    | **None**                                                 | **None**                                                  | **100**       | **+56KB**                  |

</div>

## How does Pocket Flow work?

The [100 lines](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) capture the core abstraction of LLM frameworks: Graph!
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

From there, it's easy to implement popular design patterns like ([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agents](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html), etc.
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ Below are basic tutorials:

<div align="center">
  
|  Name  | Difficulty    |  Description  |  
| :-------------:  | :-------------: | :--------------------- |  
| [Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <sup>*Dummy*</sup>  | A basic chat bot with conversation history |
| [Structured Output](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <sup>*Dummy*</sup> | Extracting structured data from resumes by prompting |
| [Workflow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <sup>*Dummy*</sup> | A writing workflow that outlines, writes content, and applies styling |
| [Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <sup>*Dummy*</sup>  | A research agent that can search the web and answer questions |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <sup>*Dummy*</sup> | A simple Retrieval-augmented Generation process |
| [Batch](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <sup>*Dummy*</sup> | A batch processor that translates markdown into multiple languages |
| [Streaming](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <sup>*Dummy*</sup> | A real-time LLM streaming demo with user interrupt capability |
| [Chat Guardrail](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <sup>*Dummy*</sup> | A travel advisor chatbot that only processes travel-related queries |
| [Majority Vote](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ☆☆☆ <sup>*Dummy*</sup> | Improve reasoning accuracy by aggregating multiple solution attempts |
| [Map-Reduce](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <sup>*Dummy*</sup>  | Batch resume qualification using map-reduce pattern |
| [CLI HITL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-cli-hitl) | ☆☆☆ <sup>*Dummy*</sup>  | A command-line joke generator with human-in-the-loop feedback |
| [Multi-Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <sup>*Beginner*</sup> | A Taboo word game for async communication between 2 agents |
| [Supervisor](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <sup>*Beginner*</sup> | Research agent is getting unreliable... Let's build a supervision process|
| [Parallel](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) |  ★☆☆ <sup>*Beginner*</sup> | A parallel execution demo that shows 3x speedup |
| [Parallel Flow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <sup>*Beginner*</sup> | A parallel image processing showing 8x speedup |
| [Thinking](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) |  ★☆☆ <sup>*Beginner*</sup> | Solve complex reasoning problems through Chain-of-Thought |
| [Memory](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) |  ★☆☆ <sup>*Beginner*</sup> | A chat bot with short-term and long-term memory |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) |  ★☆☆ <sup>*Beginner*</sup>  | Convert natural language to SQL queries with an auto-debug loop |
| [Code Generator](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-code-generator) | ★☆☆ <sup>*Beginner*</sup> | Generate test cases, implement solutions, and iteratively improve code |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) |  ★☆☆ <sup>*Beginner*</sup> |  Agent using Model Context Protocol for numerical operations |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) |  ★☆☆ <sup>*Beginner*</sup> | Agent wrapped with A2A protocol for inter-agent communication |
| [Streamlit FSM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-streamlit-fsm) | ★☆☆ <sup>*Beginner*</sup> | Streamlit app with finite state machine for HITL image generation |
| [FastAPI WebSocket](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-websocket) | ★☆☆ <sup>*Beginner*</sup> | Real-time chat interface with streaming LLM responses via WebSocket |
| [FastAPI Background](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-background) | ★☆☆ <sup>*Beginner*</sup> | FastAPI app with background jobs and real-time progress via SSE |
| [Voice Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-voice-chat) | ★☆☆ <sup>*Beginner*</sup> | An interactive voice chat application with VAD, STT, LLM, and TTS. |

</div>

👀 Want to see other tutorials for dummies? [Create an issue!](https://github.com/The-Pocket/PocketFlow/issues/new)

## How to Use Pocket Flow?

🚀 Through **Agentic Coding**—the fastest LLM App development paradigm-where *humans design* and *agents code*!

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ Below are examples of more complex LLM Apps:

<div align="center">
  
|  App Name     |  Difficulty    | Topics  | Human Design | Agent Code |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [Website Chatbot](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot) <br> <sup><sub>Turn your website into a 24/7 customer support genius</sup></sub> | ★★☆ <br> *Medium* | [Agent](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) <br> [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) | [Design Doc](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/docs/design.md) | [Flow Code](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/flow.py)
| [Danganronpa Simulator](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator) <br> <sup><sub>Forget the Turing test. Danganronpa, the ultimate AI experiment!</sup></sub> | ★★★ <br> *Advanced*   | [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) <br> [Agent](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Design Doc](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/docs/design.md) | [Flow Code](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/flow.py)
| [Codebase Knowledge Builder](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>Life's too short to stare at others' code in confusion</sup></sub> |  ★★☆ <br> *Medium* | [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [Design Doc](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [Flow Code](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [Build Cursor with Cursor](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>We'll reach the singularity soon ...</sup></sub> | ★★★ <br> *Advanced*   | [Agent](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Design Doc](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [Flow Code](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [Ask AI Paul Graham](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>Ask AI Paul Graham, in case you don't get in</sup></sub> | ★★☆ <br> *Medium*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [Design Doc](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [Flow Code](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [Youtube Summarizer](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub> Explain YouTube Videos to you like you're 5 </sup></sub> | ★☆☆ <br> *Beginner*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [Design Doc](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [Flow Code](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [Cold Opener Generator](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub> Instant icebreakers that turn cold leads hot </sup></sub> | ★☆☆ <br> *Beginner*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [Web Search](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [Design Doc](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [Flow Code](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)


</div>

- Want to learn **Agentic Coding**?

  - Check out [my YouTube](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1) for video tutorial on how some apps above are made!

  - Want to build your own LLM App? Read this [post](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)! Start with [this template](https://github.com/The-Pocket/PocketFlow-Template-Python)!


