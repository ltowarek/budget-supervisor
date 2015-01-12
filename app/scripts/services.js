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
}])

/**
 * @class BudgetSupervisor.services.TransactionsService
 * @memberOf BudgetSupervisor.services
 * @description
 * The service is able to manage transactions.
 */
.factory('TransactionsService', ['$log', function($log) {
  var transactions = [
    { id: 0, title: 'Eggs', value: 5.50, date: 'Sep 3, 2010', category: { id: 0, title: 'Food'}, tags: [{ id: 0, title: 'Tesco'}], description: '10 eggs'},
    { id: 1, title: 'Tesco salary', value: 2000.00, date: 'Sep 10, 2010', category: { id: 1, title: 'Salary'}, tags: [{ id: 0, title: 'Tesco'}, { id: 1, title: 'Part-time job'}], description: ''},
    { id: 2, title: 'Lottery', value: 3.50, date: 'Sep 8, 2010', category: { id: 0, title: 'Miscellaneous'}, tags: [], description: 'Number: 1, 2, 3, 4, 5\nLottery day: Sep 9, 2010'}
  ];

  $log.debug('Initial transactions state:');
  $log.debug(transactions);

  return {
    /**
     * @name get
     * @method
     * @memberOf BudgetSupervisor.services.TransactionsService
     * @param {number} id Transaction id.
     * @returns {?Object} Transaction object or null if a transaction is not found.
     */
    get: function(id) {
      $log.debug('Get function executed with id: ' + id);

      var transactionIndex = -1;

      for (var i = 0; i < transactions.length; i++) {
        if (transactions[i].id === id) {
          transactionIndex = i;
          break;
        }
      }

      $log.debug('Transaction index: ' + transactionIndex);

      if (transactionIndex > -1) {
        $log.debug('Transaction found');
        return transactions[transactionIndex];
      } else {
        $log.debug('Transaction not found');
        return null;
      }
    },
    /**
     * @name save
     * @method
     * @memberOf BudgetSupervisor.services.TransactionsService
     * @param {Object} transaction Transaction object.
     * @description
     * The method creates a new transaction or updates existing one.
     */
    save: function(transaction) {
      var i = 0;

      if (transaction.id === -1) {
        var actualId = -1;

        for (i = 0; i < transactions.length; i++) {
          if (transactions[i].id > actualId) {
            actualId = transactions[i].id;
          }
        }

        actualId++;

        $log.debug('Creating transaction');
        transaction.id = actualId;
        transactions.push(transaction);
      } else {
        var transactionIndex = -1;

        for (i = 0; i < transactions.length; i++) {
          if (transactions[i].id === transaction.id) {
            transactionIndex = i;
            break;
          }
        }

        $log.debug('Transaction index: ' + transactionIndex);

        if (transactionIndex > -1) {
          $log.debug('Updating transaction');
          transactions[transactionIndex] = transaction;
        }
      }

      $log.debug('Transactions state after save function:');
      $log.debug(transactions);
    },
    /**
     * @name query
     * @method
     * @memberOf BudgetSupervisor.services.TransactionsService
     * @returns {Object[]} Transactions list.
     */
    query: function() {
      return transactions;
    },
    /**
     * @name remove
     * @method
     * @memberOf BudgetSupervisor.services.TransactionsService
     * @param {number} id Transaction id.
     * @description
     * The method removes transaction from transactions list.
     */
    remove: function(id) {
      $log.debug('Remove function executed with id: ' + id);

      var transactionIndex = -1;

      for (var i = 0; i < transactions.length; i++) {
        if (transactions[i].id === id) {
          transactionIndex = i;
          break;
        }
      }

      $log.debug('Transaction index: ' + transactionIndex);

      if (transactionIndex > -1) {
        $log.debug('Removing transaction');
        transactions.splice(transactionIndex, 1);
      }

      $log.debug('Transactions state after remove function:');
      $log.debug(transactions);
    },
    /**
     * @name reorder
     * @method
     * @memberOf BudgetSupervisor.services.TransactionsService
     * @param {Object} item Transaction object.
     * @param {number} fromIndex Transaction's old array index.
     * @param {number} toIndex Transaction's new array index.
     * @description
     * The method reorders transactions list.
     */
    reorder: function(item, fromIndex, toIndex) {
      $log.debug('Reorder function executed with parameters: item, fromIndex, toIndex');

      $log.debug(item);
      $log.debug(fromIndex);
      $log.debug(toIndex);

      $log.debug('Transactions state before reload function:');
      $log.debug(transactions);

      $log.debug('Reordering transactions');
      transactions.splice(fromIndex, 1);
      transactions.splice(toIndex, 0, item);

      $log.debug('Transactions state after reload function:');
      $log.debug(transactions);
    }
  };
}])
;
