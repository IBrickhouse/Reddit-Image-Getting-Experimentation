from RedditReader import Subreddit

image = Subreddit("Twicemedia")
image.get_random()
url = image.url
print(url)