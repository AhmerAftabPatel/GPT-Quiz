import os
import re

class DesignerAgent:
    def __init__(self, output_dir):
        self.output_dir = output_dir


    def load_html_template(self):
        relative_path = "../templates/article/index.html"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        html_file_path = os.path.join(dir_path, relative_path)
        with open(html_file_path) as f:
            html_template = f.read()
        return html_template

    def designer(self, article):
        print("design starts")
        print(article)
        html_template = self.load_html_template()
        title = article["question"]
        date = article["date"]
        image = article["image"]
        options = article["options"]
        html_template = html_template.replace("{{question}}", title)
        html_template = html_template.replace("{{image}}", image)
        html_template = html_template.replace("{{date}}", date)
        for i in range(4):
            html_template = html_template.replace(f"{{option{i + 1}}}", options[i])
        article["html"] = html_template
        article = self.save_article_html(article)
        return article

    def save_article_html(self, article):
        filename = re.sub(r'[\/:*?"<>| ]', '_', article['query'])
        filename = f"{filename}.html"
        path = os.path.join(self.output_dir, filename)
        with open(path, 'w') as file:
            file.write(article['html'])
        article["path"] = filename
        return article

    def run(self, article: dict):
        article = self.designer(article)
        return article
