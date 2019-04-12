const {
    PythonShell
} = require("python-shell");


PythonShell.run('test.py', {
    args: mail
}, function (err, results) {
    if (err) return (err);
    console.dir(results);

});