document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('to-do-form');
    const input = document.getElementById('to-do-input');
    const list = document.getElementById('to-do-list');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        addTask(input.value);
        input.value = '';
    });

    function addTask(task) {
        const li = document.createElement('li');
        li.textContent = task;
        const deleteButton = document.createElement('span');
        deleteButton.textContent = '✖';
        deleteButton.classList.add('delete');
        deleteButton.addEventListener('click', () => {
            list.removeChild(li);
        });
        li.appendChild(deleteButton);
        list.appendChild(li);
    }
});
