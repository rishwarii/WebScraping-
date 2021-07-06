from os import closerange
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify)\
    # tags = soup.find('h5')  # finds the firsst instance
    courses_html_tag = soup.find_all('h5')
    # print(courses_html_tag)
    # for course in courses_html_tag:
    #     print(course.text)

    # all div tags have class as card

    course_cards = soup.find_all('div', class_='card')
    # remenber to add class_ as class is an inbuilt keyword in python
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        # print(course_name)
        # print(course_price)

        print(f'{course_name} costs {course_price}')

        # wwe can use split to get the last elemnt as its the only one we need : price
