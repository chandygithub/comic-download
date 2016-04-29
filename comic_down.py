import requests
from urlparse import urljoin
import re
import subprocess
import os
import wget

url = raw_input("Enter base url: ")
url = url + '/' if url[-1] is not '/' else url
start = int(raw_input("start issue: "))
end = int(raw_input("end issue: "))
comic_base_path = os.path.join(os.getcwd(), url.split("/")[-2])

subprocess.call(['mkdir', url.split("/")[-2]])
""" Does not work subprocess.call(['cd', url.split("/")[-2]]) """
os.chdir(comic_base_path)

link_list = []
issue_directory = []
for x in range(start, end + 1):
    adding = "Issue-" + str(x)
    link_list.append(urljoin(url, adding) + "?readType=1")
    issue_directory.append(str(adding))
    subprocess.call(['mkdir', adding])

for issue_num in range(len(link_list)):
    visit = requests.get(link_list[issue_num])
    print("Downloading " + issue_directory[issue_num])
    images = re.findall('lstImages\.push\(\"(.*)\"\)', visit.text)
    os.chdir(os.path.join(comic_base_path, issue_directory[issue_num]))
    for image_url in images:
        wget.download(image_url)

    ''' print match '''

    """
     images are in javascript array 'lstImages.push' use regex to extract
     use urrlib.urlretrieve(link, location-filename) to download
     to get issue x.split("/")[-1].split("?")[0]
    """
