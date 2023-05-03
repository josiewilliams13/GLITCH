#pip3 install requests_html bs4
#pip3 install requests beautifulsoup4
from bs4 import BeautifulSoup
import requests
import random

def glitch_misinform(url):
    # Send a GET request to the website and retrieve the HTML content
    response = requests.get(url)

    #TEST - if its working it’s going to return a 200 status code. 
    #Anything else means that your IP is getting rejected by the anti-scraping systems the website has in placed. 
    #A potential solution 
    #is adding custom headers to your script to make your script 
    #look more human – but that might not be sufficient. 
    #Another solution is using an web scraping API 
    #to handle all these complexities for you. (1)
    print(response.status_code)

    #TODO: if url is not valid -> return error message, end program, return to "home"
    #convert the request.ResponseObject into text (unicode)
    html = response.text

    # Parse the HTML content using BeautifulSoup
    #From here, we can traverse
    #the parse tree
    #using the HTML tags and their attributes.
    soup = BeautifulSoup(html, 'html.parser')

    #To show the contents of the page on the terminal, 
    #we can print it with the prettify() method 
    #in order to turn the Beautiful Soup parse tree into a 
    #nicely formatted Unicode string.
    #print(soup.prettify())

    print("checkpoint #1")

    # Find all the form elements in the HTML
    forms = soup.find_all('form')
    #forms = soup.find('table',class_ = 'stripe')

    counter = 0

    # Loop through each form element and populate it with random data
    for form in forms:
        
        # Find all the input elements in the form
        inputs = form.find_all('input')
        for input in inputs:
            # Generate random data based on the input type
            if input.get('type') == 'text':
                print(input['value'])
                data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
            # elif input.get('type') == 'email':
            #     data = f'{"".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5))}@{".".join(random.choices(["gmail", "yahoo", "hotmail"], weights=[5, 3, 2], k=1))}.com'
            elif input.get('type') == 'gender':
                data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=10))
            else:
                data = ''
            
            # counter = counter + 1
            # print (counter)

            # # Set the input value to the random data
            # input['value'] = data 
            if data is None:
                print("nada")
            else:
                print (data)

    print("checkpoint #2")

    # Submit the form
    response = requests.post(url, data=soup.find_all('form')[0].serialize())

    print("checkpoint #3 - success!")
    
    # Return the response
    return response


glitch_misinform("https://docs.google.com/forms/d/1jvhOa8Pc6X4sZgz-CGKRN5gQoX3DQwLXabu8ZLYJ5Ws/viewform?edit_requested=true")
