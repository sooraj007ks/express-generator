# import sys

viewEngines = ['pug', 'ejs', 'hbs', 'handlebars']
templateEngine = raw_input('Enter view engine (pug | ejs | hbs):').lower().strip(' ');
modules = raw_input('Enter required dependencies:').lower()
requiredModules = modules.split(' ')