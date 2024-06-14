fetch("https://api.memegen.link/templates")
  .then((response) => response.json())
  .then((data) => {
    setTemplateDescription(data.length);
    fillTemplates(data);
  });

function setTemplateDescription(length) {
  document.getElementById("templatesDescription").innerHTML =
    "Browse through our " + length + " templates.";
}

function fillTemplates(templates) {
  for (var i = 0; i < templates.length; i++) {
    var template = templates[i];
    document.getElementById("templatesContent").innerHTML += `
    <div class="col" onclick=selectTemplate("${template.id}")>
        <div class="card mt-4">
          <img
            src="${template.blank}?height=500&width=800 "
            alt="${template.name}"
          />
          <div class="card-body">
            <h5 class="card-title">${template.name}</h5>
          </div>
        </div>
    </div>
    `;
  }
}

function selectTemplate(templateId) {
  document.getElementById("templateSelectedName").innerHTML = templateId;
  document.getElementById("templateImage").src =
    "https://api.memegen.link/images/" + templateId + "/_/_";
  document
    .getElementById("generateButton")
    .setAttribute("onclick", `generateMeme("${templateId}")`);
}

function generateMeme(templateId) {
  var upperText = document.getElementById("upperText").value || "_";
  var lowerText = document.getElementById("lowerText").value || "_";

  document.getElementById(
    "templateImage"
  ).src = `https://api.memegen.link/images/${templateId}/${upperText}/${lowerText}`;
}
