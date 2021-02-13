# -*- encoding : utf-8 -*-

import requests
import re, time, os
from bs4 import BeautifulSoup

os.system('title 코로나 관제_Made by. ParkJG')
os.system('mode con: cols=42 lines=21')
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do"
query = "?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="

def cleaner(arr):
	arr = re.sub('<.+?>', '', str(arr))
	arr = arr.replace('[', '')
	arr = arr.replace(']', '')
	return arr

def TOTAL():
	r = requests.get(url+query)
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	
	result = soup.select('div[class=open] span[class=num]')
	result = cleaner(result)
	num_result = result.split(', ')
	before = soup.select('div[class=open] span[class="sub_num red"]')
	before = cleaner(before)
	print("\n<<누적 확진자 수>>")
	print(num_result[0], "명\n")
	print("<<증감률>>")
	print(str(before)[1:len(str(before))-1], "명\n")
	print("<<격리중>>")
	print(num_result[1], "명\n")
	print("<<누적 격리 해제>>")
	print(num_result[2], "명\n")
	print("<<사망자>>")
	print(num_result[3], "명\n")
	print("<<10만명당 발생률>>")
	print(num_result[4], "%\n")

def TOP5():
	r = requests.get(url+query)
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	
	print("\n상위 5개 지역 확진률")
	for result in soup.select('div[id=mapAll]'):
		num1 = result.select('p[class=allcity_info1]')
		num2 = result.select('p[class=allcity_info2]')
		num3 = result.select('p[class=allcity_info3]')
		num4 = result.select('p[class=allcity_info4]')
		num5 = result.select('p[class=allcity_info5]')
		num1 = cleaner(num1)
		num2 = cleaner(num2)
		num3 = cleaner(num3)
		num4 = cleaner(num4)
		num5 = cleaner(num5)
		print(str(num1))
		print(str(num2))
		print(str(num3))
		print(str(num4))
		print(str(num5))

def AREAVIEW():
	r = requests.get(url+query)
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	
	for result in soup.select('div[class=regional_patient_status_A]'):
		name = result.select('span[class=name]')
		name = cleaner(name)
		num = result.select('span[class=num]')
		num = cleaner(num)
		before = result.select('span[class=before]')
		before = cleaner(before)
		
	name_result = name.split(', ')
	num_result = num.split(', ')
	before_result = before.split(', ')
	
	print("\n지역\t확진자\t증감")
	for i in range(0, len(name_result)):
		print(name_result[i], " : ", num_result[i], "\t", before_result[i])

while(1):
	os.system('cls')
	TOTAL()
	time.sleep(5)
	os.system('cls')
	TOP5()
	time.sleep(5)
	os.system('cls')
	AREAVIEW()
	time.sleep(5)