from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

#@app.route('/<name>')
#def hello_name(name):
#    return f'Hello, {name}!'

#@app.route('/<name>')
#def rev_name(name):
#    new_name = name[::-1]
#    return f'Hello, {new_name}!'

@app.route('/<year>')
def year(year):
    generation = ''
    year = int(year)
    if year >= 1997 and year <2012 :
        generation = 'Gen Z'
    elif year >= 1981 and year <1997 :
        generation = 'Millenial'
    elif year >= 2012:
        generation = 'Gen Alpha'    
    else:
        generation = 'Gen X' 
    return {'year': year,
            'generation': generation}   

 
if __name__ == '__main__':
    app.run(debug=True,port=8080)
           