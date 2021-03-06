const path = require('path');
const cookieParser = require('cookie-parser');
const createError = require('http-errors');
const port = process.env.PORT || 3000;
const express = require('express');

const app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'hbs');

const indexRouter = require('./routes/index');
const usersRouter = require('./routes/users');
app.use(require('helmet')());
 
app.use(express.json());

app.use(express.urlencoded({ extended: true }));

app.use(cookieParser());

app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);

app.use('/users', usersRouter);


app.listen(port, ()=>{
    console.log(`Server started on port ${port}`);
});

module.exports = app;

    