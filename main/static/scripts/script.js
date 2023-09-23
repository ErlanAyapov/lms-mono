var menu_status = 'opened';


function menu_position(menu_status) {
	if (menu_status == 'closed') {
		$("#open_menu_text").css("display","none")
		$(".nav-link-text").css("display", 'none');
		$("#open_menu").css("display", 'block');	
		$("nav").css("width", '60px');	
		$("nav").css("padding-top", '60px');	
		$("nav li").css("padding", '15px');	
		// $(".container").css("margin-left", '80px');	
		$("#open_menu").css("left", '45px');
	} else if (menu_status == 'opened') {
		$("#open_menu_text").css("display","inline-block");
		$(".nav-link-text").css("display", 'inline-block');
		$("#open_menu").css("display", 'inline-block');	
		$("nav").css("width", '250px');	
		$("nav").css("padding-top", '20px');	
		$("nav li").css("padding", '0');	
		$("nav li").css("padding-top", '10px');	
		$("nav li").css("padding-left", '60px');	
		$("#open_menu").css("left", '235px');
		// $(".container").css("margin-left", '250px');
	}	
};

jQuery('#open_menu').on('click', function() {
	if (menu_status == 'opened') {
		menu_position('closed')
		menu_status = 'closed'
	} else {
		menu_position('opened')	
		menu_status = 'opened'
	}
	localStorage.setItem('menu_status', menu_status)
}); 

$('input').on('input invalid', function() {
	this.setCustomValidity('')
	if (this.validity.valueMissing) {
		this.setCustomValidity("Осы жолақты толтыру міндетті")
	}
	if (this.validity.typeMismatch) {
		this.setCustomValidity("Енгізілген деректер типі сәйкес емес")
	}
	if (this.validity.patternMismatch) {
		this.setCustomValidity("Паттернге сәйкес емес")
	}
});

$('textarea').on('input invalid', function() {
	this.setCustomValidity('')
	if (this.validity.valueMissing) {
		this.setCustomValidity("Алдымен кодты жазыңыз")
	}
	if (this.validity.typeMismatch) {
		this.setCustomValidity("Енгізілген деректер типі сәйкес емес")
	}
	if (this.validity.patternMismatch) {
		this.setCustomValidity("Паттернге сәйкес емес")
	}
});

menu_position( localStorage.getItem('menu_status') );

window.addEventListener('scroll', function () {
	const scrollPosition = window.scrollY; 
	if (scrollPosition >= 88) {
		$("nav").css("position", 'fixed');	
		$("nav").css("top", '0');	

	}
	 else {
		$("nav").css("position", 'absolute');	
		$("nav").css("top", '88px');	

	}
});

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});