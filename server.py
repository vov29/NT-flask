from flask import Flask, jsonify, request
app_flask = Flask("server")
ads = []
ads_id = 1
@app_flask.route("/ads", methods = ["POST"])
def create_ad():
    global ads_id
    a = request.json
    a["id"] = ads_id
    ads_id += 1
    return jsonify(a), 201
@app_flask.route("/ads", methods = ["GET"])
def get_ads():
    return jsonify(ads), 200
@app_flask.route("/ads/<int:id_ad>", methods = ["DELETE"])
def delete_ad(id_ad):
    global ads
    ads = [ad for ad in ads if ad["id"] != id_ad]
    return jsonify({"message":"Объявление ликвидировано"}), 200










app_flask.run()