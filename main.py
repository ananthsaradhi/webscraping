from bs4 import BeautifulSoup
import requests
import time

    # with open('home.html' ,'r') as html_file:
    #     content = html_file.read()
    #
    #     soup = BeautifulSoup(content, 'lxml')
    #
    # course_cards =soup.find_all('div',class_='card')
    #
    # for course in course_cards:
    #     course_name = course.h5.text
    #     course_price = course.a.text.split()[-1]
    #     print(f'{course_name} costs {course_price}')

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    location = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    html_text = requests.get(location).text
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text.replace(' ', '')
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} ")
                    f.write(f"Required Skills: {skills.strip()} ")
                    f.write(f'More Info: {more_info} ')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
