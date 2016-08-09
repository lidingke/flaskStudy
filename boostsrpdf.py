from jinja2 import Environment, PackageLoader
from flask_bootstrap import Bootstrap
env = Environment(loader=PackageLoader('bootstrpdf', 'templates'))
template = env.get_template('user.html')
print template.render(name = 'lidingke')
