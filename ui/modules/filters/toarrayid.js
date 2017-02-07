// turn a hash of key=values into an array of keys
angular
   .module('hc.Filters.toArrayID', [])
   .filter("toArrayID", function(){
      return function(obj) {
         var result = [];
         angular.forEach(obj, function(val, key) {
            val.id = key;
            result.push(val);
         });
         return result;
      };
   });

