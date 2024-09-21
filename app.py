from flask import Flask, render_template, request, redirect, url_for, jsonify

import sys
sys.path.append("AutoTorrent")

from AutoTorrent.auto_torrent import AutoTorrent

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
    
    auto_torrent = AutoTorrent()
    result = auto_torrent.defaultStart(input=movie_name, qualities=["1080P","720P"])

    results = []

    for torrent in result:
        results.append({
            'torrent_name': f" {torrent.title} {torrent.year} {torrent.quality_size}",
            'magnet_url': f"{torrent.magnet_url}"
        })
        
    # Sonuçları JSON olarak geri döndürüyoruz
    return jsonify({'results': results})

@app.route('/downloaded/<torrent_name>/<magnet_url>')
def downloaded(torrent_name, magnet_url):
    return render_template('downloaded.html', torrent_name=torrent_name, magnet_url=magnet_url)


if __name__ == '__main__':
    app.run(debug=True)
