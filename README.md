# The Lucid Dreaming Journey
#### Video Demo:  https://youtu.be/UzBr9B7Oogw
#### Description:
The Lucid Dreaming Journey is a mock app that introduces us to the world of lucid dreaming.

This app uses Flask and Jinja to render the HTML and Bootstrap for rapid styling.

My main thought was to make layout.html to reuse and implement the navbar. When rendering templates on the backend, I will assign each template a "tab" value, which will be useful for the navbar links highlighting. Example: when clicking Introduction once on the page, the Introduction text on the navbar will light up.

First, the Main Page contains a beautiful pixel art GIF that acts as a background, the title, and a container that holds two links, one that redirects to the Introduction page and the other one to the Dream Journal.Then comes the Introduction page. It contains basic info about lucid dreaming methods and basic awareness tips with a link to the dream journal. I used a table to display the methods and their difficulty level.

I also added a Dream Journal page where users can record their dreams, which is one of the fundamentals of lucid dreaming. It works by first opening a bootstrap modal when clicking the "Add Dream" button; the form inside the modal contains three inputs: "Dream Title," "Dream Desc," and "Lucid?" When clicking on the "Add Dream" button, it will fire a javascript function that first gets the user browser's local storage and searches for the key "dreams"; if not found, it will just use an empty array, then update the array with the new dream before updating the local storage and reloading the page. For the dreams rendering on screen, JavaScript will get the dreams array, and for each dream, render an HTML container with the dream info, name, and desc, and a button "Delete" that will update the local storage value by using the filter function that will remove the currently selected dream. About the border, it will change color dynamically by checking if the dream is lucid; if yes, it will change to blue. The user can also download a JSON file containing all of their dreams by clicking on the "Save to JSON" file.

Finally, my quiz page will test the user's knowledge about lucid dreaming. All the questions must be in the "questions.json" file. Each click on a button will send an HTTP POST request to the server with all the data and the current question index variable to handle which question the user is currently in. Once every answer is submitted, it will redirect to the "quizresult" route and render the score dynamically by getting the local storage key "fr" (final result) and formatting a string with the value.

