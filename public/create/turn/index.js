$(document).ready(function () {
    var firtname = document.getElementById('firstname');
    var lastname = document.getElementById('lastname');
    var timeaccess = document.getElementById('timeaccess');
    $.post('/admin/getdata', {}, function (data) {
        //console.log(data.flag.Flagcheck);
        if (data.flag.Flagcheck == false) {
            document.getElementById('imagecheck').src = '../img/layout1.png';
            firtname.innerHTML = "Undefined";
            lastname.innerHTML = "Undefined";
            timeaccess.innerHTML = "Undefined";
        }
        else {
            document.getElementById('imagecheck').src = data.list.urlimg;
            if (!data.list.Status && data.flag.Flagcheck == true) {
                firtname.innerHTML = "Undefined";
                lastname.innerHTML = "Undefined";
                timeaccess.innerHTML = moment(data.list.CreateAt).format("lll");
                console.log(data.list.CreateAt);
            }
            else {
                // Hơi thừa vì nếu là người quen thì ko flag check
                if (data.list.Status && data.flag.Flagcheck == true) {
                    $.post('/admin/getinfo', { id: data.list.Personid }, function (data2) {
                        //console.log(data2);
                        firtname.innerHTML = data2.person.Fname;
                        lastname.innerHTML = data2.person.Lname;
                        timeaccess.innerHTML = moment(data.list.CreateAt).format("lll");
                    });
                }
            }
        }
        $('#buttoncheck').click(function (e) {
            $('#confirmPersonModal').modal('show');
        })
        $('#buttoncheck1').click(function (e) {
            $('#refusePersonModal').modal('show');
        })
    });

});