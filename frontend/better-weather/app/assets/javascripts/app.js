var app = angular.module('app', []);

var locations = [{
  name: 'New York, New York',
  latlng: [40.7128, -74.0059] // S / W is (-)
}, {
  name: 'Chicago, Illinois',
  latlng: [41.8781, -87.6298] // S / W is (-)
}];

// https://api.instagram.com/v1/media/search?lat=40.7128&lng=74.0059&MAX_TIMESTAMP=1/15/2014&MIN_TIMESTAMP=1/05/2014&client_id=1d6043231a2947b7b00b2707d4f5ace3&access_token=4940705.5b9e1e6.03fdfd5d30994efd983465720e7883a0

function ConvertDMSToDD(degrees, minutes, seconds, direction) {
    var dd = degrees + minutes/60 + seconds/(60*60);

    if (direction == "S" || direction == "W") {
        dd = dd * -1;
    } // Don't do anything for N or E
    return dd;
}

function ConvertDDToDMS(D, lng){
    return {
        dir : D<0?lng?'W':'S':lng?'E':'N',
        deg : 0|(D<0?D=-D:D),
        min : 0|D%1*60,
        sec :(0|D*60%1*6000)/100
    };
}

function ParseDMS(input) {
    var parts = input.split(/[^\d\w]+/);
    var lat = ConvertDMSToDD(parts[0], parts[1], parts[2], parts[3]);
    var lng = ConvertDMSToDD(parts[4], parts[5], parts[6], parts[7]);
}

function parseLatLngToDegress(latlng) {

}


// Decimal Degrees = Degrees + minutes/60 + seconds/3600

app.controller('DashboardCtrl', function MainCtrl($scope, $http) {
  console.log('DashboardCtrl');
  $scope.test = 'hello';

  $http

  var today = new Date();
  // before Sunset (7:45PM) && after Sunrise (6:03AM)
  $scope.isDaytime = today.getHours() > (12+7 + 45/60) && today.getHours() > (6 + 3/60);

  $scope.stub = {
    currentWeather: {
      image: 'http://sdfd.com/someimage.png',
      low: 42,
      high: 75,
      descriptor: 'heavy rain' // day & night; no sep
    },
    pastWeather: [{
      image: 'http://sdfd.com/someimage.png',
      low: 42,
      high: 75,
      descriptor: 'heavy rain' // day & night; no sep
    }],
    emotions: { // ranges from 0 to 1 (in severity)
      angry: 0.8,
      sad: 0.5,
      happy: 0.3,
      contempt: 0.75,
      neutral: 0.05,
      disgust: 0.4
    }
  };

  // filtered for outdoors
  $scope.pastWeather = $scope.stub.pastWeather;

  $scope.avgTemp = function(weatherObj) {
    return (weatherObj.low + weatherObj.high) / 2;
  };
});

