$(document).ready(function () {
    var firtname =  document.getElementById('firstname');
    var lastname =  document.getElementById('lastname');
    var timeaccess =  document.getElementById('timeaccess');
    $.post('/admin/getdata', {}, function (data) {
        //console.log(data.flag.Flagcheck);
        if (data.flag.Flagcheck==false) {
            document.getElementById('imagecheck').src = '../img/layout1.png';
        }

        else
            document.getElementById('imagecheck').src = data.list.urlimg;
        if(!data.list.status && data.flag.Flagcheck==false ){
            firtname.innerHTML = "Undefined";
            lastname.innerHTML = "Undefined";
            timeaccess.innerHTML ="Undefined";
        }
        else{
            if(!data.list.status && data.flag.Flagcheck==true){
                firtname.innerHTML = "Undefined";
                lastname.innerHTML = "Undefined";
                timeaccess.innerHTML =data.list.CreateAt;
                console.log(data.list.CreateAt);
            }
            else{
                // gọi API lấy data người quen
            }
        }
    });
    
});