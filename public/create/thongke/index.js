// Get context with jQuery - using jQuery's .get() method.
var data = {
    labels: ["10", "20","30", "40", "50","60", "70", "80", "90" , "100"],
    datasets: [{
      label: 'Exact ratio',
      data: [78, 79, 80, 80,80, 81 , 82 ,83 ,85 ,87 ],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
      ],
      borderColor: [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
      ],
      borderWidth: 1,
      fill: false
    }]
  };
  var options = {
    responsive: true,
    scales: {
      yAxes: [{
        ticks: {
            max: 100,
            min: 0,
          beginAtZero: true
        }
      }]
    },
    legend: {
      display: false
    },
    elements: {
      point: {
        radius: 0
      }
    }

  };
if ($("#barChart").length) {
    var barChartCanvas = $("#barChart").get(0).getContext("2d");
    // This will get the first returned node in the jQuery collection.
    var barChart = new Chart(barChartCanvas, {
      type: 'bar',
      data: data,
      options: options
    });
  }
  function getMonday(d) {
    d = new Date(d);
    var day = d.getDay(),
        diff = d.getDate() - day + (day == 0 ? -6:1); // adjust when day is sunday
    return new Date(d.setDate(diff) );
  }
  var monday = getMonday(new Date());
  monday.setHours(0, 0, 0);
//   console.log(monday);
  var sun = 0;
  var mon = 0;
  var tue = 0;
  var wed = 0;
  var thu = 0;
  var fri = 0;
  var sat = 0;
  $.post('/thongke/getall', {}, function (turn) {
      list = turn.list;
      for(var i = 0 ; i < list.length; i++){
        if (new Date(list[i].CreateAt) >= monday ){
            // console.log(list[i]);
            switch(new Date(list[i].CreateAt).getDay() ){
                case 0: sun++; break;
                case 1: mon++; break;
                case 2: tue++; break;
                case 3: wed++; break;
                case 4: thu++; break;
                case 5: fri++; break;
                case 6: sat++; break;
            }
        }
    }
 
var areaData = {
    labels: [ "Monday", "Tuesday", "Wednesday", "Thursday" , "Friday ","Saturday","Sunday"],
    datasets: [{
      label: 'Total arrivals',
      data: [mon,tue,wed,thu,fri,sat,sun],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1,
      fill: true, // 3: no fill
    }]
  };

  var areaOptions = {
    plugins: {
      filler: {
        propagate: true
      }
    },
    scales: {
        yAxes: [{
          ticks: {
              min: 0,
            beginAtZero: true
          }
        }]
      },
  }
  if ($("#areaChart").length) {
    var areaChartCanvas = $("#areaChart").get(0).getContext("2d");
    var areaChart = new Chart(areaChartCanvas, {
      type: 'line',
      data: areaData,
      options: areaOptions
    });

  }
      })