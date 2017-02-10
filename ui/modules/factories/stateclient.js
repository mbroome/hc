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
   
   
