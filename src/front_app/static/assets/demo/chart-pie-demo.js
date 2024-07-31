Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

fetch('http://expenses-app-svc.default.svc.cluster.local/expenses')
  .then(response => response.json())
  .then(data => {
    var groupedData = data.reduce((acc, expense) => {
      if (acc[expense.category]) {
        acc[expense.category] += expense.amount;
      } else {
        acc[expense.category] = expense.amount;
      }
      return acc;
    }, {});

    var labels = Object.keys(groupedData);
    var amounts = Object.values(groupedData);

    var ctx = document.getElementById("myPieChart");
    var myPieChart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
          data: amounts,
          backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745', '#17a2b8', '#6610f2', '#6f42c1', '#e83e8c', '#fd7e14', '#20c997', '#fdcc00', '#4caf50', '#9c27b0', '#ff5722', '#795548', '#607d8b', '#ff9800', '#3f51b5', '#009688', '#ffeb3b'],
        }],
      },
    });
  })
  .catch(error => console.error('Error:', error));