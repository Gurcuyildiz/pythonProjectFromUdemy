
'''
Guide to Web Scraping
Let's get you started with web scraping and Python.
Before we begin, here are some important rules to follow and understand:

Always be respectful and try to get premission to scrape,
 do not bombard a website with scraping requests, otherwise your IP address may be blocked!
Be aware that websites change often,
meaning your code could go from working to totally broken from one day to the next.
Pretty much every web scraping project of interest is a unique and custom job,
 so try your best to generalize the skills learned here.
OK, let's get started with the basics!

Basic components of a WebSite
HTML
HTML stands for Hypertext Markup Language and every website on the internet uses it to display information.
Even the jupyter notebook system uses it to display this information in your browser.
If you right click on a website and select "View Page Source" you can see the raw HTML of a web page.
This is the information that Python will be looking at to grab information from.
 Let's take a look at a simple webpage's HTML:

<!DOCTYPE html>
<html>
    <head>
        <title>Title on Browser Tab</title>
    </head>
    <body>
        <h1> Website Header </h1>
        <p> Some Paragraph </p>
    <body>
</html>
Let's breakdown these components.

Every indicates a specific block type on the webpage:

1.<DOCTYPE html> HTML documents will always start with this type declaration, letting the browser know its an HTML file.
2. The component blocks of the HTML document are placed between <html> and </html>.
3. Meta data and script connections (like a link to a CSS file or a JS file) are often placed in the <head> block.
4. The <title> tag block defines the title of the webpage (its what shows up in the tab of a website you're visiting).
5. Is between <body> and </body> tags are the blocks that will be visible to the site visitor.
6. Headings are defined by the <h1> through <h6> tags, where the number represents the size of the heading.
7. Paragraphs are defined by the <p> tag, this is essentially just normal text on the website.

There are many more tags than just these, such as
 <a> for hyperlinks, <table> for tables, <tr> for table rows, and <td> for table columns, and more!
CSS
CSS stands for Cascading Style Sheets, this is what gives "style" to a website,
 including colors and fonts, and even some animations!
 CSS uses tags such as id or class to connect an HTML element to a CSS feature, such as a particular color.
 id is a unique id for an HTML tag and must be unique within the HTML document, basically a single use connection.
 class defines a general style that can then be linked to multiple HTML tags.
  Basically if you only want a single html tag to be red, you would use an id tag,
   if you wanted several HTML tags/blocks to be red, you would create a class in your CSS doc
   and then link it to the rest of these blocks.

Scraping Guidelines
Keep in mind you should always have permission for the website you are scraping!
Check a websites terms and conditions for more info.
Also keep in mind that a computer can send requests to a website very fast,
so a website may block your computer's ip address if you send too many requests too quickly.
Lastly, websites change all the time!
You will most likely need to update your code often for long term web-scraping jobs.

Web Scraping with Python
There are a few libraries you will need, you can go to your command line and
install them with conda install (if you are using anaconda distribution),
or pip install for other python distributions.

conda install requests
conda install lxml
conda install bs4

if you are not using the Anaconda Installation, you can use pip install instead of conda install, for example:

pip install requests
pip install lxml
pip install bs4

Now let's see what we can do with these libraries.
'''