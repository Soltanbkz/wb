let header = document.querySelector("header");
let menu = document.querySelector("#menu-icon");
let navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
  header.classList.toggle("shadow", window.scrollY > 0);
});

menu.onclick = () => {
  navbar.classList.toggle("active");
};
window.onscroll = () => {
  navbar.classList.remove("active");
};

// Dark Mode / light mode
let darkmode = document.querySelector("#darkmode");

darkmode.onclick = () => {
  if (darkmode.classList.contains("bx-moon")) {
    darkmode.classList.replace("bx-moon", "bx-sun");
    document.body.classList.add("active");
  } else {
    darkmode.classList.replace("bx-sun", "bx-moon");
    document.body.classList.remove("active");
  }
};


// popup

const viewBtn = document.querySelector(".view-modal"),
    popup = document.querySelector(".popup"),
    close = popup.querySelector(".close"),
    field = popup.querySelector(".field"),
    input = field.querySelector("input"),
    copy = field.querySelector("button");

    viewBtn.onclick = ()=>{ 
      popup.classList.toggle("show");
    }
    close.onclick = ()=>{
      viewBtn.click();
    }

    copy.onclick = ()=>{
      input.select(); //select input value
      if(document.execCommand("copy")){ //if the selected text is copied
        field.classList.add("active");
        copy.innerText = "Copied";
        setTimeout(()=>{
          window.getSelection().removeAllRanges(); //remove selection from page
          field.classList.remove("active");
          copy.innerText = "Copy";
        }, 3000);
      }
    }

// Когда пользователь прокручивает страницу, проверяем, когда элемент находится на экране
window.addEventListener("scroll", function() {
  var element = document.querySelector(".view-modal");
  var position = element.getBoundingClientRect().top;
  var windowHeight = window.innerHeight;

  // Если элемент находится на экране, показываем его
  if (position < windowHeight) {
    element.style.opacity = "1";
  }
});

 // Когда пользователь прокручивает страницу, проверяем, когда элемент находится на экране
 window.addEventListener("scroll", function() {
  var element = document.querySelector(".view-modal");
  var position = element.getBoundingClientRect().top;

  // Если элемент находится над верхней границей окна браузера, скрываем его
  if (position < 0) {
    element.style.opacity = "0";
  } else {
    element.style.opacity = "1";
  }
});


function t898_init(recId) {
    var rec = document.getElementById('rec' + recId);
    if (!rec)
        return;
    var container = rec.querySelector('.t898');
    if (!container)
        return;
    rec.setAttribute('data-animationappear', 'off');
    rec.style.opacity = 1;
    var whatsApp = rec.querySelector('.t898__icon-whatsapp_wrapper');
    if (whatsApp) {
        var whatsAppHref = whatsApp.getAttribute('href');
        if (whatsAppHref && (whatsAppHref.indexOf('whatsapp://') > -1 || whatsAppHref.indexOf('wa.me') > -1)) {
            t898_removeExtraSymbolsFromWhatsApp(whatsApp, whatsAppHref)
        }
    }
    if (window.lazy === 'y' || document.getElementById('allrecords').getAttribute('data-tilda-lazy') === 'yes') {
        t_onFuncLoad('t_lazyload_update', function() {
            t_lazyload_update()
        })
    }
}
function t898_removeExtraSymbolsFromWhatsApp(whatsApp, whatsAppHref) {
    if (whatsAppHref && whatsAppHref.indexOf('?text=') !== -1) {
        var whatsAppHrefArr = whatsAppHref.split('?text=');
        whatsAppHrefArr[0] = whatsAppHrefArr[0].replace(/[\(\)+-]/g, '');
        whatsAppHref = whatsAppHrefArr[0] + '?text=' + whatsAppHrefArr[1]
    } else {
        whatsAppHref = whatsAppHref.replace(/[\(\)+-]/, '')
    }
    whatsApp.setAttribute('href', whatsAppHref)
}
