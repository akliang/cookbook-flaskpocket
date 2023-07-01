from flask import Flask, request
import requests
import const
import helpers as h

app = Flask(__name__)


@app.route("/login", methods=["post"])
def login():
    data = request.json
    res = requests.post(const.LOGIN_URL, json=data)
    return h.format_response(res)

@app.route("/view/<id>", methods=["get"])
def view(id):
    res = requests.get(const.RECIPE_URL + id)
    return h.format_response(res)

@app.route("/list/<chef>", methods=["get"])
def list(chef):
    res = requests.get(const.RECIPE_URL + f"?filter=(chef='{chef}')")
    return h.format_response(res)

@app.route("/add", methods=["post"])
def add():
    headers = request.headers
    data = request.json
    res = requests.post(const.RECIPE_URL, headers=headers, json=data)
    return h.format_response(res)

@app.route("/edit/<id>", methods=["patch"])
def edit(id):
    headers = request.headers
    data = request.json
    res = requests.patch(const.RECIPE_URL + id, headers=headers, json=data)
    return h.format_response(res)

# TODO: this returns b'' and status code 204, but is technically silent
@app.route("/delete/<id>", methods=["delete"])
def delete(id):
    headers = request.headers
    res = requests.delete(const.RECIPE_URL + id, headers=headers)
    print(h.format_response(res), flush=True)
    return h.format_response(res)


if __name__ == '__main__':
    # TODO: turn off debug
    app.run(debug=True, host='0.0.0.0')