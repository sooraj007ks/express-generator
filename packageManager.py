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
                      "express" : "*"
                  }
                }
    def writePackageJsonFile(self, modules):
        defaultModules = ['http-errors', 'cookie-parser', 'express']
        for item in modules:
            if item not in defaultModules:
                self.packageData["dependencies"][item] = "*"
        self.packageData["dependencies"][gen.templateEngine] = "*"
        with open('package.json', 'w') as outfile:
            json.dump(self.packageData, outfile, indent=4, ensure_ascii=False)
