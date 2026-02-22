from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "Guest")
    return render_template_string("<h1>Hello {{ name }}</h1>", name=name)

@app.after_request
def set_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
