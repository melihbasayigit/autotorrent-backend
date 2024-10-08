from flask import Flask, render_template, request, redirect, url_for, jsonify

import sys
sys.path.append("AutoTorrent")

from AutoTorrent.auto_torrent import AutoTorrent
from AutoTorrent.torrent.torrent_manager import TorrentManager
from AutoTorrent.auto_torrent import CategoryType

app = Flask(__name__)

# Global manager variables
auto_torrent = AutoTorrent()
torrent_manager = TorrentManager()

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
    
    if not quality:
        quality=["1080P","720P"]

    quality = ["2160P" if q == "4K" else q for q in quality]

    result = auto_torrent.defaultStart(input=movie_name, qualities=quality)

    results = []

    for torrent in result:
        results.append({
            'torrent_name': f" {torrent.title} {torrent.year} {torrent.quality_size}",
            'magnet_url': torrent.magnet_url,
            'category' : category
        })
        
    # Sonuçları JSON olarak geri döndürüyoruz
    return jsonify({'results': results})

@app.route('/downloaded/<category>/<torrent_name>/<magnet_url>')
def downloaded(torrent_name, magnet_url, category):

    category_type = None
    category = category.upper()
    # Enuma dönüştürme
    if category == "ANIME":
        category_type = CategoryType.ANIME
    elif category == "MOVIE":
        category_type = CategoryType.MOVIE
    elif category == "TV SERIES":
        category_type = CategoryType.TV_SERIES
    else:
        print('Invalid Category Type')
        
    print(category_type)

    result = torrent_manager.insert_torrent(magnet_link=magnet_url, category_type=category_type)
    print(result)
    return render_template('downloaded.html', torrent_name=torrent_name, magnet_url=magnet_url, category=category)


if __name__ == '__main__':
    app.run(debug=True)
