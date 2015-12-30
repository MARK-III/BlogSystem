#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import codecs
import os

def generate_index():

    public_host = 'xjq314.com'
    public_url = 'http://' + public_host + '/'

    working_path = os.getcwd()
    html_path = os.path.join(working_path, 'static')
    html_list = os.listdir(html_path)
    html_list.sort(reverse = True)

    index_name = 'index.html'
    index_path = os.path.join(html_path, index_name)
    index = codecs.open(index_path, mode='w', encoding='utf-8')
    
    #Write css
    index.write('<head>\n')
    index.write('<link rel="stylesheet" type="text/css" href="http://xjq314.com/test.css" />\n')
    index.write('</head>\n')
    
    #Write head
    blog_name = "坐井观天"
    index.write('<h1>' + blog_name + '</h1>\n')
    
    #Write article list
    for html_name in html_list:
        if ((html_name != 'index.html') & (html_name.find('html') > 0)):
	    html = os.path.join(html_path, html_name)
	    
            #Add css to article
            html_file = open(html, "r")
            contents = html_file.readlines()
	    essay_name = contents[0].replace('<h1>','').replace('</h1>\n','')
            html_file.close()
            contents.insert(0, '</head>\n')
            contents.insert(0, '<link rel="stylesheet" type="text/css" href="http://xjq314.com/test.css" />\n')
            contents.insert(0, '<head>\n')
            html_file = open(html, "w")
            contents = "".join(contents)
            html_file.write(contents)
            html_file.close 

            index.write('<a href="' + public_url + 'blog/' + html_name + '">' + essay_name + '</a>\n')
            index.write('<br></br>\n')
    index.close()
