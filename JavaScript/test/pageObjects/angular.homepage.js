'use strict';

module.exports = {

  vars: {
    nameInput: element(by.model('yourName')),
    greeting: element(by.binding('yourName'))
},

  getUrl: function() {
    browser.get('http://www.angularjs.org');
    browser.waitForAngular();
  },

  setName: function(name) {
    var nm = this.vars;
    nm.nameInput.sendKeys(name);
  },

  getGreeting: function() {
    var gr = this.vars;
    return gr.greeting.getText();
  }
};