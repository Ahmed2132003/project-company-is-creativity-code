// إضافة تأثير نبض عند النقر على الأزرار
document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".button");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            button.classList.add("pulse");
            setTimeout(() => button.classList.remove("pulse"), 300);
        });
    });
});
