// turn a hash of key=values into an array of keys
angular
   .module('hc.Filters.firstLetter', [])
   .filter("firstLetter", function(){
      return function(input) {
         var output = input[0].toUpperCase();
         return output;
      };
   });


