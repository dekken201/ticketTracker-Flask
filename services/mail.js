const notifier = require('mail-notifier')
const {
    PythonShell
} = require("python-shell")
const configs = require('../config.json')

async function mailListen(io) {
    console.log("Iniciando serviço de e-mail")
    notifier(configs.imap)
        .on('mail', mail => {
            console.log("Novo e-mail.")
            processMail(mail)
        })
        .on('connected', () => {
            console.log("Conectado com sucesso! Monitorando 👮")
        })
        .on('error', (e) => {
            console.log("Erro no serviço de e-mail" + e)
        })
        .start()

    function processMail(mail) {
        console.log("Processando e-mail")
        if (2+2 == 4){//mail.from[0].name === configs.imap.sender) {
            console.log("Enviando para python")
            delete mail['html']
            PythonShell.run('test.py', { //arquivo com script para processar as informações do email recebido
                args: JSON.stringify(mail)
            }, function (err, results) {
                if (err) return console.log("Erro no processamento PYTHON: " + err);
                console.log('Results: %j', results);
                console.log("Enviando para monitores")
                io.sockets.emit('mensagem', results) //retorno do python para results
            });

        } else {
            console.log("E-mail não qualificado")
        }
    }
}

module.exports = mailListen