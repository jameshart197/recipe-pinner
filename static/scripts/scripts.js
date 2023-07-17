let openInfoButtons = document.getElementsByClassName("info-button");
const dialogContent = document.getElementsByTagName("dialog")[0];

function closeButton() {
    dialogContent.close();
}

[...openInfoButtons]?.forEach(element => {
    console.log("I am working");
    element.addEventListener("click", () => {
        const mealId = element.dataset.meal;
        const url = `info/dialog/${mealId}`;
        dialogContent.showModal();
        fetch(url).then((response)=> {
            return response.text();
        }).then((html)=>{
            dialogContent.children[1].innerHTML = html;
            // .children[1] targets the article within the dialogContent section
        }).catch((err)=> {
            console.warn('Something went wrong.', err);
            dialogContent.innerHTML = '';
        })
    })
});

// clicking outside the dialogue box closes box

dialogContent.addEventListener("click", e => {
    const dialogDimensions = dialogContent.getBoundingClientRect()
    if (
        e.clientX < dialogDimensions.left ||
        e.clientX > dialogDimensions.right ||
        e.clientY < dialogDimensions.top || 
        e.clientY > dialogDimensions.bottom
    ) {
        dialogContent.close();
    }
})