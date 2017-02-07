// turn a hash of hashes of service variables into a flat array
angular
   .module('hc.Filters.flattenServiceVariables', [])
   .filter("flattenServiceVariables", function(){
      return function(rows) {
         var result = [];
         // data[sharecare2][mservices][terminus2][planet] = {'id': 'es.host', 'rec': ..., 'bucket': '/bob'}

         angular.forEach(rows, function(row, vlevel) {
            angular.forEach(row, function(v, k) {
               v.level = vlevel;
               result.push(v);
            });
         });
         return result;
      };
   });

