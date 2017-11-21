from lxml import html
import requests, sys
from bs4 import BeautifulSoup
from requests.exceptions import SSLError
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://projecteuler.net/problem='

upper_limit = 603

counter = 1

try:
    file = open('Project-Euler-Questions.txt','w')
except IOError:
    print ('Problem with opening the file')
    sys.exit(1)

while counter <= upper_limit:
    try:
        page = requests.get(url + str(counter))
        #print (page.content)
        tree = html.fromstring(page.content)
        bs = BeautifulSoup(page.content,"lxml")
        mydivs = bs.findAll("div", { "class" : "problem_content" })
        problem_content = mydivs[0].get_text()
        print (problem_content)
        file.write(str('Question ') + str(counter) + ':')
        file.write(str(problem_content).encode('utf-8'))
        file.write(str("================="))
        print ("========================")
        counter += 1
    except SSLError as e:
        print (e)

file.close()

