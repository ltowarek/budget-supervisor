'use strict';
angular.module('BudgetSupervisor.services', [])

/**
 * A simple example service that returns some data.
 */
.factory('Friends', function() {
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var friends = [
    { id: 0, name: 'Scruff McGruff' },
    { id: 1, name: 'G.I. Joe' },
    { id: 2, name: 'Miss Frizzle' },
    { id: 3, name: 'Ash Ketchum' }
  ];

  return {
    all: function() {
      return friends;
    },
    get: function(friendId) {
      // Simple index lookup
      return friends[friendId];
    }
  };
})

.factory('CategoriesService', ['$log', function($log) {
  var categories = [
    { id: 0, title: 'Food'},
    { id: 1, title: 'Salary'},
    { id: 2, title: 'Miscellaneous'}
  ];

  $log.debug('Initial categories state:');
  $log.debug(categories);

  return {
    get: function(id) {
      var categoryIndex = -1;

      for (var i = 0; i < categories.length; i++) {
        if (categories[i].id === id) {
          categoryIndex = i;
          break;
        }
      }

      if (categoryIndex > -1) {
        return categories[categoryIndex];
      }
    },
    save: function(category) {
      categories.push(category);
    },
    query: function() {
      return categories;
    },
    remove: function(id) {
      $log.debug('Remove function executed with id: ' + id);

      var categoryIndex = -1;

      for (var i = 0; i < categories.length; i++) {
        if (categories[i].id === id) {
          categoryIndex = i;
          break;
        }
      }

      $log.debug('Category index: ' + categoryIndex);

      if (categoryIndex > -1) {
        categories.splice(categoryIndex, 1);
      }

      $log.debug('Categories state after remove function:');
      $log.debug(categories);
    },
    reorder: function(item, fromIndex, toIndex) {
      categories.splice(fromIndex, 1);
      categories.splice(toIndex, 0, item);
    }
  };
}]);
