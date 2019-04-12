$(document).ready(function () {
    const socket = io()
    let mail = '<div class="card border-light mb-3 animated fadeInDown masonry-brick masonry-brick--h" style="max-width: 21em;">' +
        '<div class="card-header">Área de suporte: Gestão de pessoal (GPE) </div>' +
        '<div class="card-body">' +
        '<h5 class="card-title">Assunto: Fechamento do período do ponto</h5>' +
        '<p class="card-text"> Atendente: Calixto Barbosa Filho' +
        'Chamado: 27968' +
        '<br>' +
        'Situação: RETORNO' +
        '<br>' +
        'Pendência: ATENDENTE' +
        '<br>' +
        '<br>' +
        'Detalhamento: "Bom dia!Hote fui efetuar o fechamento do período 02/2019 do ponto e não consigo pois aparece marcaçãoes ímpares, conforme o documento em anexo, sendo que as matrículas mencionadas não possuem essas divergencias.' +
        '<br>' +
        '<br>' +
        '</p></div>' +
        '<div class="card-footer">' +
        '<small class="text-muted">Colaborador: Eduarda Magalhães</small>' +
        '</div>' +
        '</div>'

    $("#mails").prepend(mail)

    socket.on('mensagem', (msg) => {
        $("#mails").prepend(mail)
        console.log(msg)
    })
    socket.on('disconnect', function () {
        $("#status").removeClass("fas fa-link text-success")
        $("#status").addClass("fas fa-unlink text-danger")
    })

    socket.on('connect', function () {
        $("#status").removeClass("fas fa-unlink text-danger")
        $("#status").addClass("fas fa-link text-success")
    })
});