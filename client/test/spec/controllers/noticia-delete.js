'use strict';

describe('Controller: NoticiaDeleteCtrl', function () {

  // load the controller's module
  beforeEach(module('clientApp'));

  var NoticiaDeleteCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    NoticiaDeleteCtrl = $controller('NoticiaDeleteCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(NoticiaDeleteCtrl.awesomeThings.length).toBe(3);
  });
});
