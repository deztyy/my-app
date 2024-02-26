from flask import Flask, jsonify, request



app = Flask(__name__)

products = [{"id":1, "name":"Notebook Asus Vivo", "price":19900, "img":"https://img.advice.co.th/images_nas/pic_products4/A0147295/A0147295_s.jpg"}]


@app.route('/')
def welcome():
    return "<h1>Welcome to Products Management API</h1>"


@app.route('/products', methods=["GET"])
def get_products():
    return jsonify({"products": products})

@app.route('/products/<int:id>', methods=["GET"])
def get_prodct(id):
    prodct = next((p for p in products if p["id"]==id), None)
    if prodct:
        return jsonify({"products": products}), 200
    else:
        return jsonify({"error":"prodct not found"}), 404


@app.route('/products', methods=["POST"])
def post_products():
    data = request.get_json()
    p_id = next((p for p in products if p["id"] != data["id"]), None)
    if p_id:
        new_prd = {
            "id": data["id"],
            "name": data["name"],
            "price": data["price"],
            "img":data["img"]
        }
        products.append(new_prd)
        return jsonify(new_prd), 200
    else:
        return jsonify({"error":"Cannot create new prodct"}), 500

@app.route('/products/<int:id>', methods=["PUT"])
def put_products(id):
    prd = next((p for p in products if p["id"] == id), None)
    if prd:
        data = request.get_json()
        prd.update(data)
        return jsonify(prd), 200
    else:
        return jsonify( {"error":"prodct not found"}), 404

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_products(id):
    prd = next((p for p in products if p["id"] == id), None)
    if prd:
        products.remove(prd)
        return jsonify({"message":"prodct deleted successfully"}), 200
    else:
        return jsonify({"error": "prodct not found"}), 404

def run(host="127.0.0.1", port=80):
    app.run(host=host, port=port, debug=True)

if __name__ == '__main__':
    run()