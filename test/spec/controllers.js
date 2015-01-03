'use strict';

describe('Controller: CategoriesController', function () {

  beforeEach(module('BudgetSupervisor'));

  var categoriesController,
    categoriesService,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope, $injector) {
    scope = $rootScope.$new();
    categoriesService = $injector.get('CategoriesService');
    categoriesController = $controller('CategoriesController', {
      $scope: scope
    });
  }));

  it('should attach a list of categories to the scope', function () {
    expect(scope.categories, 'categories').to.have.length(3);
  });

  it('should attach a list of config values to the scope', function () {
    expect(scope.config, 'config').to.have.property('showDelete', false);
    expect(scope.config, 'config').to.have.property('showReorder', false);
  });

  it('should toggle showDelete value and disable showReorder', function () {
    scope.toggleDelete();

    expect(scope.config.showDelete, 'showDelete').equal(true);
    expect(scope.config.showReorder, 'showReorder').equal(false);
  });

  it('should toggle showReorder value and disable showDelete', function () {
    scope.toggleReorder();

    expect(scope.config.showReorder, 'showReorder').equal(true);
    expect(scope.config.showDelete, 'showDelete').equal(false);
  });

  it('should call service remove function', function () {
    var spy = sinon.spy(categoriesService, 'remove');

    scope.remove(0);

    expect(spy.callCount, 'remove function call counts').to.equal(1);
    expect(spy.args[0][0], 'removed category id').to.equal(0);
    expect(scope.config.showDelete, 'showDelete').equal(false);
  });

  it('should call service reorder function', function () {
    var spy = sinon.spy(categoriesService, 'reorder');

    scope.reorder({}, 0, 1);

    expect(spy.callCount, 'reorder function call counts').to.equal(1);
    expect(spy.args[0][0], 'reordered category object').to.eql({});
    expect(spy.args[0][1], 'reordered category from index').to.equal(0);
    expect(spy.args[0][2], 'reordered category to index').to.equal(1);
    expect(scope.config.showDelete, 'showDelete').equal(false);
  });
});
