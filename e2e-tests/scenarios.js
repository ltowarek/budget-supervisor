'use strict';

describe('Budget Supervisor', function() {

  describe('Categories view', function() {
    beforeEach(function() {
      browser.get('index.html#/categories');
    });

    it('should redirect to the categories view', function () {
      expect(browser.getLocationAbsUrl()).toMatch('/categories');
    });

    //TODO: Protractor clicks an element, chrome displays information about the new url in the bottom left corner, but url does not change. Cannot reproduce it without protractor.
    xit('should open a new category view', function () {
      element(by.id('addCategoryButton')).click();

      expect(browser.getLocationAbsUrl()).toMatch('/categories/');
    });

    it('should open a category\'s details view', function () {
      element.all(by.css('#categoriesList ion-item')).first().click();

      expect(browser.getLocationAbsUrl()).toMatch('/categories/0');
    });

    it('should delete a category', function () {
      element(by.id('toggleDeleteButton')).click();
      element.all(by.css('.item-delete.active')).first().click();
      element(by.css('body > div.popup-container.popup-showing.active > div > div.popup-buttons > button.button.ng-binding.button-positive')).click();

      expect(element.all(by.repeater('category in categories')).count()).toEqual(2);
    });

    it('should cancel a category deletion', function () {
      element(by.id('toggleDeleteButton')).click();
      element.all(by.css('.item-delete.active')).first().click();
      element(by.css('body > div.popup-container.popup-showing.active > div > div.popup-buttons > button.button.ng-binding.button-default')).click();

      expect(element.all(by.repeater('category in categories')).count()).toEqual(3);
    });
  });

  describe('Category Details View', function() {
    it('should display existing category\'s details', function() {
      browser.get('index.html#/categories/0');

      expect(element(by.model('category.title')).getAttribute('value')).toEqual('Food');
    });

    it('should display a new category template if category does not exist', function() {
      browser.get('index.html#/categories/wrongid');

      expect(element(by.model('category.title')).getAttribute('value')).toEqual('');
    });

    it('should update existing category', function() {
      browser.get('index.html#/categories/0');
      element(by.model('category.title')).sendKeys('Updated');
      element(by.id('submit')).click();

      expect(browser.getLocationAbsUrl()).toMatch('/categories');
      expect(element(by.css('#categoriesList > div > ion-item:nth-child(1) > div.item-content > a')).getText()).toEqual('FoodUpdated');
    });

    it('should create a new category', function() {
      browser.get('index.html#/categories/');
      element(by.model('category.title')).sendKeys('New');
      element(by.id('submit')).click();

      expect(browser.getLocationAbsUrl()).toMatch('/categories');
      expect(element.all(by.repeater('category in categories')).count()).toEqual(4);
    });
  });

  describe('Tags view', function() {
    beforeEach(function() {
      browser.get('index.html#/tags');
    });

    it('should redirect to the tags view', function () {
      expect(browser.getLocationAbsUrl()).toMatch('/tags');
    });

    //TODO: Protractor clicks an element, chrome displays information about the new url in the bottom left corner, but url does not change. Cannot reproduce it without protractor.
    xit('should open a new tag view', function () {
      element(by.id('addTagButton')).click();

      expect(browser.getLocationAbsUrl()).toMatch('/tags/');
    });

    it('should open a tag\'s details view', function () {
      element.all(by.css('#tagsList ion-item')).first().click();

      expect(browser.getLocationAbsUrl()).toMatch('/tags/0');
    });

    it('should delete a tag', function () {
      element(by.id('toggleDeleteButton')).click();
      element.all(by.css('.item-delete.active')).first().click();
      element(by.css('body > div.popup-container.popup-showing.active > div > div.popup-buttons > button.button.ng-binding.button-positive')).click();

      expect(element.all(by.repeater('tag in tags')).count()).toEqual(2);
    });

    it('should cancel a tag deletion', function () {
      element(by.id('toggleDeleteButton')).click();
      element.all(by.css('.item-delete.active')).first().click();
      element(by.css('body > div.popup-container.popup-showing.active > div > div.popup-buttons > button.button.ng-binding.button-default')).click();

      expect(element.all(by.repeater('tag in tags')).count()).toEqual(3);
    });
  });

  describe('Tag Details View', function() {
    it('should display existing tag\'s details', function() {
      browser.get('index.html#/tags/0');

      expect(element(by.model('tag.title')).getAttribute('value')).toEqual('Tesco');
    });

    it('should display a new tag template if tag does not exist', function() {
      browser.get('index.html#/tags/wrongid');

      expect(element(by.model('tag.title')).getAttribute('value')).toEqual('');
    });

    it('should update existing tag', function() {
      browser.get('index.html#/tags/0');
      element(by.model('tag.title')).sendKeys('Updated');
      element(by.id('submit')).click();

      expect(browser.getLocationAbsUrl()).toMatch('/tags');
      expect(element(by.css('#tagsList > div > ion-item:nth-child(1) > div.item-content > a')).getText()).toEqual('TescoUpdated');
    });

    it('should create a new tag', function() {
      browser.get('index.html#/tags/');
      element(by.model('tag.title')).sendKeys('New');
      element(by.id('submit')).click();

      expect(browser.getLocationAbsUrl()).toMatch('/tags');
      expect(element.all(by.repeater('tag in tags')).count()).toEqual(4);
    });
  });

  describe('Transactions view', function() {
    beforeEach(function() {
      browser.get('index.html#/transactions');
    });

    it('should redirect to the transactions view', function () {
      expect(browser.getLocationAbsUrl()).toMatch('/transactions');
    });

    //TODO: Protractor clicks an element, chrome displays information about the new url in the bottom left corner, but url does not change. Cannot reproduce it without protractor.
    xit('should open a new transaction view', function () {
      element(by.id('addTransactionButton')).click();

      expect(browser.getLocationAbsUrl()).toMatch('/transactions/');
    });

    it('should open a transaction\'s details view', function () {
      element.all(by.css('#transactionsList ion-item')).first().click();

      expect(browser.getLocationAbsUrl()).toMatch('/transactions/2');
    });

    it('should delete a transaction', function () {
      element(by.id('toggleDeleteButton')).click();
      element.all(by.css('.item-delete.active')).first().click();
      element(by.css('body > div.popup-container.popup-showing.active > div > div.popup-buttons > button.button.ng-binding.button-positive')).click();

      expect(element.all(by.repeater('transaction in transactions')).count()).toEqual(2);
    });

    it('should cancel a transaction deletion', function () {
      element(by.id('toggleDeleteButton')).click();
      element.all(by.css('.item-delete.active')).first().click();
      element(by.css('body > div.popup-container.popup-showing.active > div > div.popup-buttons > button.button.ng-binding.button-default')).click();

      expect(element.all(by.repeater('transaction in transactions')).count()).toEqual(3);
    });

    it('should filter transactions', function () {
      element(by.id('searchKey')).sendKeys('Egg');

      expect(element.all(by.repeater('transaction in transactions')).count()).toEqual(1);
    });

    it('should order transactions by date', function () {
      var lastDate = new Date();
      element.all(by.repeater('transaction in transactions')).each(function(element) {
       element.getText().then(function(text) {
         var actualDate = new Date(text.split('\n', 1));
         expect(actualDate <= lastDate).toBeTruthy();
         lastDate = actualDate;
       });
      });
    });
  });

  describe('Transaction Details View', function() {
    it('should display existing transaction\'s details', function() {
      browser.get('index.html#/transactions/0');

      expect(element(by.model('transaction.title')).getAttribute('value')).toEqual('Eggs');
      expect(element(by.model('transaction.value')).getAttribute('value')).toEqual('-5.5');
      expect(element(by.model('transaction.date')).getAttribute('value')).toEqual('2010-09-03');
      expect(element(by.model('transaction.category')).getAttribute('value')).toEqual('0');
      //TODO: Handle multiple tags
      expect(element(by.model('transaction.tags')).getAttribute('value')).toEqual('0');
      expect(element(by.model('transaction.description')).getAttribute('value')).toEqual('10 eggs');
    });

    it('should display a new transaction template if tag does not exist', function() {
      browser.get('index.html#/transactions/wrongid');

      expect(element(by.model('transaction.title')).getAttribute('value')).toEqual('');
      expect(element(by.model('transaction.value')).getAttribute('value')).toEqual('');
      expect(element(by.model('transaction.date')).getAttribute('value')).toEqual('');
      expect(element(by.model('transaction.category')).getAttribute('value')).toEqual('');
      expect(element(by.model('transaction.tags')).getAttribute('value')).toEqual('');
      expect(element(by.model('transaction.description')).getAttribute('value')).toEqual('');
    });

    it('should update existing transaction', function() {
      browser.get('index.html#/transactions/0');
      element(by.model('transaction.title')).sendKeys('Updated');
      element(by.id('submit')).click();

      expect(browser.getLocationAbsUrl()).toMatch('/transactions');
      expect(element(by.css('#transactionsList > div > ion-item:nth-child(3) > div.item-content > a')).getText()).toEqual('Sep 3, 2010\nEggsUpdated\n($5.50)');
    });

    it('should create a new transaction', function() {
      browser.get('index.html#/transactions/');
      element(by.model('transaction.title')).sendKeys('New');
      element(by.model('transaction.value')).sendKeys('-5.00');
      element(by.model('transaction.date')).sendKeys('2010-01-20');
      element(by.model('transaction.category')).element(by.cssContainingText('option', 'Food')).click();
      element(by.model('transaction.tags')).element(by.cssContainingText('option', 'Tesco')).click();
      element(by.model('transaction.description')).sendKeys('Description');
      element(by.id('submit')).click();

      expect(browser.getLocationAbsUrl()).toMatch('/transactions');
      expect(element.all(by.repeater('transaction in transactions')).count()).toEqual(4);
    });
  });
});
