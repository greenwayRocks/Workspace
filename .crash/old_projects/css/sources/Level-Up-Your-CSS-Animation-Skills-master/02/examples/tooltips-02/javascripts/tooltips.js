/* Function to add tooltips to anchors */

var anchors = document.querySelectorAll('.anchor-tooltip');
anchors.forEach(function(anchor) {
  var toolTipText = anchor.getAttribute('title'),
      toolTip = document.createElement('span');
  toolTip.className = 'title-tooltip';
  toolTip.innerHTML = toolTipText;
  anchor.appendChild(toolTip);
});
