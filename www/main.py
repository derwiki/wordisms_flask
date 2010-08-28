from flask import Flask
app = Flask(__name__)
import time
from _debug import _render_template

@app.route('/hello/')
@app.route('/hello/<debug>')
def hello(debug=None):
	print "entering servlet"
	context = dict(
		name="Adam Derewecki",
		time_rendered=time.time(),
	)

	return _render_template('hello.html', debug, **context)




if __name__ == "__main__":
	app.run(debug=True)
