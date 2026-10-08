from flask import Flask, render_template, request

app = Flask(__name__)

suspects = {
    "alex": {
        "name": "Alex",
        "role": "Sports Captain",
        "statement": "I was on the playground during the lunch break.",
        "clue": "A student saw Alex near the sports room.",
    },
    "riya": {
        "name": "Riya",
        "role": "Class Representative",
        "statement": "I was in the library reading a book.",
        "clue": "The librarian confirms that Riya was in the library.",
    },
    "rahul": {
        "name": "Rahul",
        "role": "Sports Assistant",
        "statement": "I was helping the teacher in the staff room.",
        "clue": "Rahul had access to the trophy cabinet.",
    },
    "meera": {
        "name": "Meera",
        "role": "Event Coordinator",
        "statement": "I was preparing decorations in the auditorium.",
        "clue": "A decoration box was found near the trophy room.",
    },
}

thief = "rahul"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/suspects")
def show_suspects():
    return render_template("suspects.html", suspects=suspects)


@app.route("/interview/<suspect>")
def interview(suspect):
    if suspect not in suspects:
        return "404 - Suspect not found. The detective could not locate that suspect.", 404
    selected_suspect = suspects[suspect]
    return render_template("interview.html", suspect=selected_suspect, suspect_key=suspect)


@app.route("/clues")
def clues():
    evidence = [
        {
            "title": "Clue #1",
            "detail": "The trophy cabinet was opened using a staff key.",
        },
        {
            "title": "Clue #2",
            "detail": "The key was normally kept with the sports staff.",
        },
        {
            "title": "Clue #3",
            "detail": "A witness saw someone leaving the sports room shortly before the trophy disappeared.",
        },
        {
            "title": "Clue #4",
            "detail": "One suspect had direct access to the trophy cabinet.",
        },
    ]
    return render_template("clues.html", evidence=evidence)


@app.route("/accuse", methods=["GET", "POST"])
def accuse():
    if request.method == "POST":
        selected_suspect = request.form.get("suspect")

        if not selected_suspect or selected_suspect not in suspects:
            return render_template(
                "accusation.html",
                suspects=suspects,
                error="Please select a suspect before submitting your accusation.",
            )

        is_correct = selected_suspect == thief
        selected_name = suspects[selected_suspect]["name"]
        thief_name = suspects[thief]["name"]

        return render_template(
            "result.html",
            selected_suspect=selected_suspect,
            selected_name=selected_name,
            thief_name=thief_name,
            thief=thief,
            is_correct=is_correct,
        )

    return render_template("accusation.html", suspects=suspects)


if __name__ == "__main__":
    app.run(debug=True)
