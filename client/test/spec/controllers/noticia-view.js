'use strict';

describe('Controller: NoticiaViewCtrl', function () {

  // load the controller's module
  beforeEach(module('clientApp'));

  var NoticiaViewCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    NoticiaViewCtrl = $controller('NoticiaViewCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(NoticiaViewCtrl.awesomeThings.length).toBe(3);
  });
});
