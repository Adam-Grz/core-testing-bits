var ah = require('../pageObjects/angular.homepage.js');

describe('angularjs homepage', function() {
  it('should greet the named user A', function() {
    ah.getUrl();

    ah.setName('Julie');

    expect(ah.getGreeting()).toEqual('Hello Julie!');
  });
});