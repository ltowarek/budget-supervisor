'use strict';

/**
 * @namespace BudgetSupervisor.services
 */
angular.module('BudgetSupervisor.services', [])

/**
 * @class BudgetSupervisor.services.CategoriesService
 * @memberOf BudgetSupervisor.services
 * @description
 * The service is able to manage categories.
 */
.factory('CategoriesService', ['$log', function($log) {
  var categories = [
    { id: 0, title: 'Food'},
    { id: 1, title: 'Salary'},
    { id: 2, title: 'Miscellaneous'}
  ];

  $log.debug('Initial categories state:');
  $log.debug(categories);

  return {
    /**
     * @name get
     * @method
     * @memberOf BudgetSupervisor.services.CategoriesService
     * @param {number} id Category id.
     * @returns {?Object} Category object or null if a category is not found.
     */
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
    /**
     * @name save
     * @method
     * @memberOf BudgetSupervisor.services.CategoriesService
     * @param {Object} category Category object.
     * @description
     * The method creates a new category or updates existing one.
     */
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
    /**
     * @name query
     * @method
     * @memberOf BudgetSupervisor.services.CategoriesService
     * @returns {Object[]} Categories list.
     */
    query: function() {
      return categories;
    },
    /**
     * @name remove
     * @method
     * @memberOf BudgetSupervisor.services.CategoriesService
     * @param {number} id Category id.
     * @description
     * The method removes category from categories list.
     */
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
    /**
     * @name reorder
     * @method
     * @memberOf BudgetSupervisor.services.CategoriesService
     * @param {Object} item Category object.
     * @param {number} fromIndex Category's old array index.
     * @param {number} toIndex Category's new array index.
     * @description
     * The method reorders categories list.
     */
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
}])

/**
 * @class BudgetSupervisor.services.TagsService
 * @memberOf BudgetSupervisor.services
 * @description
 * The service is able to manage tags.
 */
.factory('TagsService', ['$log', function($log) {
  var tags = [
    { id: 0, title: 'Tesco'},
    { id: 1, title: 'Part-time job'},
    { id: 2, title: 'John'}
  ];

  $log.debug('Initial tags state:');
  $log.debug(tags);

  return {
    /**
     * @name get
     * @method
     * @memberOf BudgetSupervisor.services.TagsService
     * @param {number} id Tags id.
     * @returns {?Object} Tag object or null if a tag is not found.
     */
    get: function(id) {
      $log.debug('Get function executed with id: ' + id);

      var tagIndex = -1;

      for (var i = 0; i < tags.length; i++) {
        if (tags[i].id === id) {
          tagIndex = i;
          break;
        }
      }

      $log.debug('Tag index: ' + tagIndex);

      if (tagIndex > -1) {
        $log.debug('Tag found');
        return tags[tagIndex];
      } else {
        $log.debug('Tag not found');
        return null;
      }
    },
    /**
     * @name save
     * @method
     * @memberOf BudgetSupervisor.services.TagsService
     * @param {Object} tag Tag object.
     * @description
     * The method creates a new tag or updates existing one.
     */
    save: function(tag) {
      var i = 0;

      if (tag.id === -1) {
        var actualId = -1;

        for (i = 0; i < tags.length; i++) {
          if (tags[i].id > actualId) {
            actualId = tags[i].id;
          }
        }

        actualId++;

        $log.debug('Creating tag');
        tag.id = actualId;
        tags.push(tag);
      } else {
        var tagIndex = -1;

        for (i = 0; i < tags.length; i++) {
          if (tags[i].id === tag.id) {
            tagIndex = i;
            break;
          }
        }

        $log.debug('Tag index: ' + tagIndex);

        if (tagIndex > -1) {
          $log.debug('Updating tag');
          tags[tagIndex] = tag;
        }
      }

      $log.debug('Tags state after save function:');
      $log.debug(tags);
    },
    /**
     * @name query
     * @method
     * @memberOf BudgetSupervisor.services.TagsService
     * @returns {Object[]} Tags list.
     */
    query: function() {
      return tags;
    },
    /**
     * @name remove
     * @method
     * @memberOf BudgetSupervisor.services.TagsService
     * @param {number} id Tags id.
     * @description
     * The method removes tag from tags list.
     */
    remove: function(id) {
      $log.debug('Remove function executed with id: ' + id);

      var tagIndex = -1;

      for (var i = 0; i < tags.length; i++) {
        if (tags[i].id === id) {
          tagIndex = i;
          break;
        }
      }

      $log.debug('Tag index: ' + tagIndex);

      if (tagIndex > -1) {
        $log.debug('Removing tag');
        tags.splice(tagIndex, 1);
      }

      $log.debug('Tags state after remove function:');
      $log.debug(tags);
    },
    /**
     * @name reorder
     * @method
     * @memberOf BudgetSupervisor.services.TagsService
     * @param {Object} item Tag object.
     * @param {number} fromIndex Tag's old array index.
     * @param {number} toIndex Tag's new array index.
     * @description
     * The method reorders tags list.
     */
    reorder: function(item, fromIndex, toIndex) {
      $log.debug('Reorder function executed with parameters: item, fromIndex, toIndex');

      $log.debug(item);
      $log.debug(fromIndex);
      $log.debug(toIndex);

      $log.debug('Tags state before reload function:');
      $log.debug(tags);

      $log.debug('Reordering categories');
      tags.splice(fromIndex, 1);
      tags.splice(toIndex, 0, item);

      $log.debug('Tags state after reload function:');
      $log.debug(tags);
    }
  };
}]);
