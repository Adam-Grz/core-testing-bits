var ah = require('../pageObjects/angular.homepage.js');

describe('angularjs homepage', function() {
  it('should greet the named user 2', function() {
    ah.getUrl();

    ah.setName('Mark');

    expect(ah.getGreeting()).toEqual('Hello Marqqqk!');
  });
});