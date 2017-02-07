// turn a hash of key=values into an array of keys
angular
   .module('hc.Filters.toArray', [])
   .filter("toArray", function(){
      return function(obj) {
         var result = [];
         angular.forEach(obj, function(val, key) {
            result.push(val);
         });
         return result;
      };
   });

