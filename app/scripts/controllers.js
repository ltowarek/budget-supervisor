'use strict';

/**
 * @namespace BudgetSupervisor.controllers
 */
angular.module('BudgetSupervisor.controllers', ['ngMessages', 'ionic'])

.controller('LoginController', function () {
})

.controller('SignUpController', function () {
})

.controller('HomeController', [function () {
}])

/**
 * @class BudgetSupervisor.controllers.TransactionsController
 * @memberOf BudgetSupervisor.controllers
 * @description
 * The controller is able to list all transactions or delete existing ones.
 */
.controller('TransactionsController', ['$scope', '$ionicPopup', 'TransactionsService', function ($scope, $ionicPopup, TransactionsService) {
  $scope.config = {
    showDelete: false
  };

  /**
   * @name $scope.transactions
   * @property {Object[]} Transactions list.
   * @memberOf BudgetSupervisor.controllers.TransactionsController
   */
  $scope.transactions = TransactionsService.query();

  /**
   * @name $scope.toggleDelete
   * @method
   * @memberOf BudgetSupervisor.controllers.TransactionsController
   * @description
   * The method toggles delete buttons.
   */
  $scope.toggleDelete = function() {
    $scope.config.showDelete = !$scope.config.showDelete;
  };

  /**
   * @name $scope.remove
   * @method
   * @memberOf BudgetSupervisor.controllers.TransactionsController
   * @param {number} id Transactions id.
   * @description
   * The method shows deletion confirmation and if it is confirmed removes transaction.
   */
  $scope.remove = function(id) {
    var confirmPopup = $ionicPopup.confirm({
      title: 'Delete transaction',
      template: 'Are you sure you want to delete this transaction?'
    });

    confirmPopup.then(function(response) {
      if (response) {
        TransactionsService.remove(id);
      }
    });
  };
}])

/**
 * @class BudgetSupervisor.controllers.TransactionDetailsController
 * @memberOf BudgetSupervisor.controllers
 * @description
 * The controller is able to edit existing transaction or create a new one.
 *
 * If a transaction id is not present in $stateParams or is a NaN or is not present in TransactionsService then a new category template will be used.
 * Otherwise existing editable transaction will be fetched.
 */
.controller('TransactionDetailsController', ['$scope', '$state', '$stateParams', '$log', 'TransactionsService', 'CategoriesService', 'TagsService',  function ($scope, $state, $stateParams, $log, TransactionsService, CategoriesService, TagsService) {
  $log.debug('State parameters:');
  $log.debug($stateParams);

  var id = parseInt($stateParams.id);
  if (isNaN(id)) {
    id = -1;
  }

  $scope.transaction = angular.copy(TransactionsService.get(id)) || { id: -1, title: null, value: null, date: '', category: null, tags: null, description: null};
  $scope.categories = CategoriesService.query();
  $scope.tags = TagsService.query();

  // Parse a date
  $scope.transaction.date = new Date($scope.transaction.date);

  /**
   * @name $scope.save
   * @method
   * @memberOf BudgetSupervisor.controllers.TransactionDetailsController
   * @param {Object} transaction Transaction object.
   * @description
   * The method saves transaction and redirects to transactions state.
   */
  $scope.save = function(transaction) {
    // Parse a date
    transaction.date = transaction.date.toISOString().split('T')[0];
    TransactionsService.save(transaction);
    $state.go('transactions');
  };
}])

/**
 * @class BudgetSupervisor.controllers.CategoriesController
 * @memberOf BudgetSupervisor.controllers
 * @description
 * The controller is able to list all categories or delete existing ones.
 */
