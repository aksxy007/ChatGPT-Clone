from flask import Flask, render_template,jsonify,request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/api", methods=["GET","POST"])
def qa():
    if request.method=="POST":
        data={"result":"Thank you for the kind words! I'm glad you find ChatGPT awesome. If you have any questions or need assistance with anything, feel free to ask!"}
        return jsonify(data)
    data={"result":"Thank you for the kind words! I'm glad you find ChatGPT awesome. If you have any questions or need assistance with anything, feel free to ask!"}
    return jsonify(data)


app.run(debug = True)

