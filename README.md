# Mbgen2
A simple microblog generator written in python.

This script depends on the markdown package. To install it run:
``` shell
pip install markdown
```
To use the script, run:
``` shell
python3 mbgen2.py
```
In the same directory as the file.


To use this generator, you have to have a html file with a comment saying `<!--posts here-->`, to signalify where the posts should go.

When you run the script, you should see two boxes, one for a template and the other for the post content. 
In the first box you write your template with a comment saying `<!--content here-->. The contents of your post will be placed inside whatever html you write in this box where the comment is.
In the next box you can write your actual post. This can be written in markdown.

The contents of your last template will be saved in a txt file called `mbgen2.txt`
The contents of the template box with the added post wil be wrapped in a div with a class of "mbgenPost".

There is a seperate python file named `mbgen2Neocities.py`, this version has a button to upload the post directly to neocities. It requires the neocities cli to be installed. Instructions to do that can be founh [here](https://neocities.org/cli).

## Possible upcoming features:

- Timestamps
- better tagging
- Proper neocities API support

  
