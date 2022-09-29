from flask import Flask, render_template
from random import randint

app = Flask(__name__)

# RANDOM TIMER IN GAME
a = randint(10, 50)
if a <= 9:
    aa = str('0' + str(a))
else:
    aa = str(str(a))
b = randint(0, 59)
if b <= 9:
    bb = str('0' + str(b))
else:
    bb = str(str(b))
timer = str(aa + ':' + bb)

@app.route('/')
def index():
    return render_template('index.html', timer=timer)

if __name__ == "__main__":
    app.run(debug=True)