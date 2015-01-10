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

.controller('TransactionsController', function () {
})

.controller('TransactionDetailsController', function () {
})

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
   * @method
   * @memberOf BudgetSupervisor.controllers.CategoriesController
   * @returns {Object[]} Categories list.
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

  $scope.category = CategoriesService.get(id) || { id: -1, title: ''};

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
   * @method
   * @memberOf BudgetSupervisor.controllers.TagsController
   * @returns {Object[]} Tags list.
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

  $scope.tag = TagsService.get(id) || { id: -1, title: ''};

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
