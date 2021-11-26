document.write('<script src="../../moment/moment.min.js"></script>');

function fireSweetAlert1() {
    Swal.fire({
        icon: 'info',
        title: 'Error!',
        text: 'Username already used'
    })
}
function fireSweetAlert() {
    Swal.fire(
        'Good job!',
        'Succesfully!',
        'success'
    )
}
$(".btn-search").click(function (e) {
    var id = $(this).data("id");
    var lastName = $(this).data("lname");
    var firstName = $(this).data("fname");
    // $("#HistoryStudentModal input[name='id']").val(id);
    $("#HistoryStudentModal input[name='lname']").val(lastName);
    $("#HistoryStudentModal input[name='fname']").val(firstName);
    
    $.post("/history/getallTurn", { id: id }, function (historyList) {
        console.log(historyList.list[0].createAt);
        // var t = $('#historyModal').DataTable();
        var t = $('.historyModal').DataTable({
            "searching": false, // false to disable search (or any other option)
            "bDestroy": true
            });
        t.rows().remove().draw();
        for (var i = 0; i < historyList.list.length; i++) {
            //console.log(historyList.turnOfStudent[i]['creatAt']);${historyList.list[i].urlimg}
            t.row
            .add([                                                             
            `<center><td>  <img class='dataimg' src="${historyList.list[i].urlimg}" alt="Image"></img></td></center>`,
            `<center ><td > ${moment(historyList.list[i].createAt).format('lll')} </td></center>`,
            ])
            .draw(false);
        
        }
    });  
    $('#HistoryStudentModal').modal('show');
})



  // Lấy phần Modal
