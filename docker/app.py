from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def index():
    resindex = '''
    <h1> Flask Calculator </h1>
    <hr>
    For addition, use %saddition/x/y <br>
    For subtraction, use %ssubtraction/x/y <br>
    For multiplication, use %smultiplication/x/y <br>
    For division, use %sdivision/x/y <br>

    where x and y are the integer parameters.

    ''' % (request.base_url, request.base_url, request.base_url, request.base_url)
    return resindex

@app.route("/hello")
def hello():
    return request.base_url

@app.route('/addition/', defaults={'x': None, 'y': None})
@app.route('/addition/<x>/', defaults={'y': None})
@app.route("/addition/<x>/<y>/")
def getAddition(x, y):
    # if x is None or y is None:
    #    return "Both arguments x and y are required as integers. Request in the form %saddition/x/y"
    try:
        return x + ' + ' + y + ' = ' + str(int(x)+int(y))
    except:
        return "Both arguments x and y are required as integers. Request in the form %saddition/x/y" % (request.url_root)

@app.route('/subtraction/', defaults={'x': None, 'y': None})
@app.route('/subtraction/<x>/', defaults={'y': None})
@app.route("/subtraction/<x>/<y>/")
def getSubtraction(x, y):
    # if x is None or y is None:
    #    return "Both arguments x and y are required as integers. Request in the form %saddition/x/y"
    try:
        return x + ' - ' + y + ' = ' + str(int(x)-int(y))
    except:
        return "Both arguments x and y are required as integers. Request in the form %ssubtraction/x/y"  % (request.url_root)

@app.route('/multiplication/', defaults={'x': None, 'y': None})
@app.route('/multiplication/<x>/', defaults={'y': None})
@app.route("/multiplication/<x>/<y>/")
def getMultiplication(x, y):
    # if x is None or y is None:
    #    return "Both arguments x and y are required as integers. Request in the form %saddition/x/y"
    try:
        return x + ' * ' + y + ' = ' + str(int(x)*int(y))
    except:
        return "Both arguments x and y are required as integers. Request in the form %smultiplication/x/y" % (request.url_root)

@app.route('/division/', defaults={'x': None, 'y': None})
@app.route('/division/<x>/', defaults={'y': None})
@app.route("/division/<x>/<y>/")
def getDivision(x, y):
    # if x is None or y is None:
    #    return "Both arguments x and y are required as integers. Request in the form %saddition/x/y"
    try:
        return x + ' / ' + y + ' = ' + str(int(x)/int(y))
    except:
        return "Both arguments x and y are required as integers and y cannot be zero. Request in the form %sdivision/x/y" % (request.url_root)

if __name__ == "__main__":
    app.run()
    