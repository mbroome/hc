// we need to be able to tell if an object is empty rather
// than just a simple check
angular
   .module('hc.Filters.isEmpty', [])
   .filter("isEmpty", function(){
      return function(object) {
         return angular.equals({}, object);
      };
   });

