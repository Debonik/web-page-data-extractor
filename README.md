# web-page-data-extractor
This repository consists of a Python script which extracts headings, titles, post descriptions and alt tags of a particular URL.
------------------------------------------------------------------------------------------------------------------------------------

DESCRIPTION OF VARIOUS FUNCTIONS USED IN THE CODE

Here is a brief explanation of the different sections of the code:

The **get_headings()** function uses the requests library to make a request to the specified URL and then uses the BeautifulSoup library to parse the HTML response and extract all of the heading tags.
The **get_title()** function does the same thing as get_headings(), but it only extracts the title tag.
The **get_post_description()** function uses the BeautifulSoup library to find the meta tag with the name attribute set to description and then extracts the value of the content attribute.
The **get_alt_tags()** function uses the BeautifulSoup library to find all of the img tags with the alt attribute set to True and then extracts the value of the alt attribute.
The **main()** function calls all of the other functions and prints the results.
