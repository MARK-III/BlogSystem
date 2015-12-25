#Homemade Tiny Blog

Nowadays it is quite simple to have your own blog. Thousands free blog providers are out there. With some clicks and without even basic knowledge of computer science, you are a blogger. But being as myself, I am not satisfied with any blog provider on this earth.(Yes such a big asshole I am.) So, I would like to make my own blog from sketch.

------------------------------------------------------

Here are some background of this project:  

* I would like to build tech stacks as much as possible.(I won't write an OS for it, of cource.)
* I would like to make my code short and simple.
* I don't want to spend much money on it.

Anyway, the final tech stack is like this:  

`md`  
All the articles will be written in markdown format and stored in a folder of this very repository.

`crontab`  
Repeated to check if there is any new article. If there is, it will git pull it from github.

`blogbackend.py`  
A python script to convert *.md to *.html. Now I use an existing libery. Later I will write my own, or extand for the current one.

`blogfrontend.py`  
A python script to create the index page of the blog. Later I will add CSS and maybe js for some function.

`blogserver.py`  
Powered by Flask and serves static files.

`Something-daemon`  
A daemon call all the script above.

------------------------------------------------------------------

Check xjq314.com

Update on 2015.12.26:  
Now CSS is supported.



