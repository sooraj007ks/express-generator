class PrepareAppJs():
    # const createError = require('http-errors');
    appJsCodes = ""
    def importModulesInAppJs(self, modules):
        for item in modules:
            if '-' not in item:
                self.appJsCodes += "const {0} = require('{0}');\n".format(item)
            else:
                splitItem = item.split('-')
                parsedItem = splitItem[0] + splitItem[1][0].upper() + splitItem[1][1:]
                self.appJsCodes += "const {0} = require('{1}');\n".format(parsedItem, item)
        self.appJsCodes += "const path = require('path');\n" \
                           "const cookieParser = require('cookie-parser');\n" \
                            "const createError = require('http-errors');\n"\
                            "const port = process.env.PORT || 3000;\n" \
                           "const express = require('express');\n"


    def configureAppJs(self, viewEngine):
        self.appJsCodes += "\nconst app = express();\n\n// view engine setup" \
                           "\napp.set('views', path.join(__dirname, 'views'));\n\n"
        self.appJsCodes += "app.set('view engine', '{0}');\n\n".format(viewEngine)
        self.appJsCodes += "app.use(express.json());\n" \
                            "app.use(express.urlencoded({ extended: true }));\n" \
                            "app.use(cookieParser());\n\n" \
                           "app.use(express.static(path.join(__dirname, 'public')));\n\n" \
                           "const indexRouter = require('./routes/index');\n" \
                            "const usersRouter = require('./routes/users');\n\n" \
                            "app.use(require('helmet')()); \n\n" \
                            "app.use('/', indexRouter);\n" \
                            "app.use('/users', usersRouter);\n\n" \
                            "app.listen(port, ()=>{\n" \
                            "    console.log(`Server started on port ${port}`);\n" \
                            "});\n\n" \
                            "module.exports = app;" \

        with open('app.js', 'w') as jsFile:
            jsFile.write(self.appJsCodes)

