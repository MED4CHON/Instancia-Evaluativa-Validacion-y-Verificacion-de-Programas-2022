//Definición de las funciones que se ejecutan al cargar la página.
let table = $('#tablaMesas').DataTable({
    "lengthMenu": [[5, 15, 20, -1], [5, 15, 20, "Todos"]],
    "processing": true,
    "serverSide": true,
    "ajax": {
        "url": "/api/mesas/",
        "type": "GET",
        "dataType": "json"
    },
    "columns": [
        { "data": "id" },
        { "data": "idFecha" },
        { "data": "idAsignatura" },
        { "data": "idCarrera" },
        { "data": null,
            "defaultContent": '<button type="button" class="btn btn-warning" style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;">Modificar</button>' + '&nbsp;&nbsp' +
                '<button type="button" class="btn btn-danger" style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;">Eliminar</button>'
        }
    ],
    "language": {
        url: "//cdn.datatables.net/plug-ins/1.10.19/i18n/Spanish.json"
    }
});

let id = 0;

$('#tablaMesas tbody').on('click', 'button', function () {
    let data = table.row($(this).parents('tr')).data();
    let class_name = $(this).attr('class');
    if (class_name == 'btn btn-warning') {
        // Botón Editar
        $('#idFecha').val(data['idFecha']);
        $('#idAsignatura').val(data['idAsignatura']);
        $('#idCarrera').val(data['idCarrera']);
        $('#type').val('edit');
        $('#modal_title').text('MODIFICAR');
        $("#myModal").modal('show');
    } else {
        // Botón Eliminar
        $('#modal_title').text('ELIMINAR');
        $("#confirm").modal('show');
    }

    id = data['id'];
});

$('form').on('submit', function (e) {
    e.preventDefault();
    //let $this = $(this);
    let datos = {
        idFecha: $('#idFecha').val(),
        idAsignatura: $('#idAsignatura').val(),
        idCarrera: $('#idCarrera').val(),
    };
    let type = $('#type').val();
    let method = '';
    let url = '/api/mesas/';
    if (type == 'new') {
        // nuevo
        method = 'POST';
    } else {
        // editar
        url = url + id + '/';
        method = 'PUT';
    }

    $.ajax({
        url: url,
        method: method,
        data: datos,
        dataType: 'json'
        })
        .done(function() {
        location.reload();
        })
        .fail(function(datos, textStatus, jqXHR) {
        location.reload();
    });

});

$('#confirm').on('click', '#delete', function (e) {
    $.ajax({
        url: '/api/mesas/' + id + '/',
        method: 'DELETE',
        dataType: 'json'
    }).done(function () {
        location.reload();
    }).fail(function (datos, textStatus, jqXHR) {
        alert({datos, textStatus, jqXHR});
        location.reload();
    });
});

$('#cancel').on('click', function (e) {
    location.reload();
});


$('#new').on('click', function (e) {
    $('#idFecha').val('');
    $('#idAsignatura').val('');
    $('#idCarrera').val('');
    $('#type').val('new');
    $('#modal_title').text('NUEVO');
    $("#myModal").modal('show');
});
