doc_info = doc_info.split("?")


var bookdis = document.getElementById("disease")
var html =`<option value="${doc_info[0]}">${doc_info[0]}</option>`
bookdis.innerHTML = html

var bookdoc = document.getElementById("doctor")
var html =`<option value="${doc_info[2]}">${doc_info[2]}</option>`
bookdoc.innerHTML = html

function book(){
  var name= document.getElementById("name").value 
  var email= document.getElementById("email").value 
  var phone = document.getElementById("phone").value  
  var date = document.getElementById("date").value 
  var time = document.getElementById("time").value 
  var disease = document.getElementById("disease").value  
  var doctor = document.getElementById("doctor").value 
  
  var data =[name,email,phone,date,time,disease,doctor]
  console.log(data)
  const z = new XMLHttpRequest()
    z.open('post','/data')
    z.send(data)

    alert('Your booking has been confirmed',onclose=window.location='/submit')

}