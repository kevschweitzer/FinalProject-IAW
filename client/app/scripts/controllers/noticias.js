'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:NoticiasCtrl
 * @description
 * # NoticiasCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
  .controller('NoticiasCtrl', function ($scope,Noticia) {

    $scope.noticias = Noticia.getList().$object;



});
