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
var book = document.getElementById("book")

var bookhtml = book.innerHTML

doc_info = doc_info.split("?")


var html = `<div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Disease: </span><span class="ml-auto text-gray-900">${doc_info[0]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Doctor Name: </span><span class="ml-auto text-gray-900">${doc_info[2]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Mobile No: </span><span class="ml-auto text-gray-900">${doc_info[3]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Address: </span><span class="ml-auto text-gray-900">${doc_info[4]}</span></div><div class="flex border-t border-b mb-6 border-gray-200 py-2"><span class="text-gray-500">Distance: </span><span class="ml-auto text-gray-900">${Math.floor(Math.random() * 2000) + 1}</span></div>`
docblock.innerHTML =  html
book.innerHTML = bookhtml



function det(){
  det1.className = "flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1"
  rev1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
  doc1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
var html = `<p>${doc_info[2]} is a trailblazer in the field of telemedicine. With over a decade of experience in virtual healthcare, he has helped countless patients receive high-quality medical care from the comfort of their own homes. He innovative approach to healthcare has earned her recognition as one of the top telemedicine physicians in the country.</p>`
docblock.innerHTML =  html
book.innerHTML=""
}

function doc(){
  doc1.className = "flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1"
  det1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
  rev1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
var html = `<div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Disease: </span><span class="ml-auto text-gray-900">${doc_info[0]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Doctor Name: </span><span class="ml-auto text-gray-900">${doc_info[2]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Mobile No: </span><span class="ml-auto text-gray-900">${doc_info[3]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Address: </span><span class="ml-auto text-gray-900">${doc_info[4]}</span></div><div class="flex border-t border-b mb-6 border-gray-200 py-2"><span class="text-gray-500">Distance: </span><span class="ml-auto text-gray-900">${Math.floor(Math.random() * 2000) + 1}</span></div>`
docblock.innerHTML =  html
book.innerHTML = bookhtml
}

function re(){
  rev1.className = "flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1"
  det1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
  doc1.className = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1"
var html = "<table><tr><th>Reviewer</th><th>Review</th></tr><tr><td>Badal Goit</td><td>He is an excellent physician. He takes the time to listen to his patients and is always willing to answer any questions they may have. He is knowledgeable, professional, and caring, and I would highly recommend him to anyone.</td></tr><tr> <td>Akash verma</td><td>he is an amazing doctor. He is very patient and attentive, and he always puts his patients first. He is very knowledgeable and takes the time to explain everything in detail. I would definitely recommend him to anyone in need of a good doctor.</td></tr><tr> <td>Abhishek Pal</td><td>I have been seeing him for years and have always been very happy with his care. He is very thorough and always takes the time to explain everything to me. He is a great doctor, and I would highly recommend him.</td></tr><tr> <td>Ayush Kumar Patel</td><td>He is an amazing doctor. She is very compassionate and caring and always takes the time to listen to her patients. She is very knowledgeable and always explains everything in detail. I would highly recommend her to anyone in need of a good doctor.</td></tr><tr> <td>Divyank Singh</td><td>He is an excellent physician. She is very professional and always puts her patients first. She is very thorough and always takes the time to answer any questions her patients may have. I would definitely recommend her to anyone in need of a good doctor.</td></tr><tr> <td>Mohit Maurya</td><td>I have been seeing him for several years and have always been very happy with her care. She is very knowledgeable and always takes the time to explain everything in detail. She is a great doctor, and I would highly recommend her.</td></tr></table>"
docblock.innerHTML =  html
book.innerHTML=""
}

function c(){
  console.log("p")
}