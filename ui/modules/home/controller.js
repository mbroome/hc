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
