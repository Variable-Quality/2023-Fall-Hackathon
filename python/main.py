from bs4 import BeautifulSoup
import requests

#bachelors_list = requests.get("https://www.kennesaw.edu/degrees-programs/bachelor-degrees/index.php")
#masters_list = requests.get("https://www.kennesaw.edu/degrees-programs/master-degrees/index.php")

#b_soup = BeautifulSoup(bachelors_list.text,features='html.parser').find(class_="searchable_list")
#m_soup = BeautifulSoup(masters_list.text,features='html.parser').find(class_="searchable_list")

#old code

class DegreePage:

    def __init__(self):
        self.title = str
        self.description = str
        self.careers = list
        self.salary = str #Maybe change to int
        self.school = str

#End DegreePage


#Takes a url, spits back a BS4 object. Use find_class and find_id to narrow BS4 object down.
#Leave both blank if you just want the raw BS4. Can't do both (yet), it'll prioritize find_class
def soupify(url:str, find_class:str, find_id:str) -> BeautifulSoup:
    temp_page = requests.get(url)

    if find_class:
        return BeautifulSoup(temp_page.text,features='html.parser').find(class_=find_class)
    elif find_id:
        return BeautifulSoup(temp_page.text,features='html.parser').find(id=find_id)
    
    return BeautifulSoup(temp_page.text,features='html.parser')

#This nabs all the links within a given BeautifulSoup object and returns them in a list
def get_links(soup:BeautifulSoup) -> list:
    a_tags = soup.find_all("a")
    links = []
    for a in a_tags:
        if a.has_attr('href'):
            links.append(a['href'])
    return links

#Takes in a degree page as a bs4 object and packages up the info into an object
def package_page_info(soup:BeautifulSoup) -> DegreePage:
    page = DegreePage()
    page.title = soup.find(class_="section_heading").text
    print(page.title)

def main(input):

    package_page_info(input)

if __name__ == "__main__":
    b_soup = soupify("https://www.kennesaw.edu/degrees-programs/bachelor-degrees/index.php", find_class="searchable_list", find_id=None)
    m_soup = soupify("https://www.kennesaw.edu/degrees-programs/master-degrees/index.php", find_class="searchable_list", find_id=None)
    
    b_links = get_links(b_soup)
    m_links = get_links(m_soup)
    

    print("=============Bachelors Degree Titles===========")
    for link in b_links:
        t_soup = soupify(link, None, None)
        main(t_soup)

    #This is all getting redone later
    print("=============Masters Degree Titles============")
    for link in m_links:
        t_soup = soupify(link, None, None)
        main(t_soup)



