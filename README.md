# Land Registry style guide website

Website for the lr-style-guide repo.

Demonstrates one way to consume the style guide.

We’re going to install the styleguide as a submodule, then pass the assets through this site’s
 Flask Assets pipeline.

Grab the style guide as a submodule:
```git submodule add https://github.com/LandRegistry/lr-style-guide.git ./app/static```



## Working on this website

### Getting started

The site itself is a Flask application.

Clone this repo: ``` git clone git@github.com:LandRegistry/lr-styleguide-website.git ```

Set up a Python virtual environment and activate it.

Next install requirements: ``` pip install -r requirements.txt ```

Then ``` python app/server.py ``` should get you running on http://localhost:5000
