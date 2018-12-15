var appRouter = function (app) {
    app.get("/", function(req, res) {
        res.status(200).sendFile('pandas-box-plot.html');
    });
}

module.exports = appRouter;