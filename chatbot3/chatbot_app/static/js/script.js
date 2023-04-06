// Wait for the document to finish loading
document.addEventListener("DOMContentLoaded", function() {
    // Get a reference to the form element
    var form = document.querySelector("form");
  
    // Listen for the form submission event
    form.addEventListener("submit", function(event) {
      // Prevent the default form submission behavior
      event.preventDefault();
  
      // Get a reference to the file input and question input elements
      var fileInput = document.querySelector("#csv");
      var questionInput = document.querySelector("#question");
  
      // Create a FormData object and add the file and question inputs to it
      var formData = new FormData();
      formData.append("csv", fileInput.files[0]);
      formData.append("question", questionInput.value);
  
      // Send a POST request to the server with the FormData object
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/chatbot/");
      xhr.send(formData);
  
      // Listen for the server's response
      xhr.addEventListener("load", function() {
        // Get a reference to the answer element
        var answerElement = document.querySelector("#answer");
  
        // Set the answer element's innerHTML to the server's response
        answerElement.innerHTML = xhr.responseText;
      });
    });
  });
  