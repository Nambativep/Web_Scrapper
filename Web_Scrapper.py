# WEB_SCRAPPING: is extracting DATA from a website
# We'll send a request to that URL will want to scrap
# And get a response bck which data we need
# We need two Python Libraries:
# 1: Requests: used for sending request
# 2: BeautifulSoup: Used in extracting and receiving the data we need.
# bs4 as recognised by the window's machine.


(base) C:\Users\PETER NAMBATIV>python
Python 3.11.3 | packaged by Anaconda, Inc. | (main, Apr 19 2023, 23:46:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> from bs4 import BeautifulSoup
>>>
>>> url = "https://nambativep.github.io/"
>>> r = requests.get(url)
>>> r
<Response [200]>
>>> soup = BeautifulSoup(r.content, 'lxml')
>>> title = soup.find_all('h1')
>>> title
[<h1>Peter Data Administrator, Web Developer, Python Developer. My portfolio <br/></h1>]
>>> title = soup.find_all('p')
>>> title
[<p>Data Administrator, SQL, Python, HTML, CSS, Javascript, Wordpress <a href="https://twitter.com/nambative">@nambative</a> for <a href="https://html5up.net">HTML5 UP</a><br/>
                                                and released for free under the <a href="https://html5up.net/license">Creative Commons license</a>.</p>, <p>In this project I created Databases for Companies Staff using SQL Server,
                                                                        their salaries, staff ID, ETC       <br/>
<br/>
</p>, <p>All audio and video records are uploaded here for download and adverts</p>, <p>All Latest contents for download for views and download come in here </p>, <p>python and django used here to create this website display products and prices and where you can find them</p>, <p>I used pandas, matplolib, seaborn etc to predict the kind of music that people from ages of 18, 25, 35 and likes</p>, <p>Created a car game using python, here you tell the car to start and when is already
                                                                                started, car is already started, and if already stopped it tells you car is already stopped</p>, <p>Created number starter APP using JAVASCRIPT, here you can count all the projects already
                                                                                succeeded , number of number hours, your happy clients</p>, <p>Created a youtube channell where you can watch all categories of videos on youtube and different interviews</p>, <p>Encoded a credit card using python to be fully used on the AUTOMATED TELLER MACHINE FOR TRANSATIONS</p>, <p>Created an APP for counting to avoid the waste of time involved in manual counting </p>, <p>This App created by me changes different colors in differentsections of the APP</p>, <p>LACATION<br/>
                                                                Lagos, TN 00000-0000</p>, <p><a href="#">(+234) 8021-2768-91 <br/>(+234) 8069-5401-35</a></p>, <p><a href="#"></a></p>, <p><a href="#">programmewithnambativep@gmail.com
                                                                        <br/>nambativep68@gmail.com
                                                                </a></p>]
>>> title.gettext()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\PETER NAMBATIV\New folder\ANACONDA_3\Lib\site-packages\bs4\element.py", line 2428, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute 'gettext'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
>>> title[0].getText()
'Data Administrator, SQL, Python, HTML, CSS, Javascript, Wordpress @nambative for HTML5 UP\r\n\t\t\t\t\t\tand released for free under the Creative Commons license.'
>>> title1 = title[0].getText()
>>> print(title1)
Data Administrator, SQL, Python, HTML, CSS, Javascript, Wordpress @nambative for HTML5 UP
                                                and released for free under the Creative Commons license.
>>> for t in title:
...     print(t.getText())
...