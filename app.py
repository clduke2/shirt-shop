from flask import Flask, render_template, request

app = Flask(__name__)

prices = {
    "short-sleeve": 5.0,
    "long-sleeve": 7.0,
    "oxford-fabric": 5.0,
    "poplin": 6.0,
    "flannel": 7.0,
    "fine-cotton": 9.0,
    "small": 5.0,
    "medium": 6.5,
    "large": 8.0,
    "xl": 9.5,
    "2xl": 11.0,
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        cut = request.form["cut"]
        fabric = request.form["fabric"]
        color = request.form["color"]
        size = request.form["size"]

        total = prices[cut] + prices[fabric] + prices[size]

        total_string = f"${total:.2f}"

        return f"<p>Here are your shirt details: <br>{cut}, {fabric}, {color}, {size}<br><br>Your total will be {total_string}. Have a nice day!</p>"
        
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8080)