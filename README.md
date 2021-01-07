# Away-From-DataScience
![](1500x500.jpeg)

Have you ever just run out of Data Science articles on Towards Data Science and went "oh dang, now what am I going to do?" Well have no fear, I've created [Away From Data Science](https://twitter.com/AFDataScience) for all your made up Data Science needs. 

This bot does it all:
- Posts fake article titles with made up authors every 30 minutes 
- Uses 3 random hashtags probably totally unrelated to the article
- Picks from out of a pool of 30 images and uploads them along with the article

The many thousands of tweets from Towards Data Science's [twitter account](https://twitter.com/TDataScience) were scraped with love by me using Twint. The tweets were then fed into the gpt-2-simple [colab notebook](https://colab.research.google.com/drive/1qxcQ2A1nNjFudAGN_mcMOnvV9sF_PkEb) written by Max Woolf. 

The 1000 subsequently generated tweets were curated down to 124 with their original "fake" authors taken off (I realized that some of the generated names were actual people who have written for TDS) and saved. After that it was a matter of generating a list of 50 fake names, saving 30 random images off of [Unsplash](https://unsplash.com/) and writing up the bot with Tweepy. 

The code is completely resuable, all you need is your own seperate lists of tweets, names, and hashtags along with a folder full of images. Make sure you change your random modules inside the code to match how many items you have for each to avoid index errors.  
