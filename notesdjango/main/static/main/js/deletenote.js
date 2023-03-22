function DeleteNote() {
    this.form = document.getElementById("newNote");
    this.deleteButton = document.getElementById("delete");
    this.id = document.getElementById("idMysql");
    this.dataButton = document.getElementById("json");
    this.initSettings();
}

DeleteNote.prototype.initSettings = function() {

    this.deleteButton.addEventListener('click', (event) => {
        event.preventDefault();
        console.log("hello world from delete");
        let number = this.id.value;
        console.log("hello world from delete ", number);
        let url = "http://localhost:8000/" + number + "/delete";
        this.form.action = url;
        this.form.submit();
//        location.href = "http://localhost:8080/new";
    });

    this.dataButton.addEventListener('click', () => {
        this.testRestApi()
    });
}

DeleteNote.prototype.testRestApi = function() {
    let dataString;
    let url = new URL("http://localhost:8000/getdata");
    url.searchParams.set('test', "hello");
    fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            }})
            .then(response => response.text())
            .then(data => {
                dataString = data;
                console.log(dataString);

            });
}

const deleteAction = new DeleteNote();