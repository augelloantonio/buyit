$(document).ready(function() {
  var endpoint = "charts/chart/data";

  $.ajax({
    method: "GET",
    url: endpoint,
    success: function(data) {
      label_months = data.months_in_earning;
      earning_data = data.earning;
      label_orders_by_months = data.months_in_orders;
      label_product_name = data.product_name;
      orders_by_months = data.orders_by_months;
      quantity_product_sold = data.quantity_product_sold;
      label_rating = data.label_rating;
      score_rating = data.score_rating;
      console.log(label_rating);
      console.log(score_rating);

      setChart();
    },
    error: function(error_data) {
      console.log("error data");
      console.log(error_data);
    }
  });

  function setChart() {
    //Revenue Chart
    var ctx = document.getElementById("chartRevenue").getContext("2d");
    var chartRevenue = new Chart(ctx, {
      type: "bar",
      data: {
        labels: label_months,
        datasets: [
          {
            label: "€ Earned",
            data: earning_data,
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
    // Order Chart
    var ctx2 = document.getElementById("chartOrders").getContext("2d");
    var chartOrder = new Chart(ctx2, {
      type: "bar",
      data: {
        labels: label_orders_by_months,
        datasets: [
          {
            label: "Numbers of orders",
            data: orders_by_months,
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
    //Product Chart
    var ctx3 = document.getElementById("chartProducts").getContext("2d");
    var chartProducts = new Chart(ctx3, {
      type: "pie",
      data: {
        labels: label_product_name,
        datasets: [
          {
            label: "# Sold",
            data: quantity_product_sold,
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
    // Reviews chart
    var ctx4 = document.getElementById("chartReviews").getContext("2d");
    var chartProducts = new Chart(ctx4, {
      type: "doughnut",
      data: {
        labels: label_rating,
        datasets: [
          {
            label: "# Rating",
            data: score_rating,
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
