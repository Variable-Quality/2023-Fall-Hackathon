from bs4 import BeautifulSoup
from lxml import etree
import requests
import re
#https://stackoverflow.com/questions/46419607/how-to-automatically-install-required-packages-from-a-python-script-as-necessary



#bachelors_list = requests.get("https://www.kennesaw.edu/degrees-programs/bachelor-degrees/index.php")
#masters_list = requests.get("https://www.kennesaw.edu/degrees-programs/master-degrees/index.php")

#b_soup = BeautifulSoup(bachelors_list.text,features='html.parser').find(class_="searchable_list")
#m_soup = BeautifulSoup(masters_list.text,features='html.parser').find(class_="searchable_list")

#old code, keeping it here for future reference

class DegreePage:

    def __init__(self, title:str, description:str, careers:list, school:str):
        #intentionally not using salary, cant really quantify how important money is to someone
        self.title = title
        self.description = description
        self.careers = careers
        self.school = school

#End DegreePage


#Takes a url, spits back a BS4 object. Use find_class and find_id to narrow BS4 object down.
#Leave both blank if you just want the raw BS4. Can't do both (yet), it'll prioritize find_class
def soupify(url:str) -> BeautifulSoup:
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    temp_page = requests.get(url, headers=headers)
    return BeautifulSoup(temp_page.text,features='html.parser')

#This nabs all the links within a given BeautifulSoup object and returns them in a list
def get_links(soup:BeautifulSoup) -> list:
    a_tags = soup.find_all("a")
    links = []
    for a in a_tags:

        if a.has_attr('href'):
            links.append(a['href'])

    return links

#Gets the body of the page and combines it into one big output.
def get_body(soup:BeautifulSoup, xpath:str) -> str:
    for i in range(0,99):
        p_tags_xpath = f"{xpath}/p[{i}]"
        dom = etree.HTML(str(soup))
        print(dom.xpath(p_tags_xpath)[0].text)

#Takes in a degree page as a bs4 object and packages up the info into an object
def package_page_info(soup:BeautifulSoup) -> DegreePage:
    main_xpath = "/html/body/div[1]/div[6]/div/div[1]/div/div[1]" #xpath for main content div, since div does not have any identifiers
    p_title = re.sub(r'[^A-Za-z0-9 /\'()-]', '', soup.find(class_="banner_message").text)
    p_body = get_body(soup, main_xpath)

#Function that is run when the script is executed
def main():
    b_soup = soupify("https://www.kennesaw.edu/degrees-programs/bachelor-degrees/index.php").find(class_="searchable_list")
    m_soup = soupify("https://www.kennesaw.edu/degrees-programs/master-degrees/index.php").find(class_="searchable_list")
    
    b_links = get_links(b_soup)
    m_links = get_links(m_soup)
    

    print("=============Bachelors Degree Titles===========")
    for link in b_links:
        t_soup = soupify(link, None, None)
        package_page_info(t_soup)

    #This is all getting redone later
    print("=============Masters Degree Titles============")
    for link in m_links:
        t_soup = soupify(link, None, None)
        package_page_info(t_soup)
    

if __name__ == "__main__":
    #not even sure if this works, ended up doing all this manually
    #rip
    main()



