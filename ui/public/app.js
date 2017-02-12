var featureDisableList = {};

// declare modules
var app = angular.module('app', [
   'templates',
   'ngRoute',
   'LocalStorageModule',
   'base64',
   'ui.bootstrap',
   'ngAnimate',
   'ngSanitize',

   'hc.Home',
   'hc.Filters.toArray',
   'hc.Filters.toArrayByState',
   'hc.Filters.isEmpty',
   'hc.Filters.flattenServiceVariables',
   'hc.Filters.firstLetter',
   'hc.Filters.toArrayID',

   'hc.Factories.InputBox',
   'hc.Factories.StateClient',
   'hc.Factories.DevicesClient',
   'hc.Factories.LogsClient',
   'hc.Factories.ScenesClient',
   'hc.Factories.JobsClient',
]);


app.config(['$routeProvider', function ($routeProvider) {
   $routeProvider
      .when('/', {
         controller: 'HomeController',
         //templateUrl: 'modules/home/views/home.html'
         templateUrl: 'home.html'
      })

      .otherwise({ redirectTo: '/' });
}]);



angular
   .module('hc.Factories.DevicesClient', [])
   .factory('DevicesClient',
      ['$http', '$interval',
      function DevicesClient($http, $interval) {
         var DevicesClient = {};
         DevicesClient.hostname = '/api';
         

         ///////////////////////////////////////////////////////////////////
         // make a unix timestamp
         DevicesClient.now = function(){
            return(Math.floor(Date.now() / 1000));
         };
   
         // do a http get of cumulus
         DevicesClient.get = function(callback){
            var s = this;

            var url = DevicesClient.hostname + '/devices';
            $http.get(url)
               // success
               .then(function(response) {
                  s.data = response.data.data;
                  if(callback){
                     callback(response.data.data);
                  }
               },
               // error
               function(response){
                  if(callback){
                     callback(response.data);
                  }
               });
         };
   
         DevicesClient.get(function(o){
            $interval(function(){
                                   console.log('update devicesclient from interval');
                                   DevicesClient.get();
                                }, 60000*3);
         });

         return(DevicesClient);
   
      }
   ]);
   
   

angular
   .module('hc.Factories.InputBox', [])
   .factory('prompt',
      ['$uibModal','$q',
      function($uibModal,$q){
         var prompt = function(options){

             var defaults = {
                 title: '',
                 message: '',
                 input: false,
                 inputs: {},
                 label: '',
                 labels: [],
                 value: '',
                 values: false,
                 buttons: [
                     {label:'Cancel',cancel:true},
                     {label:'OK',primary:true}
                 ]
             };

             if (options === undefined){
                 options = {};
             }

             for (var key in defaults) {
                 if (options[key] === undefined) {
                     options[key] = defaults[key];
                 }
             }

             var defer = $q.defer();

             $uibModal.open({
                 templateUrl:'inputbox/views/inputbox.html',
                 controller: 'inputPromptCtrl',
                 resolve: {
                     options:function(){
                         return options;
                     }
                 }
             }).result.then(function(result){
                 if (Object.keys(result.inputs).length){
                     defer.resolve(result.inputs);
                 }else if (options.input){
                     defer.resolve(result.input);
                 } else {
                     defer.resolve(result.button);
                 }
             }, function(){
                 defer.reject();
             });

             return defer.promise;
         };

         return prompt;
         }
      ]);




angular
   .module('hc.Factories.JobsClient', [])
   .factory('JobsClient',
      ['$http', '$interval',
      function JobsClient($http, $interval) {
         var JobsClient = {};
         JobsClient.hostname = '/api';
         

         ///////////////////////////////////////////////////////////////////
         // make a unix timestamp
         JobsClient.now = function(){
            return(Math.floor(Date.now() / 1000));
         };
   
         JobsClient.get = function(callback){
            var s = this;

            var url = JobsClient.hostname + '/jobs/status';
            $http.get(url)
               // success
               .then(function(response) {
                  s.data = response.data.data;
                  if(callback){
                     callback(response.data.data);
                  }
               },
               // error
               function(response){
                  if(callback){
                     callback(response.data);
                  }
               });
         };
   

         JobsClient.get(function(o){
            $interval(function(){ 
                                   console.log('update jobsclient from interval');
                                   JobsClient.get(); 
                                }, 60000*5); 
         });
   
         return(JobsClient);
   
      }
   ]);
   
   

