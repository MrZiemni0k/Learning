Written by Marcin "MrZiemni0k".

My 1st WebScraping Project. Still needs some improvement but at least it works. Planning to add:

Interactions between an user and the script:
Check for dead hosts by .netloc?
Delete .netlock urls?
Store timed out urls?
Directory input?
Minimum size of the pictures to be downloaded?
Compress code into nicer version. Add classes.
Make nested dictionary: {Sub page:{Thread:Urls}} for smoother interaction with an user. For example to let's say to avoid sub pages that are not interesting for us.
Adjust url patterns for web-crawlers.





A script is towards common public forum which is 3-page deep(Main Page, Sub Page(Categories) and Threads with a content we are looking for. My script's main goal is to download all images(with some adjustments) from urls hidden within bbcode.

My target was a medium size japanese archive forum (12years of content). It took around 2 days to webscrape urls (Could be done faster depending on set value of time.sleep()) and 4 days to download all images after some sorting and cleaning - Many hosts were slow or dead etc.