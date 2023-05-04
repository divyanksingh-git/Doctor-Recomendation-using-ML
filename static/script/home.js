homeimage = document.getElementById("homeimage")

async function getUsers() {
  let response =await fetch("https://fakeface.rest/face/json?gender=male&minimum_age=35")
  let data = await response.json()
  return data
}

getUsers().then(data => homeimage.innerHTML=`<img class="lg:w-2/6 md:w-3/6 w-5/6 mb-10 object-cover object-center rounded" src="${data.image_url}">`)