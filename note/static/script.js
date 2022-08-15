 const addBox = document.querySelector(".add-box");
const popupbox = document.querySelector(".popup-box");
const closeIcon = popupbox.querySelector(".fa-xmark");
const addbtn = popupbox.querySelector("#addbtn")
const popupTitle = popupbox.querySelector("header p")
const titletag = popupbox.querySelector(".row input");
const desctag = popupbox.querySelector(".row textarea ");

const allnotes = JSON.parse(localStorage.getItem("notes") || "[]");
const months = ["jan", "feb", "mar", "apr", "may","jun","jul","aug","sep","oct","nov","dec"];

let isUpdate = false, updateId;
 
console.log("qdqkjdnqjdqj")



addBox.addEventListener("click",()=>{
 
    popupbox.classList.add("show");
})

closeIcon.addEventListener("click",()=>{
    isUpdate= false;  
    desctag.value = "";
    titletag.value = "";
    addbtn.innerText = "Add a Note";
    popupTitle.innerText ="Add Note"
    popupbox.classList.remove("show");
})

function showNotes(){
    document.querySelectorAll(".note").forEach(note => note.remove())
    allnotes.forEach((notes, index) => {
        let liTag = `<div class="note">
                        <div class="details">
                            <p> ${notes.title} </p>
                            <span>${notes.description}</span>
                        </div>

                        <div class="bottom-content">
                            <span>${notes.date}</span>  
                            <div class="setting">
                                <i onclick="showMenu(this)" class="fa-solid fa-ellipsis"></i>
                                <div class="menu">
                                    <div onclick="updateNote(${index},'${notes.title}','${notes.description}',  )"><i class="fa-solid fa-pen-to-square"></i>Edit</div>
                                    <div onclick="deleteNote(${index})"><i class="fa-solid fa-trash-can"></i>Delete</div>
                                </div>
                            </div>
                        </div>
                    </div>`;
        addBox.insertAdjacentHTML("afterend",liTag)
    });
}
showNotes()


function updateNote(noteId, title, desc ){
    isUpdate = true;
    updateId = noteId;
    addBox.click();
    desctag.value = desc;
    titletag.value = title;
    addbtn.innerText = "Upadate Note";
    popupTitle.innerText ="Upadate a Note"
     
}
function showMenu(elem){
    console.log(elem)
    elem.parentElement.classList.add("show")
    document.addEventListener("click",e =>{
        if(e.target.tagName != "I" || e.target != elem){
            elem.parentElement.classList.remove("show")
        }
    })
}

function deleteNote(noteId){
    allnotes.splice(noteId,1); 
    localStorage.setItem("notes", JSON.stringify(allnotes));
    showNotes()
}
addbtn.addEventListener("click",()=>{
    
    let noteTitle = titletag.value;
    let noteDesc = desctag.value;
    if(noteTitle || noteDesc){
        let dateObj = new Date();
        month = months[dateObj.getMonth()];
        day = dateObj.getDate();
        year = dateObj.getFullYear();

        let noteInfo = {
            title : noteTitle,
            description : noteDesc,
            date : `${month} ${day}, ${year}`,
        }

        
       if(!isUpdate ){
            allnotes.push(noteInfo);
       }else{
            notes[updateId] = noteInfo;
            isUpdate= false; 
       }
        allnotes.push(noteInfo);
        localStorage.setItem("notes", JSON.stringify(allnotes));
        closeIcon.click();
        console.log(allnotes);
        c
        showNotes()
    }
  
})