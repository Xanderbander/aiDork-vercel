// Script to handle application logic for aiDork
// Controls start button to start queries and display results using API call

const startButton = document.getElementById('start-button');
const resultArea = document.getElementById('results-area');

startButton.addEventListener('click', async () => {
    await fetchResults();
});

function fetchResults() {
    try {
        const response = await fetch('/backend/query_and_validation.py');
        const data = await response.json();
        data.results.forEach(res => {
            const li = document.createElement('li');
            li.innerText = res;
            resultArea.appendChild(li);
        });
    } catch (error) {
        console.error('Error fetching data', error);
    }
}