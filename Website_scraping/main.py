from bs4 import BeautifulSoup
import requests
import csv

base_url = 'https://news.tirumala.org/category/darshan/page/{}/'
with open('darsan_pilgrim_data.csv',mode='w',newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Date','Number of People'])
    for page in range(1,155):    
        url = base_url.format(page)
    
        response = requests.get(url, verify=False)  # Disable SSL verification it is not recommended for the production
        soup = BeautifulSoup(response.text,'lxml')
        jobs = soup.find_all('h2',class_ = 'post-title entry-title')
        for job in jobs:
            j = job.text
            # print(j)
            date = j[34:44]
            number_of_p = j[46:]
        
            writer.writerow([date,number_of_p])
            print(date)
            print(number_of_p)
            #print(job)
