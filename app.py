from flask import Flask, request, jsonify, make_response


app = Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    """ Method for calculating customer color"""
    if request.method == 'POST':
        salary = request.json['salary']
        expenses = request.json['expenses']
        remainder_range = int(salary) - int(expenses)

        if remainder_range > 7000:
            color_range = {"color": "#2FD0F3", "remainder": remainder_range}
        elif remainder_range > 3000 and remainder_range <= 7000:
            color_range = {"color": "#3FE449", "remainder": remainder_range}
        elif remainder_range > 1000 and remainder_range <= 3000:
            color_range = {"color": "#FCFC59", "remainder": remainder_range}
        elif remainder_range <= 1000:
            color_range = {"color": "#C7162B", "remainder": remainder_range}

        return make_response(jsonify(color_range), 200)
    else:
        deatils = {
            "message": "Method not exist",
        }
        return make_response(jsonify(deatils), 404)


if __name__ == "__main__":
    app.run(debug=True)
