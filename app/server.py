import os
from flask import Flask, render_template
from flask.ext import assets

app = Flask(__name__)

env = assets.Environment(app)

env.register(
    'styleguide_website',
    assets.Bundle(
        'demo/sass/styleguide-examples.scss',
        filters='scss',
        output='demo/css/styleguide-examples.css'
    )
)


# Small thing to allow source code examples in a template
app.jinja_env.globals['include_raw'] = lambda filename : app.jinja_loader.get_source(app.jinja_env, filename)[0]

# General base styles

@app.route('/')
def home():
    return render_template('styleguide/index.html')

@app.route('/typography')
def typography():
    return render_template('styleguide/typography.html')

@app.route('/icons')
def icons():
    return render_template('styleguide/icons.html')

@app.route('/layout')
def layout():
    return render_template('styleguide/layout.html')

@app.route('/forms')
def forms():
    return render_template('styleguide/forms.html')

@app.route('/buttons-and-similar-controls')
def buttons_and_similar_controls():
    return render_template('styleguide/buttons_and_similar_controls.html')

@app.route('/tables-and-data-display')
def tables_and_data_display():
    return render_template('styleguide/tables_and_data_display.html')

@app.route('/panels-and-callouts')
def panels_and_callouts():
    return render_template('styleguide/panels_and_callouts.html')

@app.route('/sticky-panel')
def sticky_panel():
    return render_template('styleguide/sticky_panel.html')

@app.route('/dividers')
def dividers():
    return render_template('styleguide/dividers.html')

@app.route('/utilities')
def utilities():
    return render_template('styleguide/utilities.html')

# Components

@app.route('/breadcrumbs')
def breadcrumbs():
    return render_template('styleguide/breadcrumbs.html')

@app.route('/case-list')
def case_list():
    return render_template('styleguide/case_list.html')

@app.route('/pagination')
def pagination():
    return render_template('styleguide/pagination.html')

@app.route('/search-results')
def search_results():
    return render_template('styleguide/search_results.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
