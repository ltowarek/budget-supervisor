'use strict';

angular.module('BudgetSupervisor.controllers', ['ngMessages'])

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
    showDelete: false
  };

  $scope.categories = CategoriesService.query();

  $scope.toggleDelete = function() {
    $scope.config.showDelete = !$scope.config.showDelete;
  };

  $scope.remove = function(id) {
    CategoriesService.remove(id);
  };
}])

.controller('CategoryDetailsController', ['$scope', '$state', '$stateParams', '$log', 'CategoriesService', function ($scope, $state, $stateParams, $log, CategoriesService) {
  $log.debug('State parameters:');
  $log.debug($stateParams);

  $scope.category = CategoriesService.get(parseInt($stateParams.id) || -1) || { id: -1, title: ''};

  $scope.save = function(category) {
    CategoriesService.save(category);
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
