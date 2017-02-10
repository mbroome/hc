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


