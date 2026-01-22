#!/usr/bin/env python3

from flask import Flask

contracts = [
    {
        "id": 1,
        "contract_information": "This contract is for John and building a shed",
    },
    {
        "id": 2,
        "contract_information": "This contract is for a deck for a buisiness",
    },
    {
        "id": 3,
        "contract_information": "This contract is to confirm ownership of this car",
    },
]
customers = ["bob", "bill", "john", "sarah"]
app = Flask(__name__)


@app.route("/contract/<id>")
def get_contract(id):
    contract = next(
        (contract for contract in contracts if contract["id"] == int(id)), None
    )
    if contract is None:
        return {"error": f"Contract {id} not found"}, 404

    return contract["contract_information"], 200


@app.route("/customer/<name>")
def get_customer(name):
    customer = next(
        (customer for customer in customers if customer == name), None
    )
    if customer is None:
        return {"error": f"Customer '{name}' not found."}, 404

    return "", 204


if __name__ == "__main__":
    app.run(port=5555, debug=True)
