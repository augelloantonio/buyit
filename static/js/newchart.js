var endpoint = "api/chart/data";
$.ajax({
    method: "GET",
    url: endpoint,
    success: function(data) {
      labels = data.labels;
      defaultData = data.default;
      order_label = data.order_label;
      label_months = data.months;
      earning_data = data.earning;
      
      //console.log(data.customers);
      setChart();
    },
    error: function(error_data) {
      console.log("error data");
      console.log(error_data);
    }
  });

  function setChart() {
    Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Monthly Earnings'
    },
    xAxis: {
        categories: label_months
    },
    series: [{
        name: 'Earning',
        data: earning_data,
        color: 'green'
    }]
});
}