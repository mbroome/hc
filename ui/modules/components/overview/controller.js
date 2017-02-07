angular
   .module('hc.Components.Overview', ['ui.bootstrap', 'ngSanitize'])
   .controller('OverviewController',
      ['$sce', '$scope',
      function($sce, $scope) {
         $scope.test = function(){
console.log('testing from overview');
         };


      }]);



