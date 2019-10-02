$(document).ready(function() {
  var endpoint = "charts/chart/data";
  var defaultData = [];
  var labels = [];

  $.ajax({
    method: "GET",
    url: endpoint,
    success: function(data) {
      (labels = data.labels), (defaultData = data.default);
      console.log(defaultData);
      //console.log(data.customers);
      setChart();
    },
    error: function(error_data) {
      console.log("error data");
      console.log(error_data);
    }
  });

  function setChart() {
    var ctx = document.getElementById("myChart").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          {
            label: "# of Votes",
            data: defaultData,
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)"
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)"
            ],
            borderWidth: 1
          }
        ]
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true
              }
            }
          ]
        }
      }
    });
  }
});
