(function () {
    const btnDelete = document.querySelectorAll('.btnDelete');

    btnDelete.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Are you sure you want to delete it?')) {
                e.preventDefault();
            }
        });
    });
})();