### Part 1: Setting up

## 1.1. Pre-requisites 
duration: 1 mins (should already be installed)

Python 3.6.2
Pip
Code editor of choice
Git
Chrome or Firefox 

## 1.2. Teams
duration: 10 mins

## 1.3. Getting the code
duration: 5 mins
Clone the repo
Docs folder
Follow instructions.md as we go

git clone https://olivif@bitbucket.org/olivif/avworkshop.git

## 1.4. Running the code
duration: 5 mins
Follow setup.md to install python packages
Run the server

python manage.py runserver

Ignore the warning about migrations
Navigate to http://127.0.0.1:8000/ 


### Part 2: Name your app
duration: 5 mins

### Part 3: Let's get some movie data

## 3.1. Get top 250 movie data from IMDB
duration: 15 mins

models.py 
imdb_api.py
Fill in get_top_250_movies
Fetch the data from IMDB using imdbpie
Iterate through the data and convert to Movie model objects

https://github.com/richardasaurus/imdb-pie
http://jsonviewer.stack.hu/

## 3.2. Even more movie data
duration: 10 mins

imdb_api.py
Fill in 
get_popular_movies
get_popular_shows

### Part 4: Player
duration: 2 mins

Click on one of the movies

## 4.1. Build a simple player with the test data
duration: 7 mins

player.html
Add a video element inside <!-- Video player -->
Use movie.trailer_url for the video source

## 4.2. Build a streaming player
duration: 5 mins

Use the manifest instead of the video 
Use data-dashjs-player attribute on the video element

http://amssamples.streaming.mediaservices.windows.net/683f7e47-bd83-4427-b0a3-26a6c4547782/BigBuckBunny.ism/manifest(format=mpd-time-csf)

## 4.3. Play the video and observe network traffic
duration: 7 mins

Open the browser developer tools console – network tab
Hit play on the video with the manifest
Look at the traffic
What do you think is happening?
What did you notice about the network traffic?



