from bs4 import BeautifulSoup
import urllib2
import sys

repo="https://github.com/sanskar-sopho/road-segmentation/"
base_link='http://github.com'
file_count=0

def extract_code(url,file_name):
	if(file_count>=50):
		sys.exit
	page=urllib2.urlopen(url)
	soup=BeautifulSoup(page,'xml')
	file=open(file_name,'w')
	file_count+=1
	# repcontent=(soup.find(class_="repository-content")).find_all('table')
	# for row in soup.find(class_="repository-content").find_all("tr"):
	# 	print(row,'\n')
	# date=soup.find_all(datetime=True)
	date=soup.findChildren(['relative-time'])
	datetime=date[0]['datetime']
	tables=soup.findChildren('table')
	# print(tables)
	my_table=tables[0]
	rows=my_table.findChildren(['th','tr'])
	
	line=0
	for row in rows:
		# print(line)
		line+=1
		for string in row.stripped_strings:
			string=str(unicode(string))
			# print(string)
			file.write(string)
			file.write(' ')
			# spans=cells[1].findChildren('span')
			# for span in spans:
				# print(span.string)
		file.write('\n')
	return datetime

def expand_folder(url)
	print "folder : ", url
	page=urllib2.urlopen(url)
	soup=BeautifulSoup(page,'xml')
	table=soup.find('table')
	rows=table.find_all(['th','tr'])
	for row in rows:
		if('js-navigation-item' not in row['class']):
			continue
		cols=row.find_all('td')
		for col in cols:
			if('content' not in col['class']):
				continue
			tag=col.find('a')
			link=tag['href']
			if('tree' in link):
				expand_folder(base_link+link)
			if('blob' in link):
				datetime=extract_code(base_link+link,str(file_count)+'.txt')
				print('file written ', datetime)
			else:
				return

	expand_folder(repo)