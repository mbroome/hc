angular
   .module('hc.Factories.DevicesClient', [])
   .factory('DevicesClient',
      ['$http', '$interval',
      function DevicesClient($http, $interval) {
         var DevicesClient = {};
         DevicesClient.hostname = 'http://192.168.1.79:8080/api';
         

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
                                   //console.log('update devicesclient from interval');
                                   DevicesClient.get();
                                }, 60000*5);
         });

         return(DevicesClient);
   
      }
   ]);
   
   
