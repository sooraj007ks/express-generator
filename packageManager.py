import json
import gen

class PackageManager(object):
    packageData = {
                  "name": "my-express-app",
                  "version": "1.0.0",
                  "description": "",
                  "main": "app.js",
                  "scripts": {
                    "test": "echo \"Error: no test specified\" && exit 1",
                      "start" : "node app.js"
                  },
                  "author": "admin",
                  "license": "ISC",
                  "dependencies": {
                      "http-errors" : "*",
                      "cookie-parser": "*",
                      "express" : "*",
					  "helmet":"*"
                  }
                }
    def writePackageJsonFile(self, modules):
        defaultModules = ['http-errors', 'cookie-parser', 'express', 'helmet']
        semVer = ['@', '~', '^']
        if modules[-1] in ['-i', '-install']:
            modules_ = modules[:-1]
        else:
            modules_ = modules
        for sl, item in enumerate(modules_):
            item = str(item)
            for sem in semVer:
                if sem in item:
                    moduleName, version = item.split(sem)
                    modules_[sl] = moduleName
                    self.packageData["dependencies"][moduleName] = "^{}".format(version)
                    if item == gen.templateEngine:
                        self.templateEngine = moduleName
                    break
            else:
                self.packageData["dependencies"][item] = "*"
            if item in defaultModules or item == self.templateEngine:
                self.modulesToInstall = gen.requiredModules.pop(sl)
        # self.packageData["dependencies"][gen.templateEngine] = "*"
        with open('package.json', 'w') as outfile:
            json.dump(self.packageData, outfile, indent=4, ensure_ascii=False)
