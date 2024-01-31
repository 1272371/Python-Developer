// script.js

// Function to load events
function loadEvents() {
  $.ajax({
    type: "GET",
    url: "/",
    success: function (data) {
      displayEvents(data); // Display all events initially
    },
    error: function (xhr, status, error) {
      console.error("Error loading events:", error);
    },
  });
}

// Function to display events
function displayEvents(events) {
  var eventsList = $("#eventsList");
  eventsList.empty();
  if (events.length === 0) {
    eventsList.append("<li class='list-group-item'>No events found</li>");
  } else {
    events.forEach(function (event) {
      eventsList.append(
        `<li class="list-group-item">${event.title} - ${event.description} - ${event.date} ${event.time}</li>`
      );
    });
  }
}

// Add event form submission
$("#eventForm").submit(function (event) {
  event.preventDefault();
  $.ajax({
    type: "POST",
    url: "/",
    data: $(this).serialize(),
    success: function (response) {
      loadEvents(); // Reload events after adding a new event
      $("#eventForm")[0].reset();
    },
    error: function (xhr, status, error) {
      console.error("Error adding event:", error);
    },
  });
});

// Search button click event
$("#searchButton").click(function () {
  var searchTitle = $("#searchTitle").val().toLowerCase(); // Get search query
  $.ajax({
    type: "GET",
    url: "/",
    success: function (data) {
      var filteredEvents = data.filter(function (event) {
        return event.title.toLowerCase().includes(searchTitle); // Filter events by title
      });
      displayEvents(filteredEvents); // Display filtered events
    },
    error: function (xhr, status, error) {
      console.error("Error loading events:", error);
    },
  });
});

// Load events on page load
$(document).ready(function () {
  loadEvents();
});
