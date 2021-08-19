import requests
from bs4 import BeautifulSoup
import time
import datetime
print('What are you not familiar with ?')
unfamiliar_skill = input('>')
#x = [str(x) for x in input("Enter multiple value: ").split()]
print(f'Filtering out {unfamiliar_skill}')

urljob = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='


def find_jobs():
    html_text = requests.get(urljob).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find(
            'span', class_='sim-posted').span.text.replace(' ', '')
        if 'few' in published_date:
            company_name = job.find(
                'h3',  class_='joblist-comp-name').text.replace(' ', '')

            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            print("Run Date and Time ")
            now = datetime.datetime.now()
            if unfamiliar_skill not in skills:
                with open(f'/Users/rishwari/Documents/Web Scraping/PythonJobScraping/posts/{index}.txt', 'w') as f:
                    f.write("------------------\n")
                    f.write(now.strftime("% Y-%m-%d % H: % M: % S \n"))
                    f.write(f"Company Name : {company_name.strip()}\n")
                    f.write(f"Skills: {skills.strip()}\n")
                    f.write(f"More Info : {more_info}\n")
                    f.write("------------------\n")

                print(f'File Saved as {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1000
        #print(f'Wait time is currently {time_wait} minutes ......')
        #time.sleep(time_wait * 60)

# Date Posted: {published_date}
# Execute with filter
#  Prettifying the Jobs paragraphc
# 1.Jobs Filtration by owned skillssql

# 2.Setting up the Project to scrape every 10 minutes
# 3.Storing the jobs paragraph in text files
