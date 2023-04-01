from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)
application = app

# create a list of dicts from a CSV
swim_list = convert_to_dict("swim.csv")

# create a list of tuples in which the first item is the number
# (Rank) and the second item is the name (Athlete)
pairs_list = []
for s in swim_list:
    pairs_list.append( (s['Rank'], s['Athlete']) )

# first route

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Swimmers Index")

# second route

@app.route('/swimmers/<num>')
def detail(num):
    try:
        swim_dict = swim_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Athlete Rank: {num}</h1>"
    # a little bonus function, imported on line 2 above
    ord = make_ordinal( int(num) )
    return render_template('swimmer.html', swim=swim_dict, ord=ord, the_title=swim_dict['Athlete'])


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
