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
});
