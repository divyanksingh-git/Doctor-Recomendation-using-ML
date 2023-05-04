function sub(){
    let checked = []

    for (let i=0;i<91;i++){
        let temp = document.getElementById(String(i))
        if (temp.checked){
            checked.push(temp.name)
        }
    }

    const x = new XMLHttpRequest()
    data = checked
    x.open('post','/recommend')
    x.send(data)
}

