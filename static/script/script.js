function sub(){
    let checked = []

    for (let i=0;i<91;i++){
        let temp = document.getElementById(String(i))
        if (temp.checked){
            checked.push(temp.name)
        }
    }
    console.log(checked)

    const xhr = new XMLHttpRequest()
    data = checked
    xhr.open('post','/recommend')
    xhr.send(data)
}

