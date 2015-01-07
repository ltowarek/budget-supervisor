'use strict';

/**
 * @namespace BudgetSupervisor
 */
angular.module('BudgetSupervisor', ['ionic', 'config', 'BudgetSupervisor.controllers', 'BudgetSupervisor.services'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    if(window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
    }
    if(window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
  });
})

.config(function($stateProvider, $urlRouterProvider) {

  $stateProvider

    .state('login', {
      url: '/login',
      templateUrl: '/templates/login.html',
      controller: 'LoginController'
    })

    .state('sign-up', {
      url: '/signup',
      templateUrl: '/templates/signup.html',
      controller: 'SignUpController'
    })

    .state('home', {
      url: '/',
      templateUrl: '/templates/home.html',
      controller: 'HomeController'
    })

    .state('transactions', {
      url: '/transactions',
      templateUrl: '/templates/transactions.html',
      controller: 'TransactionsController'
    })

    .state('transaction-details', {
      url: '/transactions/:id',
      templateUrl: '/templates/transactiondetails.html',
      controller: 'TransactionDetailsController'
    })

    .state('categories', {
      url: '/categories',
      templateUrl: '/templates/categories.html',
      controller: 'CategoriesController'
    })

    .state('category-details', {
      url: '/categories/:id',
      templateUrl: '/templates/categorydetails.html',
      controller: 'CategoryDetailsController'
    })

    .state('tags', {
      url: '/tags',
      templateUrl: '/templates/tags.html',
      controller: 'TagsController'
    })

    .state('reminders', {
      url: '/reminders',
      templateUrl: '/templates/reminders.html',
      controller: 'RemindersController'
    })

    .state('reminder-details', {
      url: '/reminders/:id',
      templateUrl: '/templates/reminderdetails.html',
      controller: 'ReminderDetailsController'
    })

    .state('statistics', {
      url: '/statistics',
      templateUrl: '/templates/statistics.html',
      controller: 'StatisticsController'
    })

    .state('statistics-balance', {
      url: '/statistics/balance',
      templateUrl: '/templates/statisticsbalance.html',
      controller: 'StatisticsBalanceController'
    })

    .state('settings', {
      url: '/settings',
      templateUrl: '/templates/settings.html',
      controller: 'SettingsController'
    })
  ;

    // if none of the above states are matched, use this as the fallback

  $urlRouterProvider.otherwise('/');

});

