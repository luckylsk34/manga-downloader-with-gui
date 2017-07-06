import os
import sys
from bs4 import BeautifulSoup
from urllib import request
from fpdf import FPDF
from PIL import Image

manga_name, starting_chapter, ending_chapter = sys.argv[1:]
starting_chapter = int(starting_chapter)
ending_chapter = int(ending_chapter)


folder_name = "%s(%03d-%03d)" %(manga_name, starting_chapter, ending_chapter)
if not os.path.exists(folder_name):
	os.mkdir(folder_name)
os.chdir(folder_name)


chapter_num = 1
page_num = 1

manga_name = "-".join(manga_name.split(" "))

for chapter_num in range(starting_chapter, ending_chapter+1):

	pdf = FPDF(unit ='pt')

	print("downloading chapter %03d ..." %chapter_num, end = "\r")

	req = request.Request("http://www.mangareader.net/%s/%d" %(manga_name, chapter_num), headers={'User-Agent': 'Mozilla/5.0'})



	html = request.urlopen(req).read()

	soup = BeautifulSoup(html, "html.parser")

	option_list = soup.find_all("option")
	try:
		max_pages = int(option_list[len(option_list)-1].string)
	except:
		print("""either internet connection is not available or the name you have entered is wrong
try again with the only the first part of the name
for example if "rave master" doesnot work, use rave
this must be done only if the full name doesnot work""")
		os.chdir("./..")
		os.rmdir("./%s(%03d-%03d)" %(manga_name, starting_chapter, ending_chapter))

		input("download failed press enter to continue")
		exit()


	for page_num in range(1, max_pages+1):

		print("downloading chapter %03d ... page:%02d" %(chapter_num, page_num), end = "\r")
		req = request.Request("http://www.mangareader.net/%s/%d/%d" %(manga_name, chapter_num, page_num), headers={'User-Agent': 'Mozilla/5.0'})

		html = request.urlopen(req).read()

		soup = BeautifulSoup(html, "html.parser")

		img_tag = soup.find("img")

		img_url = img_tag.get("src")

		img_req = request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})

		f = open("d%02d.jpg" %page_num, 'wb')
		f.write(request.urlopen(img_req).read())
		f.close()

		img = Image.open("./d%02d.jpg" %page_num)

		width, height = img.size


		if height<width:
			pdf.add_page('p',format = (width, height))
		else:
			pdf.add_page('l', format = (height, width))
		
		pdf.image("d%02d.jpg" %page_num, x = 0, y = 0, w = width, h = height)
		os.remove("d%02d.jpg" %page_num)

	print("completed downloading chapter.no %03d" %chapter_num)
	pdf.output("chapter-%03d.pdf" %chapter_num)
	os.chdir("./..")
input("download complete, press enter to continue")