from flask import Flask, render_template, request, redirect, url_for, jsonify

import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    movie_name = request.form.get('movie_name')
    quality = request.form.getlist('quality')
    website = request.form.getlist('website')
    category = request.form.get('category')

    print(f"Arama: {movie_name}, Kalite: {quality}, Site: {website}, Kategori: {category}")
    
    # 1-20 arasında mock veri üretme
    mock_data = []
    num_results = random.randint(1, 20)  # 1 ile 20 arasında sonuç üretecek
    for i in range(1, num_results + 1):
        mock_data.append({
            'torrent_name': f"Mock Movie {i}",
            'magnet_url': f"magnet:?xt=urn:btih:mockhash{i:05}"
        })

    # Sonuçları JSON olarak geri döndürüyoruz
    return jsonify({'results': mock_data})

@app.route('/downloaded/<torrent_name>/<magnet_url>')
def downloaded(torrent_name, magnet_url):
    return render_template('downloaded.html', torrent_name=torrent_name, magnet_url=magnet_url)


if __name__ == '__main__':
    app.run(debug=True)
