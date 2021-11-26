$("#form-add-user").submit(function (e) {
    e.preventDefault();
    //Write code to check if student id is existed!
    //Camel case
    var studentId = $("input[name='username']").val();
    var form = $(this);
    // console.log(studentId);
    //AJAX
    $.post("/user/checkId", { id: studentId }, function (data) {
        console.log(data);
        if (data.status == "FOUND") {
            //alert("Đã tồn tại mã số sinh viên này!");
            fireSweetAlert1();
        }
        else {
            fireSweetAlert();
              setTimeout(function () {
                form.unbind("submit").submit();
              }, 1000);
            // console.log("NOT FOUND");

        }
    });
});
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
$(".btn-edit").click(function (e) {
    var password = $(this).data("password");
    var username = $(this).data("username");
    $("#EditUserModal input[name='username']").val(username);
    $("#EditUserModal input[name='password']").val(password);
    $('#EditUserModal').modal('show');
});

$(".btn-delete").click(function (e) {
    var username = $(this).data("username");
    $("#DeleteUserModal input[name='username']").val(username);
    $('#DeleteUserModal').modal('show');
});