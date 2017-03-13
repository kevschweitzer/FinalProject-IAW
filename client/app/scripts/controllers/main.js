'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
  .controller('MainCtrl', function ($scope,$rootScope,$routeParams,Noticia) {

      $scope.noticias = Noticia.getList({limit:1000000}).$object;

      $scope.primero = $scope.noticias[0];

  });
