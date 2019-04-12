const services = {
    socket: require('./services/socket'),
    mail: require('./services/mail')
}

async function start() {
    console.log("Iniciando servidor...")
    let sock = await services.socket()
    await services.mail(sock)
}

start()