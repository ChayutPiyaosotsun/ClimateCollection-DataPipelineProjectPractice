document.addEventListener('DOMContentLoaded', () => {
    const graphButtons = document.querySelectorAll('.show-graphs');
    const graphsContainer = document.getElementById('graphs-container');
    const boxplotImage = document.getElementById('boxplot');
    const histogramImage = document.getElementById('histogram');
    const monthlyTrendImage = document.getElementById('monthly-trend');
    const scatterPlotImage = document.getElementById('scatter-plot');

    graphButtons.forEach(button => {
        button.addEventListener('click', () => {
            const city = button.getAttribute('data-city');
            // Update the src attribute and display the image
            boxplotImage.src = `graphs/${city}-boxplot.png`;
            histogramImage.src = `graphs/${city}-histogram.png`;
            monthlyTrendImage.src = `graphs/${city}-monthly-trend.png`;
            scatterPlotImage.src = `graphs/${city}-scatter-plot.png`;
            boxplotImage.style.display = 'block';
            histogramImage.style.display = 'block';
            monthlyTrendImage.style.display = 'block';
            scatterPlotImage.style.display = 'block';
        });
    });
});
