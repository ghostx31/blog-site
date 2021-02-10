const tbtn = document.querySelectorAll(".side-nav ul li");
const tab = document.querySelectorAll(".tabs");
function show(panelIndex){
    tab.forEach(function(node){
        node.style.display = "none";
    })
    tab[panelIndex].style.display = "block";
}
show(0)


$(".side-nav ul li").click(function(){
    $(this).addClass("active").siblings().removeClass("active");
})

