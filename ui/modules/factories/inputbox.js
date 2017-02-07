angular
   .module('hc.Factories.InputBox', [])
   .factory('prompt',
      ['$uibModal','$q',
      function($uibModal,$q){
         var prompt = function(options){

             var defaults = {
                 title: '',
                 message: '',
                 input: false,
                 inputs: {},
                 label: '',
                 labels: [],
                 value: '',
                 values: false,
                 buttons: [
                     {label:'Cancel',cancel:true},
                     {label:'OK',primary:true}
                 ]
             };

             if (options === undefined){
                 options = {};
             }

             for (var key in defaults) {
                 if (options[key] === undefined) {
                     options[key] = defaults[key];
                 }
             }

             var defer = $q.defer();

             $uibModal.open({
                 templateUrl:'inputbox/views/inputbox.html',
                 controller: 'inputPromptCtrl',
                 resolve: {
                     options:function(){
                         return options;
                     }
                 }
             }).result.then(function(result){
                 if (Object.keys(result.inputs).length){
                     defer.resolve(result.inputs);
                 }else if (options.input){
                     defer.resolve(result.input);
                 } else {
                     defer.resolve(result.button);
                 }
             }, function(){
                 defer.reject();
             });

             return defer.promise;
         };

         return prompt;
         }
      ]);



