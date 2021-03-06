/**
 * Created by Jeff on 4/23/2016.
 */
var express = require('express');
var router = express.Router();

// Using require() in ES5
var FB = require('fb');
var request = require('request');
var qs = require('querystring')
var api = require('instagram-node').instagram();

api.use({
    client_id: 'b6c15a9a8f044574bce7ef61e60a3ef1',
    client_secret: '6794c1e633f040b887d258268aab2fba'
});

var redirect_uri = 'http://localhost:8083/api/getCode/';

// This is where you would initially send users to authorize
router.get('/authorize',function(req, res, next){
    console.log('call made to authorize');
    res.redirect(api.get_authorization_url(redirect_uri));
});

router.get('/handleauth', function(req, res, next) {
    console.log('request received, handling auth');

    api.authorize_user(req.query.code, redirect_uri, function (err, result) {
        if (err) {
            console.log(err.body);
            res.send("Didn't work");
        } else {
            console.log('Yay! Access token is ' + result.access_token);
            res.send('You made it!!');
        }
    });
});

/* GET users listing. */
// router.get('/getPics/', function(req, res, next) {
//     console.log("request received");
//
//     // FB.setAccessToken('CAAZATH0lI9d8BAMPXQzGlS348qXqiColLp18UvrZBZC64Ea3HlZCPZAunteTZAZAyZCLchVYoigFYTFIX8TEZBvn9OP8cidcEOZBMxwXKjheZATtGVDz9wsh8EkIyxAZAZCZAU7KXM33HmZCc7E5vPHaye4yY3ErcoxZClcxX9Jo5NaIeFkk5rH6TKPuWdBMCUPZCFl0cFjxemhJvJxFM6IU9ZBaYZAjRbq');
//     //
//     // FB.api('4', { fields: ['id', 'name'] }, function (res) {
//     //     if(!res || res.error) {
//     //         console.log(!res ? 'error occurred' : res.error);
//     //         return;
//     //     }
//     //     console.log(res.id);
//     //     console.log(res.name);
//     // });
//
//
//     // request('https://api.instagram.com/oauth/authorize/?client_id=b6c15a9a8f044574bce7ef61e60a3ef1&response_type=code&redirect_uri=http://localhost:8083/api/getCode/',
//     //     function (error, response, body) {
//     //         //Check for error
//     //         if(error){
//     //             return console.log('Error:', error);
//     //         }
//     //
//     //         //Check for right status code
//     //         if(response.statusCode !== 200){
//     //             return console.log('Invalid Status Code Returned:', response.statusCode);
//     //         }
//     //
//     //         //All is good. Print the body
//     //         console.log(body); // Show the HTML for the Modulus homepage.
//     //         res.send(body);
//     // });
// });

router.get('/getCode', function(req, res, next) {
    console.log("get code -request received");
    var code = req.query.code;

    var headers = {'Content-Type':     'application/x-www-form-urlencoded'}

    var options = {
        url: 'https://api.instagram.com/oauth/access_token',
        method: 'POST',
        headers: headers,
        form: {
            client_id: 'b6c15a9a8f044574bce7ef61e60a3ef1',
            client_secret: '6794c1e633f040b887d258268aab2fba',
            grant_type: 'authorization_code',
            redirect_uri: 'http://localhost:8083/api/getCode/',
            code: code
        }
    }

    request(options, function (error, response, body) {
        if (response.statusCode == 200) {
            console.log(response.body)
            //res.send(response.body);
            var obj =  JSON.parse(response.body);
            var token = obj.access_token;
            //var url = 'https://api.instagram.com/v1/media/search?q=demonstration&lat=40.7128&lng=74.0059&distance=100000&min_timestamp=1272168000&max_timestamp=1461556800&access_token=' + token;
            var url = 'https://api.instagram.com/v1/users/self/media/recent/?count=200&access_token=' + token;
            request(url,function (error, response, body) {
                if (!error && response.statusCode == 200) {
                    console.log('got pics!');
                    res.send(response.body);
                }

                if (response.statusCode != 200) {
                    console.log(response);
                    res.send(response.body);
                }
            });
        }

        if (response.statusCode != 200){
            console.log(response);
        }
    })
});

router.get('/getPics/', function(req, res, next) {
    console.log('getting pics');
    var token = '';
    //var url = 'https://api.instagram.com/v1/tags/crookedspaces/media/recent/?access_token=16741082.1b07669.121a338d0cbe4ff6a5e04543158a4f82&lat=40.7128&lng=74.0059&distance=100000&min_timestamp=1272168000&max_timestamp=1461556800';
    //var url = 'https://api.instagram.com/v1/users/4940705/media/recent?access_token=4940705.5b9e1e6.03fdfd5d30994efd983465720e7883a0';
    var url =  'https://api.instagram.com/v1/users/18555911/media/recent?access_token=18555911.5b9e1e6.82f0f5988d614676b2afe8f7042fdd76&count=1000';

    request(url, function (error, response, body) {
        if (!error && response.statusCode == 200) {
            res.send(response.body);
        }
    });
});

router.get('/testget/', function(req, res, next) {
    console.log("request received");
});



module.exports = router;
