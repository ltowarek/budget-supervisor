'use strict';

angular.module('BudgetSupervisor.controllers', [])

.controller('FriendsCtrl', function($scope, Friends) {
  $scope.friends = Friends.all();
})

.controller('LoginController', function () {
})

.controller('SignUpController', function () {
})

.controller('HomeController', ['$log', function ($log) {
  $log.debug('Test');
}])

.controller('TransactionsController', function () {
})

.controller('TransactionDetailsController', function () {
})

.controller('CategoriesController', ['$scope', 'CategoriesService', function ($scope, CategoriesService) {
  $scope.config = {
    showDelete: false,
    showReorder: false
  };

  $scope.categories = CategoriesService.query();

  $scope.toggleDelete = function() {
    $scope.config.showReorder = false;
    $scope.config.showDelete = !$scope.config.showDelete;
  };

  $scope.toggleReorder = function() {
    $scope.config.showDelete = false;
    $scope.config.showReorder = !$scope.config.showReorder;
  };

  $scope.remove = function(id) {
    CategoriesService.remove(id);
  };

  $scope.reorder = function(item, fromIndex, toIndex) {
    CategoriesService.reorder(item, fromIndex, toIndex);
  };
}])

.controller('TagsController', function () {
})

.controller('RemindersController', function () {
})

.controller('ReminderDetailsController', function () {
})

.controller('SettingsController', function () {
})

.controller('StatisticsController', function () {
})

.controller('StatisticsBalanceController', function () {
});
