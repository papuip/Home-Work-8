import time

import requests
from bs4 import BeautifulSoup
#unfemiliar_skill=input('>')
def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        posted = job.find('span', class_='sim-posted').span.text
        if 'few' in posted:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace('  ','')
            skills=job.find('span',class_='srp-skills').text.replace('  ','')
            more_info=job.header.h2.a['href']
            #print(f"company name is {company_name} and required skills are {skills} its posted {posted}")
            if unfemiliar_skill not in skills:
                with open(f'jobs/{index}.txt','w') as f:
                    f.write(f"Company name:{company_name.strip()}\n")
                    f.write(f"Required skills:{skills.strip()}\n")
                    f.write(f"more info: {more_info}\n")
                print(f'file saved{index}')
if __name__=="__main__":
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)