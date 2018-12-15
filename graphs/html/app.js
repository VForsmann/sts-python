var express = require("express");
var bodyParser = require("body-parser");
var fs = require('fs')
var path = require("path");
var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

var graphs = "htmlGraphs";

fs.readdir(graphs, function (err, files) {
    if (err) {
        console.error("Could not list the directory.", err);
        process.exit(1);
    }
    console.log("Start to read Files...")
    files.forEach(file => {
        console.log("Read: " + file + "; Located in: " + __dirname + '/' + graphs + '/' + file);
        app.get('/' + file, function (req, res) {
            res.sendFile(path.join(__dirname + '/' + graphs + '/' + file));
        });
    })

    console.log("Finished!")
})

var server = app.listen(3000, function () {
    console.log("Start - Server listening on: ", server.address().port);
});