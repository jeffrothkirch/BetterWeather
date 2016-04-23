/**
 * Created by Jeff on 4/23/2016.
 */
var express = require('express');
var router = express.Router();
var request = require('request');

/* GET users listing. */
router.get('/image/:imageUrl', function(req, res, next) {
    console.log("request received");

    // Set the headers
    var headers = {
        'User-Agent':       'Super Agent/0.0.1',
        'Content-Type':     'application/json',
        'Ocp-Apim-Subscription-Key':'aef1a034d52a4018821c49cccb67d59d'
    }

    // Configure the request
    var options = {
        url: 'https://api.projectoxford.ai/emotion/v1.0/recognize',
        method: 'POST',
        headers: headers,
        json: { "url": req.params.imageUrl }
    }

    // Start the request
    request(options, function (error, response, body) {
        if (response.statusCode == 200) {
            console.log(response.body)
            res.send(response.body);
        }

        if (response.statusCode != 200){
            console.log(response);
        }
    })
});

router.post('/sendimage/', function(req, res, next) {
    console.log("request received");

    // Set the headers
    var headers = {
        'User-Agent':       'Super Agent/0.0.1',
        'Content-Type':     'application/json',
        'Ocp-Apim-Subscription-Key':'aef1a034d52a4018821c49cccb67d59d'
    }

    var imageUrl = req.body.imageUrl;
    console.log("image url = " + imageUrl);

    // Configure the request
    var options = {
        url: 'https://api.projectoxford.ai/emotion/v1.0/recognize',
        method: 'POST',
        headers: headers,
        json: { "url": imageUrl }
    }

    // Start the request
    request(options, function (error, response, body) {
        if (response.statusCode == 200) {
            console.log(response.body)
            res.send(response.body);
        }

        if (response.statusCode != 200){
            console.log(response);
        }
    })
});

module.exports = router;
