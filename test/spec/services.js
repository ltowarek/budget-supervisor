'use strict';

describe('Service: CategoriesService', function () {

  beforeEach(module('BudgetSupervisor'));

  var service;

  beforeEach(inject(function ($controller, $rootScope, $injector) {
    service = $injector.get('CategoriesService');

    //TODO: Inject the following array to tests
    //var categories = [
    //  { id: 0, title: 'Food'},
    //  { id: 1, title: 'Salary'},
    //  { id: 2, title: 'Miscellaneous'}
    //];
  }));

  it('should exists', function () {
    expect(service.query(), 'categories').to.not.be.null();
    expect(service.query(), 'categories').to.not.be.undefined();
  });

  it('should get a category by id', function () {
    var result = service.get(1);

    expect(result.id, 'result id').to.be.equal(1);
  });

  it('should get a null using wrong id', function () {
    var result = service.get(-1);

    expect(result, 'result').to.be.null();
  });

  it('should save a new category', function () {
    var oldLength = service.query().length;

    service.save({id: -1, title: 'Test'});

    expect(service.query().length).to.be.equal(oldLength + 1);
  });

  it('should update an existing category', function () {
    var oldLength = service.query().length;
    var updatedCategory = {id: 0, title: 'Test'};

    service.save(updatedCategory);

    expect(service.get(0)).to.be.eql(updatedCategory);
    expect(service.query().length).to.be.equal(oldLength);
  });

  it('should not update categories with not existing category', function () {
    var oldCategories = service.query();
    var updatedCategory = {id: 5, title: 'Test'};

    service.save(updatedCategory);

    expect(service.query()).to.be.eql(oldCategories);
  });

  it('should remove category by id', function () {
    var oldLength = service.query().length;

    service.remove(1);

    expect(service.query().length).to.be.equal(oldLength - 1);
  });

  it('should not remove category if it not exists', function () {
    var oldCategories = service.query();

    service.remove(5);

    expect(service.query()).to.be.eql(oldCategories);
  });

  it('should reorder categories', function () {
    service.reorder({id: 0, title: 'Food'}, 0, 1);

    expect(service.query()).to.be.eql([
      { id: 1, title: 'Salary'},
      { id: 0, title: 'Food'},
      { id: 2, title: 'Miscellaneous'}
    ]);
  });
});

describe('Service: TagsService', function () {

  beforeEach(module('BudgetSupervisor'));

  var service;

  beforeEach(inject(function ($controller, $rootScope, $injector) {
    service = $injector.get('TagsService');

    //TODO: Inject the following array to tests
    //var tags = [
    //  { id: 0, title: 'Tesco'},
    //  { id: 1, title: 'Part-time job'},
    //  { id: 2, title: 'John'}
    //];
  }));

  it('should exists', function () {
    expect(service.query(), 'tags').to.not.be.null();
    expect(service.query(), 'tags').to.not.be.undefined();
  });

  it('should get a tag by id', function () {
    var result = service.get(1);

    expect(result.id, 'result id').to.be.equal(1);
  });

  it('should get a null using wrong id', function () {
    var result = service.get(-1);

    expect(result, 'result').to.be.null();
  });

  it('should save a new tag', function () {
    var oldLength = service.query().length;

    service.save({id: -1, title: 'Test'});

    expect(service.query().length).to.be.equal(oldLength + 1);
  });

  it('should update an existing tag', function () {
    var oldLength = service.query().length;
    var updatedTag = {id: 0, title: 'Test'};

    service.save(updatedTag);

    expect(service.get(0)).to.be.eql(updatedTag);
    expect(service.query().length).to.be.equal(oldLength);
  });

  it('should not update tags with not existing tag', function () {
    var oldTags = service.query();
    var updatedTag = {id: 5, title: 'Test'};

    service.save(updatedTag);

    expect(service.query()).to.be.eql(oldTags);
  });

  it('should remove tag by id', function () {
    var oldLength = service.query().length;

    service.remove(1);

    expect(service.query().length).to.be.equal(oldLength - 1);
  });

  it('should not remove tag if it not exists', function () {
    var oldTags = service.query();

    service.remove(5);

    expect(service.query()).to.be.eql(oldTags);
  });

  it('should reorder categories', function () {
    service.reorder({ id: 0, title: 'Tesco'}, 0, 1);

    expect(service.query()).to.be.eql([
      { id: 1, title: 'Part-time job'},
      { id: 0, title: 'Tesco'},
      { id: 2, title: 'John'}
    ]);
  });
});