angular
   .module('hc.Factories.LogsClient', [])
   .factory('LogsClient',
      ['$http', '$interval',
      function LogsClient($http, $interval) {
         var LogsClient = {};
         LogsClient.hostname = '/api';
         

         ///////////////////////////////////////////////////////////////////
         // make a unix timestamp
         LogsClient.now = function(){
            return(Math.floor(Date.now() / 1000));
         };
   
         // do a http get of cumulus
         LogsClient.get = function(callback){
            var s = this;

            var url = LogsClient.hostname + '/logs';
            $http.get(url)
               // success
               .then(function(response) {
                  s.data = response.data.data;
                  if(callback){
                     callback(response.data.data);
                  }
               },
               // error
               function(response){
                  if(callback){
                     callback(response.data);
                  }
               });
         };
   
         LogsClient.get(function(o){
            $interval(function(){ 
                                   console.log('update logsclient from interval');
                                   LogsClient.get(); 
                                }, 60000*5);
         });
   
         return(LogsClient);
   
      }
   ]);
   
   

angular
   .module('hc.Factories.ScenesClient', [])
   .factory('ScenesClient',
      ['$http', '$interval',
      function ScenesClient($http, $interval) {
         var ScenesClient = {};
         ScenesClient.hostname = '/api';
         

         ///////////////////////////////////////////////////////////////////
         // make a unix timestamp
         ScenesClient.now = function(){
            return(Math.floor(Date.now() / 1000));
         };
   
         ScenesClient.get = function(callback){
            var s = this;

            var url = ScenesClient.hostname + '/scene';
            $http.get(url)
               // success
               .then(function(response) {
                  s.data = response.data.data;
                  if(callback){
                     callback(response.data.data);
                  }
               },
               // error
               function(response){
                  if(callback){
                     callback(response.data);
                  }
               });
         };
   

         ScenesClient.run = function(sceneid, callback){
            var s = this;

            var url = ScenesClient.hostname + '/scene/run/' + sceneid;
            $http.get(url)
               // success
               .then(function(response) {
                  if(callback){
                     callback(response.data.data);
                  }
               },
               // error
               function(response){
                  if(callback){
                     callback(response.data);
                  }
               });
         };

         ScenesClient.get(function(o){
            $interval(function(){ 
                                   console.log('update scenesclient from interval');
                                   ScenesClient.get(); 
                                }, 60000*5); 
         });
   
         return(ScenesClient);
   
      }
   ]);
   
   

angular
   .module('hc.Factories.StateClient', [])
   .factory('StateClient',
      ['$http', '$interval',
      function StateClient($http, $interval) {
         var StateClient = {};
         StateClient.hostname = '/api';
         

         ///////////////////////////////////////////////////////////////////
         // make a unix timestamp
         StateClient.now = function(){
            return(Math.floor(Date.now() / 1000));
         };
   
         // do a http get of cumulus
         StateClient.get = function(callback){
            var s = this;

            var url = StateClient.hostname + '/state';
            $http.get(url)
               // success
               .then(function(response) {
                  s.data = response.data.data;
                  if(callback){
                     callback(response.data.data);
                  }
               },
               // error
               function(response){
                  if(callback){
                     callback(response.data);
                  }
               });
         };
   
         // do a http put of cumulus
         StateClient.post = function(request, callback){
            var s = this;
   
            // ensure we don't have duplicate slashes
            //request.url = request.url.replace(/\/\/+/g, '/');
            var url = StateClient.hostname + '/state/sensor/' + request.sensor;

            // make the request with the authorization header set
            $http.post(url, "state=" + request.data, request.content)
               // success
               .then(function(response) {
                  if(callback){
                     callback(response.data);
                  }
               },
               // error
               function(response){
                  if(callback){
                     callback(response.data);
                  }
               });
         };

         StateClient.get(function(o){
            $interval(function(){ 
                                   console.log('update stateclient from interval');
                                   StateClient.get(); 
                                }, 60000*3);
         });
   
         return(StateClient);
   
      }
   ]);
   
   

