from flask import Flask, render_template, request, redirect, url_for
from recommend import recommend_article

app = Flask(__name__)

# flask automatically looks into the templates folder :) fuck


@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    recommendations = []

    if request.method == "POST":
        query = request.form["query"].strip()  # this will strip whitespaces
        print(query, type(query))

        if not query:
            error = "Please enter the search article here !"

        elif len(query) < 5:
            error = "The article length must be greater than 5. "

        else:
            recommendations = recommend_article(query)
            print(f"recommendations are : ", recommendations)

    return render_template("index.html", recommendations=recommendations, error=error)


if __name__ == "__main__":
    app.run(debug=True)
