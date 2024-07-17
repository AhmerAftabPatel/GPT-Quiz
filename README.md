# GPT Quiz

Welcome to the GPT Quiz project, an innovative autonomous agent designed to create personalized newspapers tailored to user preferences. GPT Quiz revolutionizes the way we consume news by leveraging the power of AI to curate, write, design, and edit content based on individual tastes and interests.

## 🔍 Overview

GPT Quiz consists of six specialized sub-agents in LangChain's new [LangGraph Library](https://github.com/langchain-ai/langgraph):

1. **Search Agent**: Scours the web for the text book content.
2. **Curriculum Agent**: Filters and selects text book contents based on user-defined preferences and topics.
3. **Teacher Agent**: Crafts questions related to the topics and difficulty level.
4. **Critique Agent** Provide feedback to the writer until question is approved.
5. **Designer Agent**: Layouts and designs the questrion paper for an aesthetically pleasing reading experience.
6. **Editor Agent**: Constructs the quiz based on produced questions.
7. **Publisher Agent** Publishes the quiz to the frontend or desired service

Each agent plays a critical role in delivering a unique and personalized quiz experience.

<div align="center">
<img align="center" height="500" src="https://tavily-media.s3.amazonaws.com/gpt-quiz-architecture.png">
</div>


## Demo
https://github.com/assafelovic/gpt-quiz/assets/91344214/7f265369-1293-4d95-9be5-02070f12c67e


## 🌟 Features

- **Personalized Content**: Get news that aligns with your interests and preferences.
- **Diverse Sources**: Aggregates content from a wide range of reputable news sources.
- **Engaging Design**: Enjoy a visually appealing layout and design.
- **Quality Assurance**: Rigorous editing ensures reliable and accurate news reporting.
- **User-Friendly Interface**: Easy-to-use platform for setting preferences and receiving your quiz.

## 🛠️ How It Works

1. **Setting Preferences**: Users input their interests, preferred topics, and news sources.
2. **Automated Curation**: The Search and Curator Agents find and select news stories.
3. **Content Creation**: The Writer Agent drafts articles, which are then designed by the Designer Agent.
4. **Quiz Design**: The Editor Agent reviews and finalizes the content.
5. **Delivery**: Users receive their personalized quiz to their mailbox.

## 🚀 Getting Started

### Prerequisites

- Tavily API Key - [Sign Up](https://tavily.com/)
- OpenAI API Key - [Sign Up](https://platform.openai.com/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/rotemweiss57/gpt-quiz.git
    ```
2. Export your API Keys
   ```sh
    export TAVILY_API_KEY=<YOUR_TAVILY_API_KEY>
    export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
    ```
3. Install Requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Run the app
   ```sh
    python app.py
    ```
5. Open the app in your browser
   ```sh
    http://localhost:5000/
    ```
6. Enjoy!

## 🤝 Contributing

Interested in contributing to GPT Quiz? We welcome contributions of all kinds! Check out our [Contributor's Guide](CONTRIBUTING.md) to get started.


## 🛡️ Disclaimer

GPT Quiz is an experimental project and provided "as-is" without any warranty. It's intended for personal use and not as a replacement for professional news outlets.

## 📩 Contact Us

For support or inquiries, please reach out to us:

- [Email](mailto:rotem5707@gmail.com)

Join us in redefining the future of news consumption with GPT Quiz!
