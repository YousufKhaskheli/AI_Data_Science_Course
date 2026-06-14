from fastapi import FastAPI

app = FastAPI()

data = [{'roll':120,'name':'Asad','course':'python'},
        {'roll':122,'name':'Farman','course':'Data Science'},
        {'roll':128,'name':'Shan','course':'AI'}]


@app.get("/")
def home():
    return "Welcome to my Learning Portal! I am a first year student studying AI and Data Science at TITAN"

@app.get("/add")
def add(a:int, b:int):

    return {'Num_a':a,
            'Num_b':b,
            'Addition':a+b}

@app.get("/sub")
def sub(a:int,b:int):
    return {'Num_a':a,
            'Num_b':b,
            "Subtraction":a-b}

@app.get("/multiply")
def multiplication(a:int,b:int):
    return {'Num_a':a,
            'Num_b':b,
            'Multiplication':a*b}

@app.get("/div")
def division(a:int,b:int):
    return {'Num_a':a,
            'Num_b':b,
            'Division':a/b}

@app.get("/show_data")
def show_data():
    return {"data":data}

@app.get("/only_data")
def only_data():
    return data

@app.get("/show_data/1")
def show_data_1():
    return data[0]

@app.get("/show_data/2")
def show_data_2():
    return data[1]

@app.get("/show_data/3")
def show_data_3():
    return data[2]