.controller('CategoriesController', ['$scope', '$ionicPopup', 'CategoriesService', function ($scope, $ionicPopup, CategoriesService) {
  $scope.config = {
    showDelete: false
  };

  /**
   * @name $scope.categories
   * @property {Object[]} Categories list.
   * @memberOf BudgetSupervisor.controllers.CategoriesController
   */
  $scope.categories = CategoriesService.query();

  /**
   * @name $scope.toggleDelete
   * @method
   * @memberOf BudgetSupervisor.controllers.CategoriesController
   * @description
   * The method toggles delete buttons.
   */
  $scope.toggleDelete = function() {
    $scope.config.showDelete = !$scope.config.showDelete;
  };

  /**
   * @name $scope.remove
   * @method
   * @memberOf BudgetSupervisor.controllers.CategoriesController
   * @param {number} id Category id.
   * @description
   * The method shows deletion confirmation and if it is confirmed removes category.
   */
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

/**
 * @class BudgetSupervisor.controllers.CategoryDetailsController
 * @memberOf BudgetSupervisor.controllers
 * @description
 * The controller is able to edit existing category or create a new one.
 *
 * If a category id is not present in $stateParams or is a NaN or is not present in CategoriesService then a new category template will be used.
 * Otherwise existing editable category will be fetched.
 */
.controller('CategoryDetailsController', ['$scope', '$state', '$stateParams', '$log', 'CategoriesService', function ($scope, $state, $stateParams, $log, CategoriesService) {
  $log.debug('State parameters:');
  $log.debug($stateParams);

  var id = parseInt($stateParams.id);
  if (isNaN(id)) {
    id = -1;
  }

  $scope.category = angular.copy(CategoriesService.get(id)) || { id: -1, title: ''};

  /**
   * @name $scope.save
   * @method
   * @memberOf BudgetSupervisor.controllers.CategoryDetailsController
   * @param {Object} category Category object.
   * @description
   * The method saves category and redirects to categories state.
   */
  $scope.save = function(category) {
    CategoriesService.save(category);
    $state.go('categories');
  };
}])

/**
 * @class BudgetSupervisor.controllers.TagsController
 * @memberOf BudgetSupervisor.controllers
 * @description
 * The controller is able to list all tags or delete existing ones.
 */
.controller('TagsController', ['$scope', '$ionicPopup', 'TagsService', function ($scope, $ionicPopup, TagsService) {
  $scope.config = {
    showDelete: false
  };

  /**
   * @name $scope.tags
   * @property {Object[]} Tags list.
   * @memberOf BudgetSupervisor.controllers.TagsController
   */
  $scope.tags = TagsService.query();

  /**
   * @name $scope.toggleDelete
   * @method
   * @memberOf BudgetSupervisor.controllers.TagsController
   * @description
   * The method toggles delete buttons.
   */
  $scope.toggleDelete = function() {
    $scope.config.showDelete = !$scope.config.showDelete;
  };

  /**
   * @name $scope.remove
   * @method
   * @memberOf BudgetSupervisor.controllers.TagsController
   * @param {number} id Tags id.
   * @description
   * The method shows deletion confirmation and if it is confirmed removes tag.
   */
  $scope.remove = function(id) {
    var confirmPopup = $ionicPopup.confirm({
      title: 'Delete tag',
      template: 'Are you sure you want to delete this tag?'
    });

    confirmPopup.then(function(response) {
      if (response) {
        TagsService.remove(id);
      }
    });
  };
}])

/**
 * @class BudgetSupervisor.controllers.TagDetailsController
 * @memberOf BudgetSupervisor.controllers
 * @description
 * The controller is able to edit existing tag or create a new one.
 *
 * If a tag id is not present in $stateParams or is a NaN or is not present in TagsService then a new tag template will be used.
 * Otherwise existing editable tag will be fetched.
 */
.controller('TagDetailsController', ['$scope', '$state', '$stateParams', '$log', 'TagsService', function ($scope, $state, $stateParams, $log, TagsService) {
  $log.debug('State parameters:');
  $log.debug($stateParams);

  var id = parseInt($stateParams.id);
  if (isNaN(id)) {
    id = -1;
  }

  $scope.tag = angular.copy(TagsService.get(id)) || { id: -1, title: ''};

  /**
   * @name $scope.save
   * @method
   * @memberOf BudgetSupervisor.controllers.TagDetailsController
   * @param {Object} tag Tag object.
   * @description
   * The method saves tag and redirects to tags state.
   */
  $scope.save = function(tag) {
    TagsService.save(tag);
    $state.go('tags');
  };
}])

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
