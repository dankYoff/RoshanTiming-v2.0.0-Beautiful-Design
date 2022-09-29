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

# AEGIS TIMER
aegis_a = a + 5
if aegis_a <= 9:
    aegis_a = str('0' + str(aegis_a))
else:
    aegis_a = str(aegis_a)
b = randint(0, 59)

# MIN TIMER ROSHAN
int_min_rosh = a + 8

# MAX TIMER ROSHAN
int_max_rosh = a + 11

# Enter Aegis, min or max + Check
c = 1
d = str(str(aegis_a) + bb + ' ' + str(int_min_rosh) + bb + '-' + str(int_max_rosh) + bb)

@app.route('/')
def index():
    return render_template('index.html', timer=timer, d=d)

if __name__ == "__main__":
    app.run(debug=True)