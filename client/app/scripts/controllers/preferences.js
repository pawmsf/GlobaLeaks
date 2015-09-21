GLClient.controller('PreferencesCtrl', ['$scope', '$rootScope', 'changePasswordWatcher', 'CONSTANTS', 'Authentication',
  function($scope, $rootScope, changePasswordWatcher, CONSTANTS, Authentication) {

    if (Authentication.role === 'receiver') {
      // Receivers currently are the only user that benefit of specialized preferences.
      $scope.tabs = [
        {
          title: "General Preferences",
          template: "views/receiver/preferences/tab1.html",
          ctrl: TabCtrl
        },
        {
          title: "Password Configuration",
          template: "views/receiver/preferences/tab2.html",
          ctrl: TabCtrl
        },
        {
          title: "Notification Settings",
          template: "views/receiver/preferences/tab3.html",
          ctrl: TabCtrl
        },
        {
          title:"Encryption Settings",
          template:"views/receiver/preferences/tab4.html",
          ctrl: TabCtrl
        }
      ];
    } else {
      $scope.tabs = [
        {
          title: "General Preferences",
          template: "views/user/preferences/tab1.html",
          ctrl: TabCtrl
        },
        {
          title: "Password Configuration",
          template: "views/user/preferences/tab2.html",
          ctrl: TabCtrl
        },
        {
          title:"Encryption Settings",
          template:"views/user/preferences/tab3.html",
          ctrl: TabCtrl
        }
      ];
    }

    $scope.navType = 'pills';

    $scope.timezones = CONSTANTS.timezones;
    $scope.email_regexp = CONSTANTS.email_regexp;

    changePasswordWatcher($scope, "preferences.old_password",
        "preferences.password", "preferences.check_password");

    $scope.pass_save = function () {
      if ($scope.preferences.pgp_key_remove === undefined) {
        $scope.preferences.pgp_key_remove = false;
      }
      if ($scope.preferences.pgp_key_public === undefined) {
        $scope.preferences.pgp_key_public = '';
      }

      $scope.preferences.$update(function () {

        if (!$rootScope.successes) {
          $rootScope.successes = [];
        }
        $rootScope.successes.push({message: 'Updated your password!'});
      });
    };

    $scope.pref_save = function() {
      $scope.preferences.password = '';
      $scope.preferences.old_password = '';

      if ($scope.preferences.pgp_key_remove === true) {
        $scope.preferences.pgp_key_public = '';
      }

      if ($scope.preferences.pgp_key_public !== undefined &&
          $scope.preferences.pgp_key_public !== '') {
        $scope.preferences.pgp_key_remove = false;
      }

      $scope.preferences.$update(function() {
        if (!$rootScope.successes) {
          $rootScope.successes = [];
        }
        $rootScope.successes.push({message: 'Updated your preferences!'});
      });
    };
}]);