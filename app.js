//const express = require("express");
//const app = express();

//app.use((req, res, next) => {
//	res.status(200).json({
//		message: "It Works"
//	});
//});

//module.exports = app;

const express = require("express");

const app = express();
const handlebars = require("express-handlebars").create({ defaultLayout: "main" });
const bodyParser = require("body-parser");

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static("public"));	//for serving static files
app.use(bodyParser.json());


app.engine("handlebars", handlebars.engine);
app.set("view engine", "handlebars");
app.set("port", 8080);

app.get("/", function (req, res) {
	res.render("index");
    //res.send("hello world");
	
});

//page converts data sent here to json server to send to server web crawler is located on
//may also want to just consider implementing a js to python converter here in order to run python script on same web page
//note: look at https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/forms for instructions on validation and sanitization
app.post("/crawl_web", function (req, res) {

    var payload = { page: null, method: null, limit: null, keyword: null };
    payload.page = req.body.page;
    payload.limit = parseInt(req.body.limit);
    payload.method = req.body.method;
    payload.keyword = req.body.keyword;

    //send json to server
    var request = new XMLHttpRequest();
    request.open('POST', 'http://cs467-test-server.appspot.com', false);
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.stringify(payload));
    var response = JSON.parse(request.responseText);
    //add row or report error
    if (response) {
        console.log("success");
        console.log(response);
    } else {
        alert("Error submitting to server!");       //REMOVE, not supposed to use alerts!
    }

    //res.redirect('/results');   //need to send post data as well, other option is to have this code in same page as graph code (preferred)
});


app.get("/results", function (req, res) {
	res.render("results");
});

app.get("/practice", function (req, res) {
	res.render("practice");
});

app.use(function (req, res) {
	res.status(404);
	res.render("404");
});

//error handler function
app.use(function (err, req, res, next) {
	console.error(err.stack);
	res.type("plain/text");
	res.status(500);
	res.render("500");
});

app.listen(app.get("port"), function () {
	console.log('Express started on http://localhost:' + app.get("port"));
});

//const server = app.listen(8080, () => {
//	const host = server.address().address;
//	const port = server.address().port;

//	console.log(`Example app listening at http://${host}:${port}`);
//});