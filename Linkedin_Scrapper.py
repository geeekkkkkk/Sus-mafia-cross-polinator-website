from selenium import webdriver
from bs4 import BeautifulSoup
import time
import webbrowser
import requests

# Creating a webdriver instance
driver = webdriver.Chrome("C:\\Users\\LENOVO\\Downloads\\chromedriver")
driver.get("https://linkedin.com/uas/login")

email = "codefourgoodteam22@gmail.com"
password = "Backtracking22"

username = driver.find_element_by_id("username")

username.send_keys(email)

pword = driver.find_element_by_id("password")

pword.send_keys(password)		

driver.find_element_by_xpath("//button[@type='submit']").click()

#Keyword search bar input
keyword = 'Waste management'
keyword = keyword.replace(' ','%20')

url = "https://www.linkedin.com/search/results/all/?keywords="

profile_url = url+keyword

driver.get(profile_url) 

start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
	driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
	initialScroll = finalScroll
	finalScroll += 1000

	time.sleep(3)

	end = time.time()

	if round(end - start) > 20:
		break

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

reusablecontainer =  soup.find_all("span", {'class' : "entity-result__title-text"})

c = 'company'
g = 'groups'

c_link = []
g_link = []
for cont in reusablecontainer:
    names = cont.find('a')['href']
    if c in names:
        c_link.append(names)
    if g in names:
        g_link.append(names)

intro = soup.find('div', {'class': 'search-results-container'})

intro = str(intro)

'''
f=open('C:\\Users\\LENOVO\\Downloads\\test.html','w')
f.write(intro)
f.close()
filename='C:\\Users\\LENOVO\\Downloads\\test.html'
webbrowser.open_new_tab(filename)'''

import html2text
h = html2text.HTML2Text()

h.ignore_links = True
h.ignore_images = True
print(h.handle("<p>Hello, <a href='https://www.google.com/earth/'>world</a>!"))
'''f=open('C:\\Users\\LENOVO\\Downloads\\test.html','r')
data = f.read()
f.close()'''
data = intro
data = h.handle(data)
data = data.replace('**',' ')
data = data.replace('*',' ')
data = data.split()

flag = 0
comp_data = ''
for i in data:
    if i=='Companies':
        flag = 1
        continue
    if flag==1 and i!='See' and i!=None:
        comp_data += i + ' '
    if i=='See':
        flag = 0
    
company_list = []
temp_s = ''
for i in comp_data.split():
    if i=='Follow':
        company_list.append(temp_s)
        temp_s = ''
        continue
    temp_s = temp_s + ' '
    temp_s += i

flag = 0
comp_data = ''
for i in data:
    if i=='Jobs':
        flag = 1
        continue
    if flag==1 and i!='See' and i!=None:
        comp_data += i + ' '
    if i=='See':
        flag = 0
    
job_list = []
temp_s = ''
for i in comp_data.split():
    if i=='Save':
        job_list.append(temp_s)
        temp_s = ''
        continue
    temp_s = temp_s + ' '
    temp_s += i

flag = 0
comp_data = ''
for i in data:
    if i=='Groups':
        flag = 1
        continue
    if flag==1 and i!='See' and i!=None:
        comp_data += i + ' '
    if i=='See':
        flag = 0
    
group_list = []
temp_s = ''
for i in comp_data.split():
    temp_s = temp_s + ' '
    temp_s += i
    #if i=='members':
    group_list.append(temp_s)
    temp_s = ''
    
temp = []
sen = ''
for i in range(len(group_list)-1):
    if '.' in group_list[i-1]:
        temp.append(sen)
        sen = ''
    sen = sen + ' '
    sen = sen + group_list[i]

ret_s = ''

num = []

for i in range(len(temp)-1):
    if 'members ' in temp[i]:
        ret_s = ret_s + temp[i-1] + temp[i] + temp[i+1]
        num.append(ret_s)
        ret_s = ''


# Company list consists the data about the companies 
print(len(company_list))
for i in company_list:
    print('-->',i,'\n')

# Job list consists the data about the Jobs     
print(len(job_list))
for i in job_list:
    print('-->',i,'\n')

#Num contains the data about the group data
print(len(num))
for i in num:
    print('-->',i,'\n')
    
company_data = []
group_data = []

for i in range(3):
    temp1 = [company_list[i],c_link[i]]
    temp2 = [num[i],g_link[i]]   
    company_data.append(temp1)
    group_data.append(temp2)
#company data is a list of list which contains description as well as website links
print(company_data)
#Group data is a list of list which contains description as well as website links
print(group_data)