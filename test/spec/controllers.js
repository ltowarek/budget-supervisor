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

  it('should show delete buttons', function () {
    $scope.toggleDelete();

    expect($scope.config.showDelete, 'showDelete').equal(true);
  });

  //TODO: there is an issue with $httpBackend which stops promises testing (Unexpected request: GET ...)
  it.skip('should remove category', function () {
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
      $stateParams: {id: '1'}
    });
  }));

  it('should attach an existing category to the scope', function () {
    var stub = sinon.stub(service, 'get', function () {
      return {id: 0, title: 'Salary'};
    });

    $controller('CategoryDetailsController', {
      $scope: $scope,
      $stateParams: {id: '0'}
    });

    expect(stub.callCount, 'get function call counts').to.equal(1);
    expect(stub.args[0][0], 'category id').to.equal(0);
    expect($scope.category).to.eql({id: 0, title: 'Salary'});
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

describe('Controller: TagsController', function () {

  beforeEach(module('BudgetSupervisor'));

  var service,
    serviceQueryStub,
    $scope;

  beforeEach(inject(function ($controller, $rootScope, $injector) {
    $scope = $rootScope.$new();
    service = $injector.get('TagsService');
    serviceQueryStub = sinon.stub(service, 'query', function () {
      return [
        { id: 0, title: 'Tesco'},
        { id: 1, title: 'Part-time job'}
      ];
    });
    $controller('TagsController', {
      $scope: $scope
    });
  }));

  it('should attach a list of tags to the scope', function () {
    expect(serviceQueryStub.callCount, 'query function call counts').to.equal(1);
    expect($scope.tags, 'tags').to.have.length(2);
  });

  it('should attach a list of config values to the scope', function () {
    expect($scope.config, 'config').to.have.property('showDelete', false);
  });

  it('should show delete buttons', function () {
    $scope.toggleDelete();

    expect($scope.config.showDelete, 'showDelete').equal(true);
  });

  //TODO: there is an issue with $httpBackend which stops promises testing (Unexpected request: GET ...)
  it.skip('should remove tag', function () {
    var stub = sinon.stub(service, 'remove');

    $scope.remove(0);

    expect(stub.callCount, 'remove function call counts').to.equal(1);
    expect(stub.args[0][0], 'removed tag id').to.equal(0);
    expect($scope.config.showDelete, 'showDelete').equal(false);
  });
});

describe('Controller: TagDetailsController', function () {

  beforeEach(module('BudgetSupervisor'));

  var service,
    $controller,
    $scope;

  beforeEach(inject(function (_$controller_, $rootScope, $injector) {
    $controller = _$controller_;
    $scope = $rootScope.$new();
    service = $injector.get('TagsService');

    $controller('TagDetailsController', {
      $scope: $scope,
      $stateParams: {id: '1'}
    });
  }));

  it('should attach an existing tag to the scope', function () {
    var stub = sinon.stub(service, 'get', function () {
      return {id: 0, title: 'Tesco'};
    });

    $controller('TagDetailsController', {
      $scope: $scope,
      $stateParams: {id: '0'}
    });

    expect(stub.callCount, 'get function call counts').to.equal(1);
    expect(stub.args[0][0], 'tag id').to.equal(0);
    expect($scope.tag).to.eql({id: 0, title: 'Tesco'});
  });

  it('should attach a new tag to the scope', function () {
    var stub = sinon.stub(service, 'get', function () {
      return null;
    });

    $controller('TagDetailsController', {
      $scope: $scope,
      $stateParams: {id: ''}
    });

    expect(stub.callCount, 'get function call counts').to.equal(1);
    expect(stub.args[0][0], 'tag id').to.equal(-1);
    expect($scope.tag).to.eql({id: -1, title: ''});
  });

  it('should save tag', function () {
    var stub = sinon.stub(service, 'save');

    $scope.save({});

    expect(stub.callCount, 'save function call counts').to.equal(1);
    expect(stub.args[0][0], 'tag object').to.eql({});
  });

  it('should change state after saving tag', inject(function ($state) {
    var stub = sinon.stub($state, 'go');

    $scope.save({});

    expect(stub.callCount, 'state go call counts').to.equal(1);
  }));
});

describe('Controller: TransactionsController', function () {

  beforeEach(module('BudgetSupervisor'));

  var service,
    serviceQueryStub,
    $scope;

  beforeEach(inject(function ($controller, $rootScope, $injector) {
    $scope = $rootScope.$new();
    service = $injector.get('TransactionsService');
    serviceQueryStub = sinon.stub(service, 'query', function () {
      return [
        { id: 0, title: 'Eggs', value: -5.50, date: '2010-09-03', category: { id: 0, title: 'Food'}, tags: [{ id: 0, title: 'Tesco'}], description: '10 eggs'},
        { id: 1, title: 'Tesco salary', value: 2000.00, date: '2010-09-10', category: { id: 1, title: 'Salary'}, tags: [{ id: 0, title: 'Tesco'}, { id: 1, title: 'Part-time job'}], description: ''},
        { id: 2, title: 'Lottery', value: -3.50, date: '2010-09-23', category: { id: 0, title: 'Miscellaneous'}, tags: [], description: 'Number: 1, 2, 3, 4, 5\nLottery day: Sep 24, 2010'}
      ];
    });
    $controller('TransactionsController', {
      $scope: $scope
    });
  }));

  it('should attach a list of transactions to the scope', function () {
    expect(serviceQueryStub.callCount, 'query function call counts').to.equal(1);
    expect($scope.transactions, 'transactions').to.have.length(3);
  });

  it('should attach a list of config values to the scope', function () {
    expect($scope.config, 'config').to.have.property('showDelete', false);
  });

  it('should show delete buttons', function () {
    $scope.toggleDelete();

    expect($scope.config.showDelete, 'showDelete').equal(true);
  });

  //TODO: there is an issue with $httpBackend which stops promises testing (Unexpected request: GET ...)
  it.skip('should remove transaction', function () {
    var stub = sinon.stub(service, 'remove');

    $scope.remove(0);

    expect(stub.callCount, 'remove function call counts').to.equal(1);
    expect(stub.args[0][0], 'removed transaction id').to.equal(0);
    expect($scope.config.showDelete, 'showDelete').equal(false);
  });
});

describe('Controller: TransactionDetailsController', function () {

  beforeEach(module('BudgetSupervisor'));

  var transactionsService,
    categoriesService,
    tagsService,
    $controller,
    $scope;

  beforeEach(inject(function (_$controller_, $rootScope, $injector) {
    $controller = _$controller_;
    $scope = $rootScope.$new();
    transactionsService = $injector.get('TransactionsService');
    categoriesService = $injector.get('CategoriesService');
    tagsService = $injector.get('TagsService');

    $controller('TransactionDetailsController', {
      $scope: $scope,
      $stateParams: {id: '1'}
    });
  }));

  it('should attach an existing tag to the scope', function () {
    var stub = sinon.stub(transactionsService, 'get', function () {
      return { id: 0, title: 'Eggs', value: -5.50, date: '2010-09-03', category: { id: 0, title: 'Food'}, tags: [{ id: 0, title: 'Tesco'}], description: '10 eggs'};
    });

    $controller('TransactionDetailsController', {
      $scope: $scope,
      $stateParams: {id: '0'}
    });

    expect(stub.callCount, 'get function call counts').to.equal(1);
    expect(stub.args[0][0], 'transaction id').to.equal(0);
    expect($scope.transaction).to.eql({ id: 0, title: 'Eggs', value: -5.50, date: new Date('2010-09-03'), category: { id: 0, title: 'Food'}, tags: [{ id: 0, title: 'Tesco'}], description: '10 eggs'});
  });

  it('should attach a new transaction to the scope', function () {
    var stub = sinon.stub(transactionsService, 'get', function () {
      return null;
    });

    $controller('TransactionDetailsController', {
      $scope: $scope,
      $stateParams: {id: ''}
    });

    expect(stub.callCount, 'get function call counts').to.equal(1);
    expect(stub.args[0][0], 'transaction id').to.equal(-1);
    expect($scope.transaction).to.eql({ id: -1, title: null, value: null, date: new Date(''), category: null, tags: null, description: null});
  });

  it('should attach existing categories and tags to the scope', function () {
    var categories = [
      { id: 0, title: 'Food'},
      { id: 1, title: 'Salary'},
      { id: 2, title: 'Miscellaneous'}
    ];
    var tags = [
      { id: 0, title: 'Tesco'},
      { id: 1, title: 'Part-time job'},
      { id: 2, title: 'John'}
    ];

    var categoriesStub = sinon.stub(categoriesService, 'query', function () {
      return categories;
    });
    var tagsStub = sinon.stub(tagsService, 'query', function () {
      return tags;
    });

    $controller('TransactionDetailsController', {
      $scope: $scope,
      $stateParams: {id: ''}
    });

    expect(categoriesStub.callCount, 'categories query function call counts').to.equal(1);
    expect(tagsStub.callCount, 'tags query function call counts').to.equal(1);
    expect($scope.categories).to.eql(categories);
    expect($scope.tags).to.eql(tags);
  });

  it('should save tag', function () {
    var stub = sinon.stub(transactionsService, 'save');

    $scope.save({});

    expect(stub.callCount, 'save function call counts').to.equal(1);
    expect(stub.args[0][0], 'transaction object').to.eql({});
  });

  it('should change state after saving tag', inject(function ($state) {
    var stub = sinon.stub($state, 'go');

    $scope.save({});

    expect(stub.callCount, 'state go call counts').to.equal(1);
  }));
});
