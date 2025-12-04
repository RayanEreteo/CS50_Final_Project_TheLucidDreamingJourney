# The Lucid Dreaming Journey
#### Video Demo:  https://youtu.be/UzBr9B7Oogw
#### Description:
The Lucid Dreaming Journey is a mock app that introduces us to the world of lucid dreaming. 

This app uses Flask and Jinja to render the HTML.

My main thought was to make layout.html to reuse and implement the navbar. When rendering templates on the backend, I will assign each template a "tab" value, which will be useful for the navbar links highlighting. Example: when clicking Introduction once on the page, the Introduction text on the navbar will light up.First, the Main Page contains a beautiful pixel art GIF that acts as a background, the title, and a container that holds two links, one that redirects to the Introduction page and the other one to the Dream Journal.

Then comes the Introduction page. It contains basic info about lucid dreaming methods and basic awareness tips. I used a table to display the methods and their difficulty level.I also added a Dream Journal page where users can record their dreams, which is one of the fundamentals of lucid dreaming. It works by first opening a bootstrap modal when clicking the "Add Dream" button; the form inside the modal contains three inputs: "Dream Title," "Dream Desc," and "Lucid?"When clicking on the "Add Dream" button, it will fire a javascript function that first gets the user browser's local storage and searches for the key "dreams"; if not found, it will just use an empty array, then update the array with the new dream before updating the local storage and reloading the page.For the dreams rendering on screen, JavaScript will get the dreams array, and for each dream, render an HTML container with the dream info, name, and desc, and will change the border color based on lucidity.

Finally, my quiz page will test the user's knowledge about lucid dreaming; once every answer is submitted, it will redirect to the "quizresult" route and show the score.
