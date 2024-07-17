from datetime import datetime
from langchain.adapters.openai import convert_openai_messages
from langchain_openai import ChatOpenAI
import json5 as json

sample_json = """
{
  "question": content of the question,
  "date": today's date,
  "options": [
    "option 1",
    "option 2",
    "option 3",
    "option 4",
    ],
    "answer": "correct answer from 4 options selected for the question"
}
"""

sample_revise_json = """
{
    "options": [
    "option 1",
    "option 2",
    "option 3",
    "option 4",
    ],
    "question" : content of the new question,
    "message": "message to the critique"
}
"""


class WriterAgent:
    def __init__(self):
        pass

    def writer(self, query: str, sources: list):

        prompt = [{
            "role": "system",
            "content": "You are a questionaire writer for a quiz. Your sole purpose is to form a well-written question which has a one word answer and list of 4 options to select from for the right answer about a "
                       "topic using a list of text books contents.\n "
        }, {
            "role": "user",
            "content": f"Today's date is {datetime.now().strftime('%d/%m/%Y')}\n."
                       f"Query or Topic: {query}"
                       f"{sources}\n"
                       f"Your task is to write a welformed question and 4 options to choose from for the test takers about the provided query or "
                       f"topic based on the sources.\n "
                       f"Please return nothing but a JSON in the following format:\n"
                       f"{sample_json}\n "

        }]

        lc_messages = convert_openai_messages(prompt)
        optional_params = {
            "response_format": {"type": "json_object"}
        }

        response = ChatOpenAI(model='gpt-3.5-turbo', max_retries=1, model_kwargs=optional_params).invoke(lc_messages).content
        return json.loads(response)

    def revise(self, article: dict):
        prompt = [{
            "role": "system",
            "content": "You are a question paper editor. Your sole purpose is to edit a well-written question and the 4 options given about a "
                       "topic based on given critique\n "
        }, {
            "role": "user",
            "content": f"{str(article)}\n"
                        f"Your task is to edit the question based on the critique given.\n "
                        f"Please return json format of the updated 'options', 'question' and a new 'message' field"
                        f"to the critique that explain your changes or why you didn't change anything.\n"
                        f"please return nothing but a JSON in the following format:\n"
                        f"{sample_revise_json}\n "

        }]

        lc_messages = convert_openai_messages(prompt)
        optional_params = {
            "response_format": {"type": "json_object"}
        }

        response = ChatOpenAI(model='gpt-3.5-turbo', max_retries=1, model_kwargs=optional_params).invoke(lc_messages).content
        response = json.loads(response)
        print(f"For question: {article['question']}")
        print(f"Writer Revision Message: {response['message']}\n")
        return response

    def run(self, article: dict):
        critique = article.get("critique")
        if critique is not None:
            article.update(self.revise(article))
        else:
            article.update(self.writer(article["query"], article["sources"]))
        return article
