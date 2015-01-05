'use strict';

angular.module('BudgetSupervisor.controllers', ['ngMessages', 'ionic'])

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

.controller('CategoriesController', ['$scope', '$ionicPopup', 'CategoriesService', function ($scope, $ionicPopup, CategoriesService) {
  $scope.config = {
    showDelete: false
  };

  $scope.categories = CategoriesService.query();

  $scope.toggleDelete = function() {
    $scope.config.showDelete = !$scope.config.showDelete;
  };

  $scope.remove = function(id) {
    var confirmPopup = $ionicPopup.confirm({
      title: 'Delete category',
      template: 'Are you sure you want to delete this category?'
    });

    confirmPopup.then(function(response) {
      if (response) {
        CategoriesService.remove(id);
      }
    });
  };
}])

.controller('CategoryDetailsController', ['$scope', '$state', '$stateParams', '$log', 'CategoriesService', function ($scope, $state, $stateParams, $log, CategoriesService) {
  $log.debug('State parameters:');
  $log.debug($stateParams);

  var id = parseInt($stateParams.id);
  if (isNaN(id)) {
    id = -1;
  }

  $scope.category = CategoriesService.get(id) || { id: -1, title: ''};

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
