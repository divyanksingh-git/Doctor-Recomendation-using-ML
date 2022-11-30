var doc_info = "AIDS?6?Mst. Ilham Munira?1732267340?Sadar Hospital, Chapainawabganj."
        doc_info = doc_info.split("?")
var docblock = document.getElementById("docblock")
var html = `<div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Disease: </span><span class="ml-auto text-gray-900">${doc_info[0]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Doctor Name: </span><span class="ml-auto text-gray-900">${doc_info[2]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Mobile No: </span><span class="ml-auto text-gray-900">${doc_info[3]}</span></div><div class="flex border-t border-b mb-6 border-gray-200 py-2"><span class="text-gray-500">Address: </span><span class="ml-auto text-gray-900">${doc_info[4]}</span></div>`
docblock.innerHTML =  html

var docimage = document.getElementById("docimage")

async function getUsers() {
  let response =await fetch("https://fakeface.rest/face/json?gender=male&minimum_age=35")
  let data = await response.json()
  return data
}

getUsers().then(data => docimage.innerHTML=`<img alt="doctor" width="400" height="400" src="${data.image_url}">`)