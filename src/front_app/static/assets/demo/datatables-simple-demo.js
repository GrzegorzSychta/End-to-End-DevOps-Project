document.addEventListener('DOMContentLoaded', function () {
    fetch('http://expenses-app-svc.default.svc.cluster.local/expenses')
        .then(response => response.json())
        .then(data => {
            let tableElement = document.querySelector('#expensesTable');
            if (tableElement) {
                let dataTable = new simpleDatatables.DataTable(tableElement, {
                    data: {
                        headings: ['Name', 'Amount', 'Description', 'Date', 'Category', 'Actions'],
                        data: data.map(item => [
                            item.name,
                            item.amount,
                            item.description,
                            item.date,
                            item.category,
                            `<button class="edit-btn" data-id="${item.id}">Edit</button>
                             <button class="delete-btn" data-id="${item.id}" style="margin-left: 5px;">Delete</button>`
                        ])
                    }
                });

                document.querySelector('#expensesTable tbody').addEventListener('click', function(e) {
                    const row = e.target.closest('tr');
                    const id = e.target.getAttribute('data-id'); 

                    if (e.target.className.includes('edit-btn')) {
                        let cells = row.querySelectorAll('td:not(:last-child)');
                        cells.forEach(cell => {
                            let text = cell.innerText;
                            cell.innerHTML = `<input type="text" value="${text}">`;
                        });
                        e.target.textContent = 'Save';
                        e.target.classList.add('save-btn');
                        e.target.classList.remove('edit-btn');
                        row.querySelector('.delete-btn').style.display = 'none'; 
                    } else if (e.target.className.includes('save-btn')) {
                        let updatedData = {};
                        let cells = row.querySelectorAll('td:not(:last-child)');
                        cells.forEach((cell, index) => {
                            let input = cell.querySelector('input');
                            let text = input ? input.value : '';
                            cell.innerText = text; 
                            switch (index) {
                                case 0: updatedData.name = text; break;
                                case 1: updatedData.amount = parseFloat(text); break; 
                                case 2: updatedData.description = text; break;
                                case 3: updatedData.date = text.split('T')[0]; break; 
                                case 4: updatedData.category = text; break;
                            }
                        });
                        e.target.textContent = 'Edit';
                        e.target.classList.add('edit-btn');
                        e.target.classList.remove('save-btn');
                        row.querySelector('.delete-btn').style.display = ''; 

                        fetch(`http://expenses-app-svc.default.svc.cluster.local/expenses/${id}`, {
                            method: 'PUT',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify(updatedData)
                        })
                        .then(response => response.json())
                        .then(data => console.log('Success:', data))
                        .catch(error => console.error('Error:', error));
                    } else if (e.target.className.includes('delete-btn')) {
                        fetch(`http://expenses-app-svc.default.svc.cluster.local/expenses/${id}`, {
                            method: 'DELETE',
                        })
                        .then(response => {
                            if (response.ok) {
                                let rowElement = e.target.closest('tr');
                                if (rowElement) {
                                    rowElement.remove();
                                }
                        }})
                        .catch(error => console.error('Error:', error));
                    }
                });
            }
        });
});
                    
