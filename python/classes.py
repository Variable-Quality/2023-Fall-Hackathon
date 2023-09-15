from bs4 import BeautifulSoup
import requests
import re

#BASE_URL: https://catalog.kennesaw.edu/content.php?catoid=68&catoid=68&navoid=5469&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=1#acalog_template_course_filter


def soupify(url:str) -> BeautifulSoup:
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    temp_page = requests.get(url, headers=headers)
    return BeautifulSoup(temp_page.text,features='html.parser')

def main() -> dict:
    #32 pages of classes, at the time of making this
    courses = {}
    for page in range(1,32):
        
        url = "https://catalog.kennesaw.edu/content.php?catoid=68&catoid=68&navoid=5469&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D={0}#acalog_template_course_filter".format(page)

        page = soupify(url).find_all(class_="block_content")
        for p in page:
            key = ""
            #says this is out of range, idk, im goin to bed
            course_list = p.find_all("tbody")[8]
            tr_list = course_list.find_all("tr")[1:]

            for row in tr_list:
                if len(row.find_all("strong")) > 0:
                    key = row.text
                    print(f"New Key: {key}")
                else:
                    txt = re.sub(r'[^A-Za-z0-9 /\'()-]:', '', row.text).split(":")
                    courses[key] = (txt[0],txt[1])
                    print(courses[key])

    return courses


            

if __name__ == "__main__":
    main()
