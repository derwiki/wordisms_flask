from flask import Flask
app = Flask(__name__)
import simplejson
from flask import render_template

def _render_template(template_name, debug, **context):
	if debug == "debug":
		return simplejson.dumps(dict(context=context, template_name=template_name))
	else:
		return render_template(template_name, **context)

