var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// app.use('/', indexRouter);
// app.use('/users', usersRouter);
app.listen(2048); //  Node.js express WAS 포트번호
app.get("/html.test", function (req, res) {
  // 요청받은 주소로 들어오면 함수 내용 실핼
  // resss.send("asdf");
  var html = "<html><head><meta charset='utf-8'></head><body>";
  html += "내용내용내용내용";
  html += "</body></html>";
  res.send(html);
});
// app.post();

app.get("/param.reqq", function (req, res) {
  var xx = req.query.x * 1;
  var yy = req.query.y * 1;
  var html = "<html><head><meta charset='utf-8'></head><body>";
  html += xx + yy;
  html += "</body></html>";
  res.send(html);
});

app.get("/js.on", function (req, res) {
  var xx = req.query.x * 1;
  var yy = req.query.y * 1;
  var rr = { "result": xx + yy };
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.send(rr);
});




// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