describe('Service: TransactionsService', function () {

  beforeEach(module('BudgetSupervisor'));

  var service;

  beforeEach(inject(function ($controller, $rootScope, $injector) {
    service = $injector.get('TransactionsService');

    //TODO: Inject the following array to tests
    //var transactions = [
    //  { id: 0, title: 'Eggs', value: -5.50, date: '2010-09-03', category: { id: 0, title: 'Food'}, tags: [{ id: 0, title: 'Tesco'}], description: '10 eggs'},
    //  { id: 1, title: 'Tesco salary', value: 2000.00, date: '2010-09-10', category: { id: 1, title: 'Salary'}, tags: [{ id: 0, title: 'Tesco'}, { id: 1, title: 'Part-time job'}], description: ''},
    //  { id: 2, title: 'Lottery', value: -3.50, date: '2010-09-23', category: { id: 0, title: 'Miscellaneous'}, tags: [], description: 'Number: 1, 2, 3, 4, 5\nLottery day: Sep 24, 2010'}
    //];
  }));

  it('should exists', function () {
    expect(service.query(), 'transactions').to.not.be.null();
    expect(service.query(), 'transactions').to.not.be.undefined();
  });

  it('should get a transaction by id', function () {
    var result = service.get(1);

    expect(result.id, 'result id').to.be.equal(1);
  });

  it('should get a null using wrong id', function () {
    var result = service.get(-1);

    expect(result, 'result').to.be.null();
  });

  it('should save a new transaction', function () {
    var oldLength = service.query().length;

    service.save({ id: -1, title: 'Test', value: -5.50, date: '2010-09-03', category: { id: 0, title: 'Food'}, tags: [{ id: 0, title: 'Tesco'}], description: '10 eggs'});

    expect(service.query().length).to.be.equal(oldLength + 1);
  });

  it('should update an existing transaction', function () {
    var oldLength = service.query().length;
    var updatedTag = { id: 0, title: 'EggsUpdated', value: -5.50, date: '2010-09-03', category: { id: 0, title: 'Food'}, tags: [{ id: 0, title: 'Tesco'}], description: '10 eggs'};

    service.save(updatedTag);

    expect(service.get(0)).to.be.eql(updatedTag);
    expect(service.query().length).to.be.equal(oldLength);
  });

  it('should not update transactions with not existing transaction', function () {
    var oldTags = service.query();
    var updatedTag = { id: 5, title: 'EggsUpdated', value: -5.50, date: '2010-09-03', category: { id: 0, title: 'Food'}, tags: [{ id: 0, title: 'Tesco'}], description: '10 eggs'};

    service.save(updatedTag);

    expect(service.query()).to.be.eql(oldTags);
  });

  it('should remove transaction by id', function () {
    var oldLength = service.query().length;

    service.remove(1);

    expect(service.query().length).to.be.equal(oldLength - 1);
  });

  it('should not remove transaction if it not exists', function () {
    var oldTags = service.query();

    service.remove(5);

    expect(service.query()).to.be.eql(oldTags);
  });

  it('should reorder transactions', function () {
    service.reorder({ id: 0, title: 'Eggs', value: -5.50, date: '2010-09-03', category: { id: 0, title: 'Food'}, tags: [{ id: 0, title: 'Tesco'}], description: '10 eggs'}, 0, 1);

    expect(service.query()).to.be.eql([
      { id: 1, title: 'Tesco salary', value: 2000.00, date: '2010-09-10', category: { id: 1, title: 'Salary'}, tags: [{ id: 0, title: 'Tesco'}, { id: 1, title: 'Part-time job'}], description: ''},
      { id: 0, title: 'Eggs', value: -5.50, date: '2010-09-03', category: { id: 0, title: 'Food'}, tags: [{ id: 0, title: 'Tesco'}], description: '10 eggs'},
      { id: 2, title: 'Lottery', value: -3.50, date: '2010-09-23', category: { id: 0, title: 'Miscellaneous'}, tags: [], description: 'Number: 1, 2, 3, 4, 5\nLottery day: Sep 24, 2010'}
    ]);
  });
});
