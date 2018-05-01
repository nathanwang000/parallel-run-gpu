from flask import Flask
from flask import request, url_for, render_template, flash, redirect
from src.parallel_run import ProcessManager
import time

app = Flask(__name__)   
PM = ProcessManager()

##### test function #####
C = 0

def long_task(i):
    time.sleep(5)
    return i

def callback(res):
    print('result ready')
    global C
    C = res

@app.route('/favicon.ico')
def favicon():
    return "favicon"

@app.route('/update_C', methods=['POST'])
def update_C():
    print('>> updating C')
    PM._terminateAll()
    PM.add(target=long_task, args=(-(abs(C)+1), ))
    print(abs(C)+1)    
    PM.run(callback)
    
    return str(C)
### test function done####
    
@app.route('/')
def index():
    return render_template("index.html", progress=PM.progress(), C=C)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, port=5007)    
