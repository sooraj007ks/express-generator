## Generate Express project Directory
Written over the Mighty Python. I like to  call Python like that :)
This app creates NodeJs Express project directories with basic files and automatically
installs all the dependencies specified when creating directory. It will also import all
of them to the project main file.

You can add more dependencies after a space.

It will work in windows 10. For others, download the source code and
compile using pyinstaller in your computer.

Run ExpressGenerator.exe to use the tool.
In your cmd | powershell | gitbash
```
start F:/ExpressGenerator
```

You can enter your desired packages with or without version

```
Enter view engine ( pug | ejs | hbs | mustache ):pug@2.0.3
Enter required dependencies:express@4.5.6 passport bcryptjs body-parsor -i
```
After entering necessary packages enter `-i` or `-install` to automatically install the packages.

Or you will have to use `npm install` to install the packages