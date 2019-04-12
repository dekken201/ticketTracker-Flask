const configs = require('../config.json')
const express = require('express')
const patch = require('path')
const app = express()
const server = require('http').createServer(app)
const io = require('socket.io')(server)


async function socket() {
    app.use(express.static(patch.join(__dirname, '../public')))
    app.set('views', patch.join(__dirname, '../public'))
    app.engine('html', require('ejs').renderFile)
    app.set('viw engine', 'html')

    app.use('/', (req, res) => {
        res.render('index.html')
    })

    server.listen(configs.port);
    console.log("Socket iniciado na porta: " + configs.port + ".")

    return io
}

module.exports = socket