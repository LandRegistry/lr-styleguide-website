# Land Registry style guide website

Website for the lr-style-guide repo at https://github.com/LandRegistry/lr-style-guide

Demonstrates one possible way to consume the style guide.

We’re going to install the styleguide as a submodule, then simply use the generated assets:

Grab the style guide as a submodule:
```git submodule add https://github.com/LandRegistry/lr-style-guide.git ./app/static```

Within the ```head``` of ```/app/templates/layout.html``` we import the css:

```
  <!-- Styleguide assets -->
  <!--[if gt IE 8]><!--><link href="/static/lr-style-guide/lr-styleguide/css/styleguide.css" media="screen" rel="stylesheet" type="text/css" /><!--<![endif]-->
  <!--[if IE 8]><link href="/static/lr-style-guide/lr-styleguide/css/styleguide.css-ie8" media="screen" rel="stylesheet" type="text/css" /><![endif]-->
  <!--[if IE 7]><link href="/static/lr-style-guide/lr-styleguide/css/styleguide.css-ie7" media="screen" rel="stylesheet" type="text/css" /><![endif]-->
  <!--[if IE 6]><link href="/static/lr-style-guide/lr-styleguide/css/styleguide.css-ie6" media="screen" rel="stylesheet" type="text/css" /><![endif]-->
```

Before the closing ```</body>``` tag, we then import the js:

```
  <!-- Styleguide assets -->
  <script type="text/javascript" src="/static/lr-style-guide/lr-styleguide/js/styleguide.min.js"></script>
```

## Working on this website

### Getting started

The site itself is a Flask application.

Clone this repo: ``` git clone git@github.com:LandRegistry/lr-styleguide-website.git ```

Set up a Python virtual environment and activate it.

Next install requirements: ``` pip install -r requirements.txt ```

Then ``` python app/server.py ``` should get you running on http://localhost:5000
