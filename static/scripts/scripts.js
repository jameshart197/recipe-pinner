const openInfoButtons = document.getElementsByClassName("open-info-button");
const closeInfoButtons = document.getElementsByClassName("close-info-button");
const dialogContent = document.getElementsByTagName("article")

openInfoButtons.array.forEach(element => {
    element.addEventListener("click", () => {
        modal.showModal()
    })
});

closeInfoButtons.array.forEach(element => {
    element.addEventListener("click", () => {
        modal.close()
    })
});

fetch(url).then((response)=> {
    return response.text();
}).then((html)=>{
    dialogContent.innerHTML = html;
}).catch((err)=> {
    console.warn('Something went wrong.', err);
    dialogContent.innerHTML = '';
})