import os
import gen
from customError import Errors
from packageManager import PackageManager
from writeAppJs import PrepareAppJs

class ExpressGenerator(Errors, PackageManager, PrepareAppJs):
    templateEngine = gen.templateEngine
    requiredModules = gen.requiredModules
    modulesToInstall = []
    directoriesRequired = [
        'node_modules',
        'public',
        'routes',
        'views'
    ]

    def createDirectories(self):
        publicFolders = ['IMG', 'JS', 'CSS']
        try:
            for directory in self.directoriesRequired:
                os.mkdir(directory)
            for folder in publicFolders:
                os.mkdir(os.path.join(os.getcwd(),'public', folder))
        except Exception as e:
            if not str(e).startswith("[Error 183]"):
                self.reportError('creating directories', e)

    def fillPublicFolder(self):
        try:
            publicDir = os.path.join(os.getcwd(), 'public')
            with open(os.path.join(publicDir, 'JS', 'main.js'), 'w') as fh:
                fh.write('window.onload = function(){\n\n};')
            with open(os.path.join(publicDir, 'CSS', 'style.css'), 'w') as fh:
                fh.write('*{\n\tmargin: 0;\n\tpadding:0;\n\tbox-sizing:border-box;\n}')
        except Exception as e:
            self.reportError('creating public directory files', e)

    def fillViewsFolder(self):
        try:
            publicDir = os.path.join(os.getcwd(), 'views')
            with open(os.path.join(publicDir, 'index.{}'.format(self.templateEngine)), 'w') as fh:
                if not self.templateEngine == 'pug':
                    fh.write('')
                else:
                    fh.write('''extends layout

block content
  h1= title
  p Welcome to #{title}''')
            with open(os.path.join(publicDir, 'layout.{}'.format(self.templateEngine)), 'w') as fh:
                if not self.templateEngine == 'pug':
                    fh.write('')
                else:
                    fh.write('''doctype html
html
  head
    title= title
    link(rel='stylesheet', href='/CSS/style.css')
  body
    block content
    script(src="/JS/main.js")
''')
        except Exception as e:
            self.reportError('creating public directory files', e)

    def fillRouterFolder(self):
        try:
            routerDir = os.path.join(os.getcwd(), 'routes')
            indexData = '''
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', (req, res, next) => {
  res.render('index', { title: 'Home page' });
});

module.exports = router;
'''
            userData = '''
var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', (req, res, next) => {
  res.send('respond with a resource');
});

module.exports = router;

            '''
            with open(os.path.join(routerDir, 'index.js'), 'w') as fh:
                fh.write(indexData)
            with open(os.path.join(routerDir, 'users.js'), 'w') as fh:
                fh.write(userData)
        except Exception as e:
            self.reportError('creating public directory files', e)

    def installDependencies(self):
        # data = 'cd {0}\nnpm install\ncode .\npause'.format(os.getcwd())
        data = 'cd {0}\nnpm install\npause'.format(os.getcwd())

        try:
            with open("run.bat", 'w') as fh:
                fh.write(data)
            os.startfile("run.bat")
            # os.startfile("app.js")
        except Exception as e:
            self.reportError('trying to install', e)

    def prepareNecessaryFiles(self):
        self.createDirectories()
        self.fillPublicFolder()
        self.fillRouterFolder()
        self.fillViewsFolder()
        self.writePackageJsonFile(self.requiredModules)
        self.importModulesInAppJs(self.modulesToInstall)
        self.configureAppJs(self.templateEngine)
        if gen.requiredModules[-1] in ['-i', '-install']:
            self.installDependencies()


def main():
    while True:
        generator = ExpressGenerator()
        generator.prepareNecessaryFiles()
        # print gen.templateEngine
        break
    #raw_input('Press any key to quit')


if __name__ == '__main__':
    main()