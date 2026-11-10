var itemList = [];
var addbutton = document.querySelector("#add");
addbutton.addEventListener("click", addList);

function addList() {
    var item = document.querySelector("#item").value;
    if (item != "") {
        itemList.unshift(item);
        document.querySelector("#item").value = "";
        document.querySelector("#item").focus();
    }
    showList();
}

function showList() {
    var list = "<ul>";
    for (var i = 0; i < itemList.length; i++) {
        list += "<li>" + itemList[i] + "<span class='close' id=" + i + "> 삭제 </span></li>";
    }
    list += "</ul>";
    document.querySelector("#itemList").innerHTML = list;

    var remove = document.querySelectorAll(".close");
    for (var i = 0; i < remove.length; i++) {
        remove[i].addEventListener("click", removeList);
    }
}

function removeList() {
    var id = this.getAttribute("id");
    
    var deletedItem = itemList[id];

    itemList.splice(id, 1);
    
    alert('"' + deletedItem + '"이(가) 삭제되었습니다.');
    
    showList();
}