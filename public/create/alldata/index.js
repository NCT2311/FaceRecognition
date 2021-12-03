$(".btn-search").click(function (e) {

    var url = $(this).data("url");

    // $("#HistoryStudentModal input[name='id']").val(id);
    console.log(url);
    $('.dataimg').attr("src", url);
    $('#HistoryStudentModal').modal('show');
})
$('#tab-users').DataTable({
    "responsive": true, "lengthChange": true, "autoWidth": true, "searching": true, "bPaginate": false, "dom": "lfrti",
    language: {
        url: "//cdn.datatables.net/plug-ins/1.10.25/i18n/Vietnamese.json"
    } ,
    "columns": [
        { "width": "20%" },
        { "width": "20%" },
        { "width": "20%" },
        { "width": "20%" },
        { "width": "40%" },
        { "width": "20%" },
      ]
    })