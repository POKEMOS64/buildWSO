$(function(){
  $(window).scroll(function(){
    var winTop = $(window).scrollTop();
    if(winTop >= 40){
      $(".static").addClass("sticky-header");
    }else{
      $(".static").removeClass("sticky-header");
    }//if-else
  });//win func.
});//ready func.



$('.owl-carousel').owlCarousel({
  loop:true,
  margin:10,
  nav:true,
  navText: ["Назад","Вперед"],
  responsive:{
      0:{
          items:1
      },
      600:{
          items:2
      },
      1000:{
          items:3
      }
  }
})

if( $(document).height() <= $(window).height() ){		
  $(".fix_footer").addClass("fixed-bottom");
}

function openDebt(evt, DebtClick){
  var i, tabcontent, tablinks;

  tabcontent = document.getElementsByClassName('tabcontent');
  for (i=0; i < tabcontent.length; i++){
    tabcontent[i].style.display = 'none';
  }
  tablinks = document.getElementsByClassName("tablinks");
  for(i=0; i< tablinks.length; i++){
    tablinks[i].className = tablinks[i].className.replace(" active",'');
  }
  document.getElementById(DebtClick).style.display = 'block';
  evt.currentTarget.className +=' active';
}

$(window).on('load', function () {
  $('.preloader-6').addClass("preloader-remove");     
});

document.addEventListener('DOMContentLoaded', (event) => {
document.querySelector('.target-burger').addEventListener("click",function(){
    document.querySelector('body').classList.toggle('toggled');
})
})