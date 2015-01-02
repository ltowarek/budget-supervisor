'use strict';

angular.module('BudgetSupervisor.controllers', [])

.controller('FriendsCtrl', function($scope, Friends) {
  $scope.friends = Friends.all();
})

.controller('LoginController', function () {
})

.controller('SignUpController', function () {
})

.controller('HomeController', function () {
})

.controller('TransactionsController', function () {
})

.controller('TransactionDetailsController', function () {
})

.controller('CategoriesController', function () {
})

.controller('TagsController', function () {
})

.controller('RemindersController', function () {
})

.controller('ReminderDetailsController', function () {
})

.controller('StatisticsController', function () {
})

.controller('StatisticsBalanceController', function () {
});
