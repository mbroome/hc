angular.module('templates', []).run(['$templateCache', function($templateCache) {$templateCache.put('overview/views/overview.html','<div ng-controller="OverviewController">\noverview\n\n<label class="btn btn-warning" ng-click="test()">Overview::Test</label>\n</div>\n');
$templateCache.put('home.html','<div ng-controller="HomeController">\n   <div class="container-fluid">\n      <div class="row no-gutters">\n         <label class="btn btn-warning" ng-click="update()">Refresh</label>\n      </div>\n      <div class="row no-gutters">\n         <div class="col-lg-9">\n            <table class="table">\n               <thead>\n                  <tr>\n                     <th>SensorID</th>\n                     <th>Name</th>\n                     <th>Value</th>\n                     <th>Time</th>\n               </thead>\n               <tr ng-repeat="statefield in StateClient.data | toArray | orderBy: \'id\'">\n                  <td>{{statefield.id}}</td>\n                  <td>{{DevicesClient.data.sensors[statefield.id].name}}</td>\n                  <td>\n                     <div ng-if="DevicesClient.data.sensors[statefield.id].type == 3">\n                        <label class="btn btn-warning" ng-click="changeState(statefield.id)">{{statefield.value}}</label>\n                     </div>\n                     <div ng-if="DevicesClient.data.sensors[statefield.id].type != 3">{{statefield.value}}</div>\n                  </td>\n                  <td>{{statefield.time * 1000| date:\'yyyy-MM-dd HH:mm:ss Z\'}}</td>\n               </tr>\n            </table>\n         </div>\n         <div class="col-lg-3">\n            <table class="table">\n               <thead>\n                  <tr>\n                     <th>Scene</th>\n                     <th>Description</th>\n               </thead>\n               <tr ng-repeat="scenefield in ScenesClient.data | orderBy: \'id\'">\n                  <td>{{scenefield.id}}</td>\n                  <td>{{scenefield.description}}</td>\n               </tr>\n            </table>\n\n         </div>\n      </div>\n      <div class="row no-gutters">\n         <table class="table">\n            <thead>\n               <tr>\n                  <th>Time</th>\n                  <th>Data</th>\n            </thead>\n            <tr ng-repeat="logfield in LogsClient.data | toArray | orderBy:\'-\'">\n               <td width=200>{{logfield.time * 1000| date:\'yyyy-MM-dd HH:mm:ss Z\'}}</td>\n               <td>{{logfield.data}}</td>\n            </tr>\n         </table>\n      </div>\n   </div>\n   <label class="btn btn-warning" ng-click="test()">Home::Test</label>\n</div>\n   \n');}]);