// turn a hash of key=values into an array of keys
angular
   .module('hc.Filters.firstLetter', [])
   .filter("firstLetter", function(){
      return function(input) {
         var output = input[0].toUpperCase();
         return output;
      };
   });



// turn a hash of hashes of service variables into a flat array
angular
   .module('hc.Filters.flattenServiceVariables', [])
   .filter("flattenServiceVariables", function(){
      return function(rows) {
         var result = [];
         // data[sharecare2][mservices][terminus2][planet] = {'id': 'es.host', 'rec': ..., 'bucket': '/bob'}

         angular.forEach(rows, function(row, vlevel) {
            angular.forEach(row, function(v, k) {
               v.level = vlevel;
               result.push(v);
            });
         });
         return result;
      };
   });


// we need to be able to tell if an object is empty rather
// than just a simple check
angular
   .module('hc.Filters.isEmpty', [])
   .filter("isEmpty", function(){
      return function(object) {
         return angular.equals({}, object);
      };
   });


// turn a hash of key=values into an array of keys
angular
   .module('hc.Filters.toArray', [])
   .filter("toArray", function(){
      return function(obj) {
         var result = [];
         angular.forEach(obj, function(val, key) {
            result.push(val);
         });
         return result;
      };
   });


// turn a hash of key=values into an array of keys
// if the value's state field is true
angular
   .module('hc.Filters.toArrayByState', [])
   .filter("toArrayByState", function(){
      return function(obj) {
         var result = [];

         var enabled = [];
         var disabled = [];

         angular.forEach(obj, function(val, key) {
            if(val.state){
               enabled.push(val.id);
            }else{
               disabled.push(val.id);
            }
         });

         enabled.sort();
         result = enabled.concat(disabled.sort());

         return result;
      };
   });


// turn a hash of key=values into an array of keys
angular
   .module('hc.Filters.toArrayID', [])
   .filter("toArrayID", function(){
      return function(obj) {
         var result = [];
         angular.forEach(obj, function(val, key) {
            val.id = key;
            result.push(val);
         });
         return result;
      };
   });


angular.module('hc.Home', [])
   .controller('HomeController',
      ['JobsClient', 'ScenesClient', 'StateClient', 'DevicesClient', 'LogsClient', '$scope', '$timeout', '$interval',
      function(JobsClient, ScenesClient, StateClient, DevicesClient, LogsClient, $scope, $timeout, $interval) {
         $scope.StateClient = StateClient;
         $scope.DevicesClient = DevicesClient;
         $scope.LogsClient = LogsClient;
         $scope.ScenesClient = ScenesClient;
         $scope.JobsClient = JobsClient;

         // whena button is pressed
         $scope.changeState = function(id){
            var state = $scope.StateClient.data[id].value ? 0 : 1;
            $scope.StateClient.post({'sensor': id, 'data': state}, function(o){
               $timeout($scope.updateState, 5000);
            });
         };

         // testing
         $scope.test = function(){
            console.log($scope.DevicesClient.data);
            console.log($scope.StateClient.data);
            console.log($scope.LogsClient.data);
            console.log($scope.ScenesClient.data);
            console.log($scope.JobsClient.data);
         };

         // just update state
         $scope.updateState = function(){
            $scope.StateClient.get(function(o){
               $scope.LogsClient.get(function(s){
                  $scope.JobsClient.get();
               });
            });
         };

         // update devices and state
         $scope.update = function(){
            $scope.DevicesClient.get(function(o){
               $scope.StateClient.get(function(o){ });
            });
         };


         $scope.runScene = function(sceneid){
            $scope.ScenesClient.run(sceneid, function(o){
               $timeout($scope.updateState, 5000);
            });
         };

      }]);

angular
   .module('hc.Components.Overview', ['ui.bootstrap', 'ngSanitize'])
   .controller('OverviewController',
      ['$sce', '$scope',
      function($sce, $scope) {
         $scope.test = function(){
console.log('testing from overview');
         };


      }]);



