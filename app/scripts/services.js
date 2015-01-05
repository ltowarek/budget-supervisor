'use strict';

angular.module('BudgetSupervisor.services', [])

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
      $log.debug('Get function executed with id: ' + id);

      var categoryIndex = -1;

      for (var i = 0; i < categories.length; i++) {
        if (categories[i].id === id) {
          categoryIndex = i;
          break;
        }
      }

      $log.debug('Category index: ' + categoryIndex);

      if (categoryIndex > -1) {
        $log.debug('Category found');
        return categories[categoryIndex];
      } else {
        $log.debug('Category not found');
        return null;
      }
    },
    save: function(category) {
      var i = 0;

      if (category.id === -1) {
        var actualId = -1;

        for (i = 0; i < categories.length; i++) {
          if (categories[i].id > actualId) {
            actualId = categories[i].id;
          }
        }

        actualId++;

        $log.debug('Creating category');
        category.id = actualId;
        categories.push(category);
      } else {
        var categoryIndex = -1;

        for (i = 0; i < categories.length; i++) {
          if (categories[i].id === category.id) {
            categoryIndex = i;
            break;
          }
        }

        $log.debug('Category index: ' + categoryIndex);

        if (categoryIndex > -1) {
          $log.debug('Updating category');
          categories[categoryIndex] = category;
        }
      }

      $log.debug('Categories state after save function:');
      $log.debug(categories);
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
        $log.debug('Removing category');
        categories.splice(categoryIndex, 1);
      }

      $log.debug('Categories state after remove function:');
      $log.debug(categories);
    },
    reorder: function(item, fromIndex, toIndex) {
      $log.debug('Reorder function executed with parameters: item, fromIndex, toIndex');

      $log.debug(item);
      $log.debug(fromIndex);
      $log.debug(toIndex);

      $log.debug('Categories state before reload function:');
      $log.debug(categories);

      $log.debug('Reordering categories');
      categories.splice(fromIndex, 1);
      categories.splice(toIndex, 0, item);

      $log.debug('Categories state after reload function:');
      $log.debug(categories);
    }
  };
}]);
