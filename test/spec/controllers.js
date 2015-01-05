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
  });

  it('should show delete buttons and hide reorder buttons', function () {
    $scope.toggleDelete();

    expect($scope.config.showDelete, 'showDelete').equal(true);
  });

  it('should remove category', function () {
    var stub = sinon.stub(service, 'remove');

    $scope.remove(0);

    expect(stub.callCount, 'remove function call counts').to.equal(1);
    expect(stub.args[0][0], 'removed category id').to.equal(0);
    expect($scope.config.showDelete, 'showDelete').equal(false);
  });
});

describe('Controller: CategoryDetailsController', function () {

  beforeEach(module('BudgetSupervisor'));

  var service,
    $controller,
    $scope;

  beforeEach(inject(function (_$controller_, $rootScope, $injector) {
    $controller = _$controller_;
    $scope = $rootScope.$new();
    service = $injector.get('CategoriesService');

    $controller('CategoryDetailsController', {
      $scope: $scope,
      $stateParams: {id: 1}
    });
  }));

  it('should attach an existing category to the scope', function () {
    var stub = sinon.stub(service, 'get', function () {
      return {id: 1, title: 'Salary'};
    });

    $controller('CategoryDetailsController', {
      $scope: $scope,
      $stateParams: {id: '1'}
    });

    expect(stub.callCount, 'get function call counts').to.equal(1);
    expect(stub.args[0][0], 'category id').to.equal(1);
    expect($scope.category).to.eql({id: 1, title: 'Salary'});
  });

  it('should attach a new category to the scope', function () {
    var stub = sinon.stub(service, 'get', function () {
      return null;
    });

    $controller('CategoryDetailsController', {
      $scope: $scope,
      $stateParams: {id: ''}
    });

    expect(stub.callCount, 'get function call counts').to.equal(1);
    expect(stub.args[0][0], 'category id').to.equal(-1);
    expect($scope.category).to.eql({id: -1, title: ''});
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
