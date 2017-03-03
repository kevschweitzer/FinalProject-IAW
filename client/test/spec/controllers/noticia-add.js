'use strict';

describe('Controller: NoticiaAddCtrl', function () {

  // load the controller's module
  beforeEach(module('clientApp'));

  var NoticiaAddCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    NoticiaAddCtrl = $controller('NoticiaAddCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(NoticiaAddCtrl.awesomeThings.length).toBe(3);
  });
});
