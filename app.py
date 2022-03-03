from selenium import webdriver


from pages.quotes_page import QuotesPage


#Load chrome from driver
'''
The chrome instance has the whole page info

-html 
-movements 
'''
chrome = webdriver.Chrome(executable_path = "/Users/gustavotamasco/chromedriver")
chrome.get("https://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

author = input("Enter the author you'd like quotes from: ")
page.select_author(author)

tags = page.get_available_tags()

tag = input("Select one of these tags-> [{}]: ".format(" | ".join(tags)))
page.select_tag(tag)

page.search_button.click()

print(page.quotes)
