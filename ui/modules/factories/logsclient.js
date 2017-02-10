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
   
   
