document.addEventListener("DOMContentLoaded", function () {
    const opinionCards = document.querySelectorAll(".opinion-card");

    function showCardsOnScroll() {
        const triggerBottom = window.innerHeight * 0.85; // 85% viewport height

        opinionCards.forEach((card, index) => {
            const cardTop = card.getBoundingClientRect().top;

            if (cardTop < triggerBottom) {
                setTimeout(() => {
                    card.classList.add("show"); // Add class to trigger animation
                }, index * 200); // Delay each card slightly for a staggered effect
            }
        });
    }

    // Run on scroll
    window.addEventListener("scroll", showCardsOnScroll);
    showCardsOnScroll(); // Run immediately in case they are already in view
});
