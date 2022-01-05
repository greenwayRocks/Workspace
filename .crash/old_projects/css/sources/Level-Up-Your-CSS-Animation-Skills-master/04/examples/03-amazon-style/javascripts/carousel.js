$(function() {
  // Set up the carousel's "state"
  var prevIndex = 2;
  var currentIndex = 0;
  var nextIndex = 1;
  var lastIndex = $('#carousel').find('.item').length - 1;

  // Actions to listen for
  $('#carousel').on('click', '.previous', showQuote);
  $('#carousel').on('click', '.next', showQuote);
  // $('#carousel-pips').on('click', '.pip', showFromPip);
  $('#control-previous').click(showPrevious);
  $('#control-next').click(showNextQuote);

  // Cycle automatically
  var carouselRunning = true;
  var carouselRestartTimeout;

  delay = 5000;

  showNextQuote();

  // Set the carousel working
  var interval = setInterval(function() {
    if (carouselRunning) {
      showNextQuote();
    }
  }, delay);

  function showNextQuote() {
    // Calculate the indices needed to show the next quote
    if (currentIndex === lastIndex) {
      currentIndex = 0;
    } else {
      currentIndex++;
    }
    updateState(currentIndex, "left");
    carouselRunning = false;
  }

  function showPrevious() {
    // Calculate the indices needed to show the next quote
    if (currentIndex === 0) {
      currentIndex = lastIndex;
    } else {
      currentIndex--;
    }
    updateState(currentIndex, "right");
    carouselRunning = false;
  }

  function showQuote(event) {
    // Get the index of the clicked quote and show it
    if ($(event.target).hasClass('quote')) {
      var target = $(event.target);
    } else {
      var target = $(event.target).parent();
    }
    var index = $('.item').index(target);
    updateState(index);

    // Since this is by click, pause the automatic movement for a few seconds
    clearTimeout(carouselRestartTimeout);
    carouselRunning = false;
    carouselRestartTimeout = setTimeout(function() {
      carouselRunning = true;
    }, 10000);
  }

  function updateState(index, direction) {
    // Calculates the previous and next indices, and updates the carousel
    prevIndex = index === 0 ? lastIndex : index - 1;
    currentIndex = index;
    nextIndex = index === lastIndex ? 0 : index + 1;
    updateCarouselPosition(direction);
  }


  function updateCarouselPosition(direction) {
    // Remove any previous, current, next classes
    $('#carousel').find('.previous').removeClass('previous');
    $('#carousel').find('.current').removeClass('current');
    $('#carousel').find('.next').removeClass('next');
    var allQuotes = $('#carousel').find('.item');
    $(allQuotes[prevIndex]).addClass('previous');
    $(allQuotes[currentIndex]).addClass('current');
    $(allQuotes[nextIndex]).addClass('next');
    $(allQuotes[currentIndex]).css('z-index', 10)
    if (direction === "right") {
      $(allQuotes[prevIndex]).css('z-index', 0);
      $(allQuotes[nextIndex]).css('z-index', 1);
    } else {
      $(allQuotes[prevIndex]).css('z-index', 1);
      $(allQuotes[nextIndex]).css('z-index', 0);
    }
  }

  // Lastly, add a listener for situations where the browser is in another tab / not visible
  document.addEventListener("visibilitychange", function() {
    if (document.hidden) {
      carouselRunning = false;
    } else {
      carouselRunning = true;
    }
  });

});

