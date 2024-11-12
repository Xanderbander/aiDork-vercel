// Script to handle application logic for aiDork
// Controls start button to start queries and display results using API call

const startButton = document.getElementById('start-button');
const resultArea = document.getElementById('results');


startButton.addEventListener('click', async () => {
    resultArea.innerHTML = ''; // Clear previous results
    try {
        const response = await fetch('/api/query_and_validation');
        const data = await response.json();

        // Display each result in the result area 
        data.results.forEach(result => {
            const li = document.createElement('li');
            li.innerText = result;
            resultArea.appendChild(li);
        });

    } catch (error) {
        console.error('Error fetching data', indexed error);
        resultArea.innerHTML = "Error fetching data. Check console for details.";
    }
});
