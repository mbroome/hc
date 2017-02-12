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
   
   
