var fs = require('fs');
var files = fs.readdirSync('./test/specs');

exports.config = {
  framework: 'jasmine',
  seleniumAddress: 'http://localhost:4444/wd/hub',
  specs: ['./test/specs/test_*.js'],
  jasmineNodeOpts: {
    showColors: true,
  },
  multiCapabilities: [{
        browserName: 'chrome',
        shardTestFiles: true,
        maxInstances: files.length,
    }]
};