import os
import re
from blog import article
from blog import index

working_path = os.getcwd()
# Delete all the html files
html_path = os.path.join(working_path, 'html')
html_list = os.listdir(html_path)
for name in html_list:
    if name.find('html') > 0:
        html_file = os.path.join(html_path, name)
        os.remove(html_file)
# Convert md to html
md_path = os.path.join(working_path, 'md')
md_list = os.listdir(md_path)
for name in md_list:
    if re.match(r'[0-9][0-9][0-9][0-9]_[0-9][0-9]_[0-9][0-9].*', name) is not None:
        myarticle = article.Article(name)
        myarticle.to_html()
# Generate index
myindex = index.Index()
myindex.to_html()



