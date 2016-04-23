/**
 * Created by Jeff on 4/23/2016.
 */
var express = require('express');
var router = express.Router();
var request = require('request');

/* GET users listing. */
router.get('/image/', function(req, res, next) {
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
        json: { "url": "https://scontent-yyz1-1.xx.fbcdn.net/hphotos-xpl1/v/t1.0-9/12715270_1196180507076818_6586415939809965548_n.jpg?oh=92c75195f20e9a188304dbe8e26833b1&oe=57ABE939" }
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
