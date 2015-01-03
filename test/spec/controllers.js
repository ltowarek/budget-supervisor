'use strict';

describe('Controller: CategoriesController', function () {

  beforeEach(module('BudgetSupervisor'));

  var service,
    serviceQueryStub,
    $scope;

  beforeEach(inject(function ($controller, $rootScope, $injector) {
    $scope = $rootScope.$new();
    service = $injector.get('CategoriesService');
    serviceQueryStub = sinon.stub(service, 'query', function () {
      return [
        {id: 0, title: 'Food'},
        {id: 1, title: 'Salary'}
      ];
    });
    $controller('CategoriesController', {
      $scope: $scope
    });
  }));

  it('should attach a list of categories to the scope', function () {
    expect(serviceQueryStub.callCount, 'query function call counts').to.equal(1);
    expect($scope.categories, 'categories').to.have.length(2);
  });

  it('should attach a list of config values to the scope', function () {
    expect($scope.config, 'config').to.have.property('showDelete', false);
    expect($scope.config, 'config').to.have.property('showReorder', false);
  });

  it('should show delete buttons and hide reorder buttons', function () {
    $scope.toggleDelete();

    expect($scope.config.showDelete, 'showDelete').equal(true);
    expect($scope.config.showReorder, 'showReorder').equal(false);
  });

  it('should show reorder buttons and hide delete buttons', function () {
    $scope.toggleReorder();

    expect($scope.config.showReorder, 'showReorder').equal(true);
    expect($scope.config.showDelete, 'showDelete').equal(false);
  });

  it('should remove category', function () {
    var stub = sinon.stub(service, 'remove');

    $scope.remove(0);

    expect(stub.callCount, 'remove function call counts').to.equal(1);
    expect(stub.args[0][0], 'removed category id').to.equal(0);
    expect($scope.config.showDelete, 'showDelete').equal(false);
  });

  it('should reorder categories', function () {
    var stub = sinon.stub(service, 'reorder');

    $scope.reorder({}, 0, 1);

    expect(stub.callCount, 'reorder function call counts').to.equal(1);
    expect(stub.args[0][0], 'reordered category object').to.eql({});
    expect(stub.args[0][1], 'reordered category from index').to.equal(0);
    expect(stub.args[0][2], 'reordered category to index').to.equal(1);
    expect($scope.config.showDelete, 'showDelete').equal(false);
  });
});

describe('Controller: CategoryDetailsController', function () {

  beforeEach(module('BudgetSupervisor'));

  var service,
    serviceGetStub,
    $scope;

  beforeEach(inject(function ($controller, $rootScope, $injector) {
    $scope = $rootScope.$new();
    service = $injector.get('CategoriesService');

    serviceGetStub = sinon.stub(service, 'get', function () {
      return {id: 1, title: 'Salary'};
    });

    $controller('CategoryDetailsController', {
      $scope: $scope,
      $stateParams: {id: 1}
    });
  }));

  it('should attach a category to the scope', function () {
    expect(serviceGetStub.callCount, 'get function call counts').to.equal(1);
    expect(serviceGetStub.args[0][0], 'category id').to.equal(1);
    expect($scope.category).to.eql({id: 1, title: 'Salary'});
  });

  it('should save category', function () {
    var stub = sinon.stub(service, 'save');

    $scope.save({});

    expect(stub.callCount, 'save function call counts').to.equal(1);
    expect(stub.args[0][0], 'category object').to.eql({});
  });

  it('should change state after saving category', inject(function ($state) {
    var stub = sinon.stub($state, 'go');

    $scope.save({});

    expect(stub.callCount, 'state go call counts').to.equal(1);
  }));
});
