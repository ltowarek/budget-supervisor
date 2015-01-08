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
});
