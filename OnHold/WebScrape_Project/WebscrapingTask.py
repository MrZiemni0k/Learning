# **TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. 
# Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. 
# For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that 
#is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!**



page_on = True
numpage = 1
authors = set()
while page_on:

    # Chck page number
    
    print(numpage)
    
    # Cnnt to website/page and convert text into readable state. 
    
    cnnt_to_web = requests.get(f"http://quotes.toscrape.com/page/{numpage}/")
    soup = bs4.BeautifulSoup(cnnt_to_web.text, "lxml")
    
    # Chck if a loaded page is empty. For empty page exit the loop. 
    # For a page with a content get set of authors and add page number to continue with the loop.
    
    if len([author for author in soup.select(".author")]) == 0:
        page_on = False
    else:
        for author in soup.select(".author"):
            authors.add(author.text)
    numpage += 1
    
authors
