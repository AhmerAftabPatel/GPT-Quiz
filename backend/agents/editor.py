import os

article_templates = {
    "layout_1.html": """
    <div class="question_paper">
        <h2>{{question}}</h2>
        <input type="radio" value="{{options[0]}}">{{options[0]}}</input>
        <input type="radio" value="{{options[1]}}">{{options[1]}}</input>
        <input type="radio" value="{{options[2]}}">{{options[2]}}</input>
        <input type="radio" value="{{options[3]}}">{{options[3]}}</input>
    </div>
    """,
    "layout_2.html": """
    <div class="article">
        <img src="{{image}}" alt="Article Image">
        <div>
            <a href="{{path}}" target="_blank"><h2>{{title}}</h2></a>
            <p>{{summary}}</p>
        </div>
    </div>
    """,
    "layout_3.html": """
    <div class="article">
        <a href="{{path}}" target="_blank"><h2>{{title}}</h2></a>
        <img src="{{image}}" alt="Article Image">
        <p>{{summary}}</p>
    </div>
    """,
}

class EditorAgent:
    def __init__(self, layout):
        self.layout = layout

    def load_html_template(self):
        template_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'quiz', 'layouts', self.layout)
        with open(template_path) as f:
            return f.read()

    def editor(self, articles):
        html_template = self.load_html_template()

        # Article template
        article_template = article_templates[self.layout]

        # Generate articles HTML
        articles_html = ""
        for article in articles:
            article_html = article_template.replace("{{question}}", article["question"])
            article_html = article_html.replace("{{image}}", article["image"])
            article_html = article_html.replace("{{options[0]}}", article["options"][0])
            article_html = article_html.replace("{{options[1]}}", article["options"][1])
            article_html = article_html.replace("{{options[2]}}", article["options"][2])
            article_html = article_html.replace("{{options[3]}}", article["options"][3])
            article_html = article_html.replace("{{path}}", article["path"])
            articles_html += article_html

        # Replace placeholders in template
        html_template = html_template.replace("{{date}}", articles[0]["date"])
        newspaper_html = html_template.replace("{{articles}}", articles_html)
        return newspaper_html

    def run(self, articles):
        res = self.editor(articles)
        return res
