// script.js

/**
 * Handle navigation menu functionality.
 */
const list = document.querySelectorAll(".nav-list li");

list.forEach((item) => {
  item.addEventListener("click", function (e) {
    list.forEach((li) => li.classList.remove("active"));
    e.currentTarget.classList.add("active");

    // Get the text content of the clicked menu item
    const menuItemText = e.currentTarget.classList.textContent.trim();

    // Hide or show the corresponding div based on the clicked menu item
    if (menuItemText === "ADD") {
      $(".sidebar").addClass("hide");
      $(".content").addClass("visible");
    } else if (menuItemText === "VIEW") {
      document.querySelector(".sidebar").style.display = "block";
      document.querySelector("#content").style.display = "none";
    }
  });
});

/**
 * Load events from the server.
 */ // script.js

// Fetch events from the server
function loadEvents() {
  fetch("/api/events/")
    .then((response) => response.json())
    .then((data) => displayEvents(data))
    .catch((error) => console.error("Error loading events:", error));
}

// Handle form submission and validate input fields
document
  .getElementById("eventForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Get form inputs
    var titleInput = document.getElementById("title").value;
    var descriptionInput = document.getElementById("description").value;
    var dateInput = document.getElementById("date").value;
    var timeInput = document.getElementById("time").value;

    // Validate form inputs...
    if (!titleInput || !descriptionInput || !dateInput || !timeInput) {
      alert("Please fill all the fields");
      return;
    }

    // If the form passes validation, send a POST request to the server
    var eventObject = {
      title: titleInput,
      description: descriptionInput,
      date: dateInput,
      time: timeInput,
    };

    fetch("/api/events/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(eventObject),
    })
      .then((response) => response.json())
      .then((data) => {
        // Add event to events list
        events.push(eventObject);

        // Display updated events list
        displayEvents(events);

        // Clear the form inputs (optional)
        this.reset();
      })
      .catch((error) => console.error("Error:", error));
  });

// Handle search button click event
$("#searchButton").click(function () {
  var searchTitle = $("#searchTitle").val().toLowerCase();

  fetch(`/api/events/titleInput?title=${searchTitle}`)
    .then((response) => response.json())
    .then((data) => displayEvents(data))
    .catch((error) => console.error("Error loading events:", error));
});
