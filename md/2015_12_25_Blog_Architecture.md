#Homemade Tiny Blog

Nowadays it is quite simple to have your own blog. Thousands free blog providers are out there. With some clicks and without even basic knowledge of computer science, you are a blogger. But being as myself, I am not satisfied with any blog provider on this earth.(Yes such a big asshole I am.) So, I would like to make my own blog from sketch.

Here are the targets of this project:  

* I would like to build tech stacks as much as possible.(I won't write an OS for it, of cource.)
* I would like to make my code short and simple.
* I don't want to spend much money on it.

------------------------------------------------------

######Software Architecture  

`/md`  
All the articles will be written in markdown format and stored in this folder.

`/html`
The generated html file and css file will be sroted in this folder.

`crontab -l`  
A cron task will repeatly pull from github and call main to convert md to html and generate an index page.

`blogbackend.py`  
A python library to convert *.md to *.html. Now an existing libary is being used. Later I will write my own, or extand for the current one.

`blogfrontend.py`  
A python library to create the index page of the blog. Later I will add CSS and maybe js for some function.

`blogserver.py`  
Will call flask to run an http server.

`restart_server.sh`  
Call nohup to run flask http server, log will be write to nohup.out  

------------------------------------------------------------

######OS

Some version of [linaro](http://dl.cubieboard.org/model/cubietruck/Image/Linaro-server/) compiled for arm is used. Later I will compile my own system.  
Version:  
* Linux kernel: `3.4.79`
* Python: `2.7.3`
* Sqlite3: `3.7.13`
* Flask: `0.10.1`

-----------------------------------------------------------

######Hardware

I choose [**Cubie Truck**](cubieboard.org) to host my server.

-----------------------------------------------------------

Check [here](xjq314.com) if you are interested.




