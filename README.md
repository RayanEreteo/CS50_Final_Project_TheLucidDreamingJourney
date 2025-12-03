# The Lucid Dreaming Journey
#### Video Demo:  <URL HERE>
#### Description:
The Lucid Dreaming Journey is a mock app that introduces us to the world of lucid dreaming. 

This app uses Flask and Jinja to render the HTML.

My main tought was to make layout.html to reuse and implement the navbar, when rendering templates on the backend i will assign each template a "tab" value, and will be useful for the navbar links highlighting, example : when clicking **Introduction** once on the page the **Introduction** word on the navbar will light up

First, the **Main Page**, it contains a beautiful pixel art GIF that acts as a background, the title and a container that holds two links, one that redirects to the **Introduction** page and the other one on the **Dream Journal**.

Then comes the Introduction page. It contains basic info about lucid dreaming methods and basic awareness tips. I used a table to display the methods and their difficulty level.

I also added a **Dream Journal** page where users can record their dreams wich is one of the fundamentals of lucid dreaming. It works by first opening a bootstrap modal when clicking the "Add Dream" button, the form inside the modal contains three inputs, "Dream Title", "Dream Desc" and "Lucid?".
When clicking on the "Add Dream" button, it will fire a javascript function that first get the user browser local storage and search for the key "dreams", if not found, it will just use an empty array, then update the array with the new dream before updating the local storage and reloading the page.
For the dreams rendering on screen, javascript will get the dreams array and for each dream, render an html container with the dream info, name, desc and will change the border color based on lucidity.

Finally my **Quiz** page

