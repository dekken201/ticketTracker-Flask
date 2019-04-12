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
            console.log("Conectado com sucesso! Monitorando..")
        })
        .on('error', (e) => {
            console.log("Erro no serviço de e-mail" + e)
        })
        .start()

    function processMail(mail) {
        console.log("Processando e-mail..")
        console.log(mail.from[0].name)
        console.log(configs.imap.senderJS)
        if (mail.from[0].name === configs.imap.senderJS) {
            console.log("E-mail válido! Enviando para o banco de dados.")
            delete mail['html']
            PythonShell.run('run.py', {
            }, function (err, results) {
                if (err) return console.log("Erro no processamento PYTHON: " + err);
            });

        } else {
            console.log("E-mail não qualificado")
        }
    }
}

module.exports = mailListen