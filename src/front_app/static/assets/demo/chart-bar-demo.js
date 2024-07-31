Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

fetch('http://expenses-app-svc.default.svc.cluster.local/expenses')
  .then(response => response.json())
  .then(data => {
    var groupedData = data.reduce((acc, item) => {
      const month = new Date(item.date).getMonth(); 
      if (acc[month]) {
        acc[month] += item.amount;
      } else {
        acc[month] = item.amount;
      }
      return acc;
    }, {});

    var labels = Object.keys(groupedData).map(month => new Date(2020, month).toLocaleString('default', { month: 'long' }));
    var amounts = Object.values(groupedData);

    var ctx = document.getElementById("myBarChart");
    var myLineChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: "Revenue",
          backgroundColor: "rgba(2,117,216,1)",
          borderColor: "rgba(2,117,216,1)",
          data: amounts,
        }],
      },
      options: {
        scales: {
          xAxes: [{
            time: {
              unit: 'month'
            },
            gridLines: {
              display: false
            },
            ticks: {
              maxTicksLimit: 6
            }
          }],
          yAxes: [{
            ticks: {
              min: 0,
              max: 15000,
              maxTicksLimit: 5
            },
            gridLines: {
              display: true
            }
          }],
        },
        legend: {
          display: false
        }
      }
    });
  })
  .catch(error => console.error('Error:', error));
