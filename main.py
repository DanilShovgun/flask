from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

ads = []

@app.route('/ads', methods=['GET', 'POST'])
def handle_ads():
  if request.method == 'POST':
    new_ad = request.get_json()
    new_ad['id'] = len(ads) + 1
    new_ad['date'] = datetime.now()
    ads.append(new_ad)
    return jsonify(new_ad), 201  
  elif request.method == 'GET':
    return jsonify(ads)

@app.route('/ads/<int:ad_id>', methods=['DELETE'])
def handle_ad_delete(ad_id):
  for ad in ads:
    if ad['id'] == ad_id:
      ads.remove(ad)
      return jsonify({'message': f'ad {ad_id} has been deleted.'})
  
  return jsonify({'error': 'ad not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
