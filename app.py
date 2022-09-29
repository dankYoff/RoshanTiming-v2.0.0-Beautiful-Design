from flask import Flask, render_template
import jinja2

app = Flask(__name__)
timer='12345'
@app.route('/')
def index():
    return render_template('index.html', timer=timer)

if __name__ == "__main__":
    app.run(debug=True)