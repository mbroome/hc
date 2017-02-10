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
   

         ScenesClient.run = function(request, callback){
            var s = this;

            var url = ScenesClient.hostname + '/scene/' + request.scene;
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
/*            $interval(function(){ 
                                   //console.log('update stateclient from interval');
                                   ScenesClient.get(); 
                                }, 60000*5); */
         });
   
         return(ScenesClient);
   
      }
   ]);
   
   
