$(function() {
  // Set up the carousel's "state"
  var prevIndex = 0;
  var currentIndex = 1;
  var nextIndex = 2;
  var lastIndex = $('#quotes-carousel').find('.quote').length - 1;

  // Click actions to listen for
  $('#quotes-carousel').on('click', '.previous', showQuote);
  $('#quotes-carousel').on('click', '.next', showQuote);
  $('#quotes-carousel-pips').on('click', '.pip', showFromPip);

  // Generate pips
  generatePips();

  // Cycle automatically
  var carouselRunning = true;

  // Set the carousel working
  var interval = setInterval(function() {
    if (carouselRunning) {
      showNextQuote();
    }
  }, 4000);

  function showNextQuote() {
    // Calculate the indices needed to show the next quote
  }

  function showQuote(event) {
    // Get the index of the clicked quote and show it
  }

  function updateState(index) {
    // Calculates the previous and next indices, and updates the carousel
  }

  function updateCarouselPosition() {
    // Update the carousel depending on the "state"
  }

  function generatePips() {
    // Add pips to the ul element in index.html
  }

  function updatePips() {
    // Update the classes on the pips depending on the current indices
  }

  function showFromPip(event) {
    // Helper for when someone clicks a pip
  }

  function setLeftClass() {
    // For when we want the item to appear from the left side if it's "earlier" in the list
  }

});

