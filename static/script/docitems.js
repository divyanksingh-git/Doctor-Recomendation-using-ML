/*<div class="flex border-t border-gray-200 py-2">
                    <span class="text-gray-500">Disease: </span>
                    <span class="ml-auto text-gray-900">{{ dise }}</span>
                  </div>
                  <div class="flex border-t border-gray-200 py-2">
                    <span class="text-gray-500">Doctor Name: </span>
                    <span class="ml-auto text-gray-900"></span>
                  </div>
                  <div class="flex border-t border-gray-200 py-2">
                    <span class="text-gray-500">Mobile No: </span>
                    <span class="ml-auto text-gray-900"></span>
                  </div>
                  <div class="flex border-t border-b mb-6 border-gray-200 py-2">
                    <span class="text-gray-500">Address: </span>
                    <span class="ml-auto text-gray-900"></span>
                  </div>*/

var rev1 = document.getElementById("re")
var det1 = document.getElementById("de")
var doc1 = document.getElementById("do") 
var docblock = document.getElementById("docblock")

doc_info = doc_info.split("?")


var html = `<div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Disease: </span><span class="ml-auto text-gray-900">${doc_info[0]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Doctor Name: </span><span class="ml-auto text-gray-900">${doc_info[2]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Mobile No: </span><span class="ml-auto text-gray-900">${doc_info[3]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Address: </span><span class="ml-auto text-gray-900">${doc_info[4]}</span></div><div class="flex border-t border-b mb-6 border-gray-200 py-2"><span class="text-gray-500">Distance: </span><span class="ml-auto text-gray-900">${Math.floor(Math.random() * 2000) + 1}</span></div>`
docblock.innerHTML =  html

docimage = document.getElementById("docimage")


async function getUsers() {
  let response =await fetch("https://fakeface.rest/face/json?gender=male&minimum_age=35")
  let data = await response.json()
  return data
}

getUsers().then(data => docimage.innerHTML=`<img alt="doctor" width="400" height="400" src="${data.image_url}">`)



function det(){
  det1.className = "flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1"
  rev1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
  doc1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
var html = `<div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Disease: </span><span class="ml-auto text-gray-900"></span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Doctor Name: </span><span class="ml-auto text-gray-900"></span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Mobile No: </span><span class="ml-auto text-gray-900">${doc_info[3]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Address: </span><span class="ml-auto text-gray-900">${doc_info[4]}</span></div><div class="flex border-t border-b mb-6 border-gray-200 py-2"><span class="text-gray-500">Distance: </span><span class="ml-auto text-gray-900">${Math.floor(Math.random() * 2000) + 1}</span></div>`
docblock.innerHTML =  html
}

function doc(){
  doc1.className = "flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1"
  det1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
  rev1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
var html = `<div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Disease: </span><span class="ml-auto text-gray-900">${doc_info[0]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Doctor Name: </span><span class="ml-auto text-gray-900">${doc_info[2]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Mobile No: </span><span class="ml-auto text-gray-900">${doc_info[3]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Address: </span><span class="ml-auto text-gray-900">${doc_info[4]}</span></div><div class="flex border-t border-b mb-6 border-gray-200 py-2"><span class="text-gray-500">Distance: </span><span class="ml-auto text-gray-900">${Math.floor(Math.random() * 2000) + 1}</span></div>`
docblock.innerHTML =  html
}

function re(){
  rev1.className = "flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1"
  det1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
  doc1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
var html = `<div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Disease: </span><span class="ml-auto text-gray-900"></span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Doctor Name: </span><span class="ml-auto text-gray-900"></span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Mobile No: </span><span class="ml-auto text-gray-900">${doc_info[3]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Address: </span><span class="ml-auto text-gray-900">${doc_info[4]}</span></div><div class="flex border-t border-b mb-6 border-gray-200 py-2"><span class="text-gray-500">Distance: </span><span class="ml-auto text-gray-900">${Math.floor(Math.random() * 2000) + 1}</span></div>`
docblock.innerHTML =  html
}