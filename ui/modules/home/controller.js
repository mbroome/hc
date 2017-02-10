﻿angular.module('hc.Home', [])
   .controller('HomeController',
      ['ScenesClient', 'StateClient', 'DevicesClient', 'LogsClient', '$scope', '$timeout', '$interval',
      function(ScenesClient, StateClient, DevicesClient, LogsClient, $scope, $timeout, $interval) {
         $scope.StateClient = StateClient;
         $scope.DevicesClient = DevicesClient;
         $scope.LogsClient = LogsClient;
         $scope.ScenesClient = ScenesClient;

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
         };

         // just update state
         $scope.updateState = function(){
            $scope.StateClient.get(function(o){
               $scope.LogsClient.get();
            });
         };

         // update devices and state
         $scope.update = function(){
//console.log('update time');
            $scope.DevicesClient.get(function(o){
//console.log(o);
               $scope.StateClient.get(function(o){ });
//console.log(o);
            });
         };

      }]);
