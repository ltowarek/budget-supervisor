'use strict';

describe('Budget Supervisor', function() {

  describe('Categories view', function() {
    beforeEach(function() {
      browser.get('index.html#/categories');
    });

    it('should redirect to the categories view', function () {
      expect(browser.getLocationAbsUrl()).toMatch('/categories');
    });
  });
});
