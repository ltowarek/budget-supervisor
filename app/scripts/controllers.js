'use strict';

angular.module('BudgetSupervisor.controllers', [])

.controller('LoginController', function () {
})

.controller('SignUpController', function () {
})

.controller('HomeController', [function () {
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

.controller('CategoryDetailsController', ['$scope', '$state', '$stateParams', '$log', 'CategoriesService', function ($scope, $state, $stateParams, $log, CategoriesService) {
  $log.debug('State parameters:');
  $log.debug($stateParams);

  $scope.category = CategoriesService.get(parseInt($stateParams.id) || -1) || { id: -1, title: ''};

  $scope.save = function(category) {
    CategoriesService.save(category);
    //TODO: Handle form validation errors
    $state.go('categories');
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
