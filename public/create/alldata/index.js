$(".btn-search").click(function (e) {

    var url = $(this).data("url");

    // $("#HistoryStudentModal input[name='id']").val(id);
    console.log(url);
    $('.dataimg').attr("src", url);
    $('#HistoryStudentModal').modal('show');
})