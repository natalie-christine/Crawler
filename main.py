import crawler
import csv
   
fetcher = crawler.ArticleFetcher()
#articles = fetcher.fetch()

# for article in articles:
#     print("Title:", article.title)
#     print("Emoji:", article.emoji)
    # print("Content:", article.content)
    # print("Image URL:", article.image)
    # print("---")
    
with open ('crawler_output', 'w', newline= '', encoding='utf-8') as csvfile: 
    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)  
      
    counter = 0
    for article in fetcher.fetch():
        if counter == 10:
            break
        counter = counter +1
        print(article.emoji + ": " + article.title)
        articlewriter.writerow([article.emoji, article.title,article.content,article.image])
    
   
