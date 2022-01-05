/* Set up a data attribute for the links to use as the pseudo element content */

var anchors = document.querySelectorAll('.anchor-tooltip')
anchors.forEach(function (anchor) {
  var linkText = anchor.innerText
  console.log('Setting: ', linkText)
  anchor.setAttribute('data-linkText', linkText)
})
