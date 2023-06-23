import requests
from bs4 import BeautifulSoup

def get_headings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headings = soup.find_all("h1", "h2", "h3", "h4", "h5", "h6")
    return headings

def get_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title").text
    return title

def get_post_description(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    post_description = soup.find("meta", attrs={"name": "description"})["content"]
    return post_description

def get_alt_tags(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    alt_tags = soup.find_all("img", attrs={"alt": True})
    return alt_tags

def main():
    url = "https://www.example.com/"
    headings = get_headings(url)
    title = get_title(url)
    post_description = get_post_description(url)
    alt_tags = get_alt_tags(url)

    print("Headings:")
    for heading in headings:
        print(heading.text)

    print("Title:")
    print(title)

    print("Post description:")
    print(post_description)

    print("Alt tags:")
    for alt_tag in alt_tags:
        print(alt_tag["alt"])

if __name__ == "__main__":
    main()
