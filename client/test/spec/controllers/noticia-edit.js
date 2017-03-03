'use strict';

describe('Controller: NoticiaEditCtrl', function () {

  // load the controller's module
  beforeEach(module('clientApp'));

  var NoticiaEditCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    NoticiaEditCtrl = $controller('NoticiaEditCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(NoticiaEditCtrl.awesomeThings.length).toBe(3);
  });
});
