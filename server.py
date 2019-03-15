#/'/

from bottle import route, run, static_file, template, request
import granolapods
import time

@route('/', method=['GET','POST'])
def index():
	postdata = request.body.read()
	if len(postdata) > 0:
		pval = request.params.get('pval', type=float)
		fval = request.params.get('fval', type=float)
		cval = request.params.get('cval', type=float)
		granolapods.newRequestCallback(pval, fval, cval)
	return template('./htdocs/index.html')

@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='./htdocs/')
	
if __name__ == '__main__':
	run(host='0.0.0.0', reLoader=True, debug=True)
