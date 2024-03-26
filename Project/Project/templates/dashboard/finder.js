document.addEventListener("DOMContentLoaded", function () {
    const filterForm = document.getElementById("filterForm");
    const houseBoxes = document.querySelectorAll(".house-box");

    filterForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission

        // Retrieve filter values
        const price = parseInt(document.getElementById("price").value);
        const location = document.getElementById("location").value.toLowerCase();
        const area = document.getElementById("area").value.toLowerCase();
        const type = document.getElementById("type").value.toLowerCase();

        // Iterate through house listings
        houseBoxes.forEach(function (houseBox) {
            const houseLocation = houseBox.getAttribute("data-location").toLowerCase();
            const houseArea = houseBox.getAttribute("data-area").toLowerCase();
            const housePrice = parseInt(houseBox.getAttribute("data-price"));
            const houseType = houseBox.getAttribute("data-type").toLowerCase();

            // Check if house listing matches filter criteria
            const matchesFilter = (
                (price === 0 || housePrice <= price) &&
                (location === '' || houseLocation.includes(location)) &&
                (area === '' || houseArea.includes(area)) &&
                (type === '' || houseType === type)
            );

            // Show/hide house listing based on filter results
            houseBox.style.display = matchesFilter ? "block" : "none";
        });
    });

    // Update price value display on range input change
    document.getElementById("price").addEventListener("input", function () {
        document.getElementById("priceValue").textContent = "$" + this.value;
    });
});
