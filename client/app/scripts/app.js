'use strict';

/**
 * @ngdoc overview
 * @name clientApp
 * @description
 * # clientApp
 *
 * Main module of the application.
 */
angular
  .module('clientApp', [
    'ngRoute',
    'restangular'
  ])
  .config(function ($routeProvider, $locationProvider, RestangularProvider) {

    RestangularProvider.setBaseUrl('http://localhost:3000');

    $locationProvider.hashPrefix('');
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
      })
      .when('/noticias', {
        templateUrl: 'views/noticias.html',
        controller: 'NoticiasCtrl',
      })
      .when('/create/noticia', {
        templateUrl: 'views/noticia-add.html',
        controller: 'NoticiaAddCtrl',
      })
      .when('/noticia/:id', {
        templateUrl: 'views/noticia-view.html',
        controller: 'NoticiaViewCtrl',
      })
      .when('/noticia/:id/delete', {
        templateUrl: 'views/noticia-delete.html',
        controller: 'NoticiaDeleteCtrl',
      })
      .when('/noticia/:id/edit', {
        templateUrl: 'views/noticia-edit.html',
        controller: 'NoticiaEditCtrl',
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .factory('NoticiaRestangular', function(Restangular) {
  return Restangular.withConfig(function(RestangularConfigurer) {
    RestangularConfigurer.setRestangularFields({
      id: '_id'
    });
  });
  })
  .factory('Noticia', function(NoticiaRestangular) {
    return NoticiaRestangular.service('noticia');
  });
