const allBox=document.querySelectorAll('.box')
const allTasks = document.querySelectorAll('.task');

allTasks.forEach(task => {
    task.addEventListener('dragstart', () => {
        task.classList.add('is-dragging');
    });

    task.addEventListener('dragend', () => {
        task.classList.remove('is-dragging');
    });
});
allBox.forEach(box=>{
    box.addEventListener('dragover', (e) => {
        e.preventDefault();
        const add = document.querySelector('.is-dragging');
        box.appendChild(add);

});
});
// //deadline 
// function addDeadline(task, deadline) {
//     task.deadline = new Date(deadline);
// }

// // Function to check if a task is overdue
// function isTaskOverdue(task) {
//     return task.deadline < new Date();
// }
// function addDeadline(task, deadline) {
//     task.deadline = new Date(deadline);
// }

// Function to check if a task is overdue
function isTaskOverdue(task) {
    return task.deadline < new Date();
}
//adding new task
const form=document.querySelector('#add-form');
const input=document.querySelector('#todoinput');
const todobox=document.querySelector('#todo');
form.addEventListener('submit',e=>{
    e.preventDefault();
    const newtask=input.value;
    if(!newtask)return;
    //<p class="task" draggable="true">palying</p>
    const news=document.createElement('p');
    news.innerHTML=newtask;
    news.classList.add('task');
    news.setAttribute('draggable','true');
    news.addEventListener('dragstart', () => {
        news.classList.add('is-dragging');
    });

    news.addEventListener('dragend', () => {
        news.classList.remove('is-dragging');
    });
    todobox.appendChild(news);
    input.value="";
})