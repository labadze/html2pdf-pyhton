This project was developed for converting any html page, or html file to PDF.

## Why python?

I have developed a project using node.js with mongo, but once I found that I cannot generate PDF files on freeBSD server. I could not install puppitter and / or fantom.js because it's not supported by unix OS and downloaded OS X files instead.
After Googling for a week i made this patch or I don't know how to call it, but I liked python and python flask.
For now it works fine and I happy. Down where I will provide instruction for Python 2.7 (It was tested on 2.7 and works fine), also how to make it work on  freeBSD (if you like this OS).

####
##### USAGE
####
###### `python html2pdf.py file_to_convert.html output_converted_file.pdf`
####
###### You can also get help using
###### `python html2pdf.py -h`
####

### `What to to before ?`

It's very very simple, you need **python** installed on  your OS you need to set path to python executable. You need also **pip** installed to  install additional packages. 

### `Lets start`

You know, python project need python and pip installed and working, also virtualenv and GCC, there is lot of documentation for LINUX and Windows but not for FreeBSD and it's problem, but if you know all benefits of this OS you know that performance and security is very very important, DO NOT FORGET, USER AND CUSTOMER ARE VIP NOT A root...


Well preparing....

### `SETUP FreeBSD For Python`

For package searching use following command:


`pkg seach python`

You will  get list of packages like: 
 
 and onw of them: 
 
 `python27-2.7.16_1              Interpreted object-oriented programming language`
 
 Well let's do it and command: 
 
 `pkg install python27`
 
 now you need package **pip** it's ofr install python packages like flask mongo etc.
 
 `pkg seach pip`
 
 And here is: 
 
 `py27-pip-19.1.1                Tool for installing and managing Python packages`
 
 Well done now  install it: 
 
 `pkg install py27-pip`
 
 See logic on package installation? ;)
  
 Now if you type python or pip you will get output I didn't and was very sad and unhappy...
 
 But everything is fixable besides death, we have just alias to like env variable in  windows.
 
 `which python`
 
 And if you get that command not found try to find your python installation in: 
 
 `/usr/local/bin/python2.7`
 
 Now make symlink:
 
 `ln -s /usr/local/bin/python2.7 /usr/local/bin/python`
 
You need more for FreeBSD you need alias this paths:

`# cat .tcshrc`

`alias python python2.7`


`alias pip /usr/local/bin/pip-2.7`

And everything this you can do using 

`echo 'alias python python2.7' >> ~/.tcshrc`

Alias will not automatically work in your current session until you relog to shell or "reload" changes in .tcshrc:

`source ~/.tcshrc`

By editing dotfile, alias will become permanent.
To create just a temporary alias for current session, you may set alias directly in the shell:

`alias python python2.7`

Temporary alias will disappear once you log off but can be "unaliased" in current session:

`unalias python`

Or just edit this file and do `source ~/.tcshrc`

So check if following command works: 

`python`

`pip`

If you get output it's ok and we can move.

### Install everything we need before proceed
You need also few packages to convert PDF on  freeBSD:

It's **wkhtmltopdf** and you need **x11 Webfonts** (maybe).

Well use `pkg search wkhtmltopdf`

Output is only one: 

`wkhtmltopdf-0.12.5_3           Convert HTML (or live webpages) to PDF or image`

Now install be brave baby : 

`pkg install wkhtmltopdf`

Do not forget:

`webfonts-0.30_14               TrueType core fonts for the Web`

And: 

`pkg install webfonts`

Well done! Now your application is ready for work, do not forget to install all packages via **pip**

But it's another chapter, it's python package.

### Install Python packages

`pip install pdfkit`

### Finally as bonus track lets complete deployment for operating system

Do not forget install virtual environment for python : 

`pkg install py27-virtualenv`
 
 
### Good luck and happy coding

 
