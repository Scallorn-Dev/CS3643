'''
Scenario
You have been tasked with building a URL file validator for a web crawler. A web crawler is an application that fetches a web page, extracts the URLs present in that page, and then recursively fetches new pages using the extracted URLs. The end goal of a web crawler is to collect text data, images, or other resources present in order to validate resource URLs or hyperlinks on a page. URL validators can be useful to validate if the extracted URL is a valid resource to fetch. In this scenario, you will build a URL validator that checks for supported protocols and file types.

Introducing a split function:
A split function is a string method. It is used to create a list of words that is separated by a particular delimiter.

A delimiter can be any character, comma, or space, or any word. For example, a student’s details (that is, name, age, and language) are given as a “John,25,English” string, and if you want to create a list. The string is delimited by “,”:

#example-1
	student_detail = “John,25,English”.split(“,”)
	print(student_detail)
	[“John”, “25”, “English”]
#example-2
	student_detail = “John|25|English”.split(“|”)
	print(student_detail)
	[“John”, “25”, “English”]
Validation
A URL is in the form of <Protocol>://<hostname>/<fileinfo>. In order to be a valid URL, it must fulfill the following requirements:

Protocol: This can be any value from given list, such as http, https, or ftp.

Hostname: Any string

File extension: fileinfo can be any filename, but it must have an extension from given list (such as .html, .csv, .docx, .jpg, .png, or .gif).

Lets have a look at a few URL examples below:

Input: https://www.technotification.com/2018/06/best-programming-blog.html

Output: True
Input: rstp://www.technotification.com/2018/06/best-programming-blog.html

Output: False (an invalid protocol)
Input: http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv

Output: True
Input: http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample/

Output: False (an invalid file extension)
(Problem here is to validate a resource URL, not a valid link.)

URL = <Protocol>://<hostname>/<fileinfo>
'''
	
import requests #pip install requests

def validate_url(url):
    """Validates the given URL passed as a string.
    
    Arguments:
    url -- String, A valid URL should be of form <Protocol>://<hostname>/<fileinfo>
    
    Valid Protocols: ['http', 'https', 'ftp']
    Valid File Extensions: ['.html', '.csv', '.docx']
    
    Returns:
    True if the URL is valid, otherwise False.
    """

    valid_protocols = ['http', 'https', 'ftp'] #list of valid protocols
    valid_fileinfo = ['.html', '.csv', '.docx'] #list of valid file extensions

    splitUrl = url.split("://") #splitting the protocol from the URL @ :// so https://youtube.com/page.html becomes ["https", "youtube.com/page.html"]

    if len(splitUrl) != 2 or splitUrl[0] not in valid_protocols:    #if splitUrl doesn't have 2 elements (protocol, webpageUrl) or the 1st element (protocol) isn't a valid protcol, return false.
        return False

    domain_and_file = splitUrl[1]   #storing the URL after the protocol
    
    if "/" not in domain_and_file:  #checking for file path after the hostname "/page.html", returns false if missing.
        return False

    file_info = domain_and_file.split("/")[-1]  #splitting the url from the sub directory and the filename: [youtube.com/channel/views.csv] = ["youtube.com", "channel", "views.csv"] and [-1] selects the last element from the split.

    if not any(file_info.endswith(ext) for ext in valid_fileinfo): #checking file extensions 'ext' for validity, if not extension not in valid_fileinfo list, return false.
        return False

    try:
        response = requests.get(url)    #attempting to make a request on the URL

        if response.status_code == 200:     #if status code returns 200 the URL is accessible
            print("URL is valid and accessible.")

        else:
            print(f"URL is valid but returned status code: {response.status_code}") #else there was an error making the request

    except requests.RequestException:   #Exception to catch network areas (no internet/invalid domain)
        print("URL is valid but could not be accessed.")

    return True #URL passes all validation checks!


if __name__ == '__main__':
    url = input("Enter a URL: ")
    print(validate_url(url))

	