// turn a hash of key=values into an array of keys
// if the value's state field is true
angular
   .module('hc.Filters.toArrayByState', [])
   .filter("toArrayByState", function(){
      return function(obj) {
         var result = [];

         var enabled = [];
         var disabled = [];

         angular.forEach(obj, function(val, key) {
            if(val.state){
               enabled.push(val.id);
            }else{
               disabled.push(val.id);
            }
         });

         enabled.sort();
         result = enabled.concat(disabled.sort());

         return result;
      };
   });

