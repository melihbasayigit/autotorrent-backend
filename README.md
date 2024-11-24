# Auto Torrent Web

![Logo](#) Coming Soon

Auto Torrent is a torrent scraper and downloader. The Auto Torrent Web version is a full-stack web application that automatically searches and adds torrents. The Auto Torrent Web version is powered by Docker.

## Requirments

- Python
- AutoTorrent Module
- Qbittorrent Web UI
- Plex

## Installation

If you have already install all requirments above,

Also there is dockerfile for containers. Build and Use it.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file (in torrent module)

`QB_USERNAME`

`QB_PASSWORD`

`QB_WEB_UI`

**NOTE** and also you need to add your paths to category_type.py correctly. I will fix that soon. 

Example of .env file:
```env
QB_USERNAME=admin
QB_PASSWORD=123456
QB_WEB_UI=http://127.0.0.1:9000
```


## FAQ

#### EnvError: Please provide QB_USERNAME, QB_PASSWORD, and QB_WEB_UI in the .env file.

You need to check your .env file is correct. There is an example [.env](#usage) file

#### Where is my downloaded files.

I will fix savepath soon. You find all paths in category_type.py

## Upcoming Features

- Admin Panel
- Add Movie Information and Poster in Frontend

## Related

[AutoTorrent](https://github.com/melihbasayigit/AutoTorrent) Module

## Web Images

![ss_1](/doc/sc1.PNG)

![ss_2](/doc/sc2.PNG)

![ss_3](/doc/sc3.PNG)