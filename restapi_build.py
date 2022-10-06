from flask import Flask, jsonify, request
import random
import json

app = Flask(__name__)
jsonfile = 'Data.json'

structure = {
    "name": str,
    "email": str,
    "username": str,
}

def input_validation(new_data):
    given_data = True
    for y, z in new_data.items():
        if y in structure:
            if type(new_data[y]) == structure[y]:
                print("all good")
            else:
                print("ERROR")
                given_data = False
                break
        else:
            print("Incorrect data given")
            given_data = False
            break
    return(given_data)

# Home
@app.route('/')
def hello_world():
   return 'Hello World'

# List or Create api
@app.route('/users', methods=['GET', 'POST'])
def list_create():
    if request.method == 'GET':
        with open(jsonfile) as f:
            data = json.loads(f.read())
        return jsonify(data)
    elif request.method == 'POST':
        id = random.randint(1000, 9999)
        new_data = request.json

        if input_validation(new_data) == True:
            new_data.update({"id": id})
            with open(jsonfile) as f:
                data = json.loads(f.read())
            data.append(new_data)
            with open(jsonfile, "w") as f:
                json.dump(data, f)
            return jsonify(new_data)
        else:
            return jsonify("ERROR: Can't create api, incorrect data given")


# get api
@app.route('/users/<int:id>', methods=['GET'])
def get_id(id):
    with open(jsonfile) as f:
        data = json.loads(f.read())
    for data_dict in data:
        if id == data_dict['id']:
            return jsonify(data_dict)
    return "Not found"

# update api
@app.route('/users/<int:id>', methods = ['PUT'])
def update(id):
    with open(jsonfile) as f:
        data = json.loads(f.read())
    for data_dict in data:
        if id == data_dict['id']:
            new_data = request.json
            if input_validation(new_data)== True:
                data_dict.update(new_data)
                with open(jsonfile, "w") as f:
                    json.dump(data, f)
                return jsonify(data_dict)
            else:
                return jsonify("ERROR: Can't create api, incorrect data given")
    return "Not found"

# delete api
@app.route('/users/<int:id>', methods = ['DELETE'])
def delete(id):
    with open(jsonfile) as f:
        data = json.loads(f.read())
    data_found = False
    for data_dict in data:
        if id == data_dict['id']:
            data_found = True
            break
    if data_found:
        data.remove(data_dict)
        with open(jsonfile, "w") as f:
            json.dump(data, f)
        return "Deleted"
    else:
        return "Not found"

if __name__ == '__main__':
    app.run(debug=True)
