const cupcakesurl = "http://127.0.0.1:3000/api/cupcakes";
const cupcakecontainer = document.querySelector("ul");
const form = document.querySelector("form");

form.onsubmit = function (event) {
  event.preventDefault();
  let newcupcake = collectinputs(form);
  fetch(cupcakesurl, {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify(newcupcake),
  })
    .then((result) => result.json())
    .then((respond) => {
      const cupcakeElement = rendercupcake(respond.cupcake);
      cupcakecontainer.append(cupcakeElement);
    });
};

// let respond = {
//   cupcakes: [
//     {
//       flavor: "vanilla",
//       id: 2,
//       image: "https://tinyurl.com/demo-cupcake",
//       rating: 4.0,
//       size: "large",
//     },
//   ],
// };
fetch(cupcakesurl)
  .then((resolve) => resolve.json())
  .then((respond) => {
    respond.cupcakes.forEach((cupcake) => {
      const cupcakeElement = rendercupcake(cupcake);
      cupcakecontainer.append(cupcakeElement);
    });
  });

function rendercupcake(cupcake) {
  const { flavor, id, image, rating, size } = cupcake;
  let li = document.createElement("li");
  li.innerHTML = `
    <div>

    <img src="${image}"/>
    <div> flavor: ${flavor}</div>
    <div> rating: ${rating}</div>
    <div> size: ${size}</div>
    <div> id: ${id}</div>
    </div>
    `;
  return li;
}

function collectinputs(form) {
  const formData = new FormData(form);
  let flavor = formData.get("flavor");
  let image = formData.get("image");
  let rating = Number(formData.get("rating"));
  let size = formData.get("size");
  let newcupcake = { flavor, image, rating, size };
  console.log(newcupcake);
  return newcupcake;
